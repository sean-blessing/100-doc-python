from turtle import Turtle, Screen

# draw a dashed line...  solid line 10 paces,
# gap for 10 paces, repeat 50 times
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
for _ in range (15):
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)

screen = Screen()
screen.exitonclick()
