from turtle import Screen
import turtle as t
import random

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.speed("fastest")
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
turns = [90, 180, 270, 360]

#draw a circle... with a certain width... then alter the tilt
for x in range(0, 360, 5):
    color = random_color()
    timmy_the_turtle.color(color)
    timmy_the_turtle.circle(100)
    timmy_the_turtle.left(5)
# make pen wider
# random color each walk
#timmy_the_turtle.width(15)
#timmy_the_turtle.speed("fastest")
#how many walks??
# for _ in range(50):
#
#     angle = random.choice(turns)
#     color = random_color()
#     timmy_the_turtle.color(color)
#     timmy_the_turtle.right(angle)
#     timmy_the_turtle.forward(50)

screen = Screen()
screen.exitonclick()