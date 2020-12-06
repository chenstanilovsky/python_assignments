import turtle
import random as rand
import create_board as cb
import game_engine as ge

def get_username(s):
    username = s.textinput("Memory Master", "Your name:")
    while(len(username) == 0):
        username = s.textinput("Memory Master", "Invalid name, please try again\nYour name:")
    return username

def get_num_cards(s):
    num_cards = s.numinput("Memory Master", "# of cards:\n(Please enter 8, 10, or 12)")
    while( num_cards < 8 or num_cards > 12 or num_cards % 2 == 1):
        num_cards = s.numinput("Memory Master", "Invalid amount, please try again\n# of cards:\n(Please enter 8, 10, or 12)")
    return num_cards

def generate_turtles():
    turtle_dict = {}

    box_turtle = turtle.Turtle()
    box_turtle.hideturtle()
    box_turtle.width(5)
    turtle_dict["box"] = box_turtle

    status_turtle = turtle.Turtle()
    status_turtle.hideturtle()
    turtle_dict["status"] = status_turtle

    highscore_turtle = turtle.Turtle()
    highscore_turtle.hideturtle()
    turtle_dict["highscore"] = highscore_turtle

    quit_turtle = turtle.Turtle()
    quit_turtle.hideturtle()
    turtle_dict["quit"] = quit_turtle

    return turtle_dict

def shuffle(cards):
    for i in range(0, 100):
        rand1 = rand.randint(0, len(cards) - 1)
        rand2 = rand.randint(0, len(cards) - 1)
        # Swap two random elements in new_cards list
        temp = cards[rand1]
        cards[rand1] = cards[rand2]
        cards[rand2] = temp

def init_game(s, t_dict): # s -> screen, t -> turtle
    s.setup(width = 800, height = 800, startx = 600, starty = 0) # reset start x to 0 after testing

    username = get_username(s)
    num_cards = get_num_cards(s)

    cb.draw_board(t_dict["box"])
    cb.fill_board(s, t_dict["status"], t_dict["highscore"])
    cb.add_quit_button(s,t_dict["quit"])

    cards = ge.generate_cards_list(num_cards)
    shuffle(cards)
    t_cards = ge.generate_cards_turtles(s,cards)
    placement_x, placement_y = cb.place_cards(t_cards)

    ge.start_game(s, t_dict, cards, t_cards, placement_x, placement_y, username)

def main():
    screen = turtle.getscreen()
    turtle.hideturtle()


    turtle_dict = generate_turtles()
    init_game(screen, turtle_dict)
    
    turtle.done() # this line stops the screen from instantly closing

if __name__ == "__main__":
    main()