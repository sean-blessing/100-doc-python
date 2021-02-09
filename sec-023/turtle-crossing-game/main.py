import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
# turn off tracer
screen.tracer(0)
# create a player turtle at bottom of screen
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# add keypress listener to detect up arrow, moving player north with each keypress
screen.listen()
screen.onkeypress(player.move, "Up")
game_is_on = True
car_gen = 1
while game_is_on:
    # only generate a car once in every 6 times through this loop
    # make it random to make the generation more dynamic
    car_gen = True if random.randint(1,6) == 1 else False
    if car_gen:
        rand_y = random.randint(-250, 250)
        car = car_manager.gen_car(300, rand_y)
        car_gen = 1
    car_manager.move_cars()
    time.sleep(0.1)
    screen.update()

    # detect collision with a car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            print("you hit a car... game over!")
            scoreboard.game_over()

    # detect when player reaches the other side
    if player.reached_finish():
        # you win!
        print("You leveled-up!")
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increment_level()


screen.exitonclick()