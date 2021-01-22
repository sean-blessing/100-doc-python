import turtle as t
from turtle import Screen
import random
color_list = [(25, 108, 164), (194, 38, 81), (238, 161, 49), (234, 215, 85), (226, 237, 228), (223, 137, 176), (144, 108, 56), (102, 197, 219), (206, 166, 29), (20, 57, 132), (214, 73, 90), (239, 89, 50), (141, 208, 227), (118, 192, 140), (3, 186, 176), (106, 107, 199), (138, 29, 73), (4, 161, 86), (98, 51, 36), (22, 156, 210), (232, 165, 184), (175, 185, 221), (29, 90, 95), (233, 172, 161), (152, 213, 190), (242, 205, 8), (89, 48, 31), (39, 46, 81), (26, 97, 94)]
screen = Screen()
#screen.setup(width=600, height=600)
#t.setworldcoordinates(-1, -1, 20, 20)
#10 x 10 grid of dots
# 20 in size
# 50 spaced

#draw dots in turtle

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.speed("fastest")
t.colormode(255)

timmy_the_turtle.setheading(225)
timmy_the_turtle.penup()
timmy_the_turtle.forward(300)
# start loop?
for i in range(0, 5):
    timmy_the_turtle.setheading(0)
    for _ in range(10):
        timmy_the_turtle.dot(20, random.choice(color_list))
        timmy_the_turtle.forward(50)
    timmy_the_turtle.setheading(90)
    timmy_the_turtle.forward(50)
    timmy_the_turtle.setheading(180)

    for _ in range(10):
        timmy_the_turtle.forward(50)
        timmy_the_turtle.dot(20, random.choice(color_list))
    timmy_the_turtle.setheading(90)
    timmy_the_turtle.forward(50)
#start w/ penup
# t.penup()
# # go to bottom left corner
# t.goto(-300, -300)
# print(f"turtle position = {timmy_the_turtle.position()}")
# timmy_the_turtle.dot(20, random.choice(color_list))
# timmy_the_turtle.penup()
# timmy_the_turtle.forward(2)
#
# timmy_the_turtle.color(color_list[1])
# timmy_the_turtle.dot(20)
# timmy_the_turtle.penup()
# timmy_the_turtle.forward(2)
#
# timmy_the_turtle.color(color_list[2])
# timmy_the_turtle.dot(20)
# timmy_the_turtle.penup()
# timmy_the_turtle.forward(2)
#
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(2)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(2)
# timmy_the_turtle.right(180)


print("done")

screen.exitonclick()