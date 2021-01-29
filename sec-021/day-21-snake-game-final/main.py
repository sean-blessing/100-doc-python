from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.bgcolor("black")
screen.title("My Snake Game")

game_is_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()
#scoreboard.display()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey( key="Left", fun=snake.left)
screen.onkey( key="Right", fun=snake.right)

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        print(f"nom nom nom!  score is {scoreboard.score}")



screen.exitonclick()