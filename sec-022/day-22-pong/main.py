# screen width = 800, height = 600
# color black
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed -= .005 if ball.speed > 0 else 0

    #detect right paddle miss
    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset_position()

    # detect left paddle miss
    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()