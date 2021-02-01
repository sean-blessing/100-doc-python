# screen width = 800, height = 600
# color black
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball(45, screen)

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    curr_heading = ball.heading()
    ball.move(curr_heading)
    screen.update()
    time.sleep(.5)

screen.exitonclick()