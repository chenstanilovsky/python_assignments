import turtle

def move_to(t,x,y):
    t.up()
    t.setpos(x,y)

def draw_to(t,x,y):
    t.down()
    t.setpos(x,y)

def draw_main(t):
    move_to(t,-370, 370)
    draw_to(t,100, 370)
    draw_to(t,100,-260)
    draw_to(t,-370,-260)
    draw_to(t,-370,370)

def draw_highscores(t):
    move_to(t,135,370)
    draw_to(t,360,370)
    draw_to(t,360,-260)
    draw_to(t,135,-260)
    draw_to(t,135,370)

def draw_stats(t):
    move_to(t,-370,-275)
    draw_to(t,100,-275)
    draw_to(t,100,-370)
    draw_to(t,-370,-370)
    draw_to(t,-370,-275)

def draw_board(t):
    draw_main(t)
    draw_stats(t)
    draw_highscores(t)
 
def get_highscores(s, file):
    datum = []
    try:
        with open(file, "r") as f:
            for line in f:
                if line[-1] == "\n":
                    line = line[:-1]
                if(len(line) == 0):
                    continue
                data = line.split(" ")
                datum.append(data)
    except IOError:
        open("highscores.txt", "w")
        s.addshape("./assets/leaderboard_error.gif")
        t_hs_error = turtle.Turtle()
        t_hs_error.hideturtle()
        move_to(t_hs_error, 250, 200)
        t_hs_error.shape("./assets/leaderboard_error.gif")
        t_hs_error.showturtle()
    
    return datum
            
def fill_highscores(t, hs):
    move_to(t, 150, 330)
    t.write("Leaderboard:",font=("Arial", 20,"normal"))
    x = 150
    y = 275
    for score in hs:
        move_to(t,x,y)
        entry = score[0] + " " + score[1]
        t.write(entry, font=("Arial", 20,"normal"))
        y -= 75

def fill_stats(t, guesses, matches):
    t.clear()
    move_to(t,-360,-300)
    t.write("Status", font=("Arial", 20,"normal"))
    move_to(t, -360, -330)
    t.write("Guesses: " + str(guesses), font=("Arial", 20,"normal"))
    move_to(t, -360, -360)
    t.write("Matches: " + str(matches), font=("Arial", 20,"normal"))

def fill_board(s, status_t, highscore_t):
    hs_list = get_highscores(s, "highscores.txt")
    fill_highscores(highscore_t,hs_list)
    fill_stats(status_t, 0, 0)

def add_quit_button(s,t):
    s.addshape("./assets/quitbutton.gif")
    t.shape("./assets/quitbutton.gif")
    move_to(t,160,-290)
    t.showturtle()
    
def place_cards(t_cards):
    placementx = []
    placementy = []
    if len(t_cards) == 8:
        placementx = [-300, -190, -80, 30, -300, -190, -80, 30]
        placementy = [250, 250, 250, 250, 50, 50, 50, 50]
    elif len(t_cards) == 10:
        placementx = [-300, -190, -80, 30, -300, -190, -80, 30, -190, -80]
        placementy = [250, 250, 250, 250, 50, 50, 50, 50, -150, -150]
    else:
        placementx = [-300, -190, -80, 30, -300, -190, -80, 30, -190, -80, -300, 30]
        placementy = [250, 250, 250, 250, 50, 50, 50, 50, -150, -150, -150, -150]

    for i in range(len(t_cards)):
        move_to(t_cards[i],placementx[i],placementy[i])
        t_cards[i].showturtle()
    
    return placementx, placementy