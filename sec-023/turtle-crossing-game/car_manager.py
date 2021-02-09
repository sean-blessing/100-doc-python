from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def gen_car(self, x_cor, y_cor):
        car = Turtle("square")
        car.color(random.choice(COLORS))
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        # generate at random pos along y-axis in range from (top - 50px) and (bottom - 50px), passed from main
        car.goto(x_cor, y_cor)
        self.cars.append(car)

    def move_cars(self):
        # loop through and move each car
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

