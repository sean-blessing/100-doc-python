from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
colors = ["blue", "red", "black", "green", "orange", "pink", "purple", "indigo", "yellow", "cyan"]

#draw some shapes
# 360 degrees / # of sides
# 3 sided shape to 10 sided shape
# each side is 100 length
#-triangle - 3 sides, 120 degrees
#-square - 4 sides, 90 degrees
#-pentagon - 5 sides, 72 degrees
# etc

for num_sides in range(3, 11):
    print(f"drawing a {num_sides} sided object...")
    angle = 360 / num_sides
    color = random.choice(colors)
    timmy_the_turtle.color(color)
    for n in range(0,num_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

screen = Screen()
screen.exitonclick()
