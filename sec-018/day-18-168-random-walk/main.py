from turtle import Screen
import turtle as t
import random

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
#colors = ["blue", "red", "black", "green", "orange", "pink", "purple", "indigo", "yellow", "cyan"]
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
turns = [90, 180, 270, 360]

#draw a random walk
# make pen wider
# random color each walk
timmy_the_turtle.width(15)
timmy_the_turtle.speed("fastest")
#how many walks??
for _ in range(50):

    angle = random.choice(turns)
    color = random_color()
    timmy_the_turtle.color(color)
    timmy_the_turtle.right(angle)
    timmy_the_turtle.forward(50)

screen = Screen()
screen.exitonclick()
