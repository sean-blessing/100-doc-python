from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.bgcolor("black")
screen.title("My Snake Game")

game_is_on = True
snake = Snake()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey( key="Left", fun=snake.left)
screen.onkey( key="Right", fun=snake.right)

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()


screen.exitonclick()
