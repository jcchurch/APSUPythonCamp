import turtle
import random

X = -300
Y = -100
GOAL = 300
colors = ["cyan","coral","mediumblue","greenyellow","black","indigo","darkviolet"]

def draw_goal_line():
    t = turtle.Turtle()
    t.penup()
    t.setposition(GOAL, 300)
    t.right(90)
    t.pendown()
    t.forward(600)

def draw_fresh_penstroke(t):
    t.pensize(random.randint(0, 10)+5)
    t.forward(random.randint(0, 100))

def draw_turtle_movement(t):
    draw_fresh_penstroke(t)
    t.left(90)
    draw_fresh_penstroke(t)
    t.right(90)
    draw_fresh_penstroke(t)
    t.right(90)
    draw_fresh_penstroke(t)
    t.left(90)

def build_turtles():
    turtles = []
    for i in range(len(colors)):
        t = turtle.Turtle()
        t.penup()
        t.setposition(X,Y + i*25)
        t.pendown()
        t.color(colors[i])
        turtles.append(t)
    return turtles

def did_any_turtle_reach_goal(turtles):
    for t in turtles:
        if t.position()[0] >= GOAL:
            return True
    return False

def which_turtle_moved_farthest(turtles):
    farthest_turtle = turtles[0]
    for t in turtles:
            if t.position()[0] >= farthest_turtle.position()[0]:
                farthest_turtle = t
    return farthest_turtle

if __name__ == '__main__':
    draw_goal_line()
    turtles = build_turtles()
    while did_any_turtle_reach_goal(turtles) == False:
        for t in turtles:
            draw_turtle_movement(t)

    t = which_turtle_moved_farthest(turtles)
    print("Our winning turtle was the", t.color()[0], "turtle.")

    turtle.update() #render image
    turtle.exitonclick()  #wait for mouse click

