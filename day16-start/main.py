#import turtle

#timmy = turtle.Turtle()

#doc:  https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen
timmy = Turtle()

print(timmy)
timmy.shape("turtle")
timmy.color("green")
timmy.fd(100)

my_screen = Screen()

print(my_screen.canvheight)
my_screen.exitonclick()