import turtle;
import math;
import PositionService as ps;

CIRCLE_RADIUS = 80

# Update Position of Circle
def set_ps(x,y):
    ps.set_position(x,y)
    ps.set_visible(True)

# Move turtle without making line while changing positions
def move_and_draw(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.circle(CIRCLE_RADIUS)

# Response when the screen is clicked
def response(x,y):

    # Print click coordinates
    print("Click occured at: {}, {}".format(x,y))

    if not ps.is_visible:
        # if click happened with no existing circle
        move_and_draw(x,y)
        set_ps(x,y)
        return

    # x² + y² = r² <-- Circle function
    # distance from center formula: sqrt ((x1-x)² + (y1-y)²)
    # if distance from center is less than or equal to the radius, the click was inside the circle
    # if distance from cetner is more than radius, the click was outside of the circle
    center_x = ps.get_position_x()
    center_y = ps.get_position_y() + 80
    distance_from_center = math.sqrt( (x - center_x)**2 + (y - center_y)**2)


    if distance_from_center <= CIRCLE_RADIUS:
        # if click was inside of an existing circle
        t.clear()
        ps.set_visible(False)
        ps.set_position(-9999, -9999)
    elif distance_from_center > CIRCLE_RADIUS:
        # if click was outside of an existing circle
        t.clear()
        move_and_draw(x,y)
        set_ps(x,y)

# init screen
s = turtle.getscreen()
s.bgpic("shape_window.png")
s.setup(width = 970, height = 635, startx = 0, starty = 0)

# init turtle
t = turtle.Turtle()
t.pencolor("green")

# Create first circle at 0,0
t.circle(CIRCLE_RADIUS)
ps.PositionService()
ps.set_position(0,0)
ps.set_visible(True)

# When the screen is clicked
s.onclick(response)
s.mainloop()

    






    









