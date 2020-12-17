import turtle
import time
import create_board as cb


guesses = 0
matches = 0
curr_selected = None

def generate_default_config():
    with open("cards.cfg", "w") as f:
        f.write("./assets/2_of_clubs.gif\n")
        f.write("./assets/2_of_diamonds.gif\n")
        f.write("./assets/3_of_hearts.gif\n")
        f.write("./assets/ace_of_diamonds.gif\n")
        f.write("./assets/jack_of_spades.gif\n")
        f.write("./assets/king_of_diamonds.gif")

def getKCards(k):
    cards_list = []
    try:
        with open("cards.cfg", "r") as f:
            for i in range(int(k/2)):
                line = f.readline()
                if(line[-1] == "\n"):
                    line = line[:-1]
                cards_list.append(line)
                cards_list.append(line)
    except IOError:
        generate_default_config()
        return getKCards(k)
    return cards_list

def generate_cards_list(num):
    cards = getKCards(num)
    return cards

def generate_cards_turtles(s, cards):
    t_cards = []
    s.addshape("./assets/card_back.gif")
    for i in range(len(cards)):
        turtle.hideturtle()
        turt = turtle.Turtle()
        s.addshape(cards[i])
        turt.shape("./assets/card_back.gif")
        t_cards.append(turt)
    return t_cards

def select_card(card, t_card):
    t_card.shape(card)

def remove_cards(cards, t_cards, idx_1, idx_2, pl_x, pl_y):
    if idx_1 < idx_2:
        temp = idx_1
        idx_1 = idx_2
        idx_2 = temp

    t_cards[idx_1].hideturtle()
    del(t_cards[idx_1])
    del(cards[idx_1])
    del(pl_x[idx_1])
    del(pl_y[idx_1])

    t_cards[idx_2].hideturtle()
    del(t_cards[idx_2])
    del(cards[idx_2])
    del(pl_x[idx_2])
    del(pl_y[idx_2])

def place_down_card(t_card):
    t_card.shape("./assets/card_back.gif")

def do_nothing(x,y):
    x = 1

def quit_game(s):
    s.addshape("./assets/quitmsg.gif")
    s.onclick(do_nothing)
    t_quit_msg = turtle.Turtle()
    t_quit_msg.shape("./assets/quitmsg.gif")

def write_highscores(hs):
    with open("highscores.txt", "w") as f:
        for score in hs:
            f.write(str(score[0]) + " " + str(score[1]) + "\n")

def update_highscores(s, guesses, name):
    hs = cb.get_highscores(s, "highscores.txt")
    for i in range(len(hs)):
        if guesses < int(hs[i][1]):
            hs.insert(i, [name, guesses])
            break
    if len(hs) == 0:
        hs.append([name, guesses])
    if len(hs) > 8:
        hs = hs[0:8]
    write_highscores(hs)



def win_game(s,name):
    global guesses

    s.addshape("./assets/winner.gif")
    s.onclick(do_nothing)
    t_win_msg = turtle.Turtle()
    t_win_msg.shape("./assets/winner.gif")
    update_highscores(s, guesses, name)

def start_game(s, t_dict, cards, t_cards, pl_x, pl_y, name):
    def process_click(x,y):
        s.onclick(do_nothing)
        # First check if quit button was clicked
        if x >= 130 and x <= 190:
            if y >= -310 and y <= -270:
                quit_game(s)
        global guesses
        global matches
        global curr_selected
        for i in range(len(pl_x)):
            if x >= pl_x[i] - 50 and x <= pl_x[i] + 50:
                if y >= pl_y[i] - 75 and y <= pl_y[i] + 75:
                    if curr_selected == None:
                        select_card(cards[i], t_cards[i])
                        curr_selected = i
                        break
                    elif cards[curr_selected] == cards[i]:
                        select_card(cards[i], t_cards[i])
                        time.sleep(1)
                        remove_cards(cards, t_cards, curr_selected, i, pl_x, pl_y)
                        matches += 1
                        guesses += 1
                        cb.fill_stats(t_dict["status"], guesses, matches)
                        curr_selected = None
                        if len(cards) == 0:
                            win_game(s, name)
                        break
                    else:
                        select_card(cards[i], t_cards[i])
                        time.sleep(1)
                        place_down_card(t_cards[curr_selected])
                        place_down_card(t_cards[i])
                        guesses += 1
                        cb.fill_stats(t_dict["status"], guesses, matches)
                        curr_selected = None
                        break
        s.onclick(process_click)
    s.onclick(process_click)
    turtle.mainloop()

    

