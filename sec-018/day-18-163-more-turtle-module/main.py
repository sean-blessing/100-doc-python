from turtle import Turtle, Screen
#can alias modules too
#import turtle as t
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
#timmy_the_turtle.shapesize(5,5,12)
timmy_the_turtle.color("red")
for n in range(0, 200,5):
    fwd = 5 + (n)
    timmy_the_turtle.forward(fwd)
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(fwd)
    timmy_the_turtle.left(90)






screen = Screen()
screen.exitonclick()
