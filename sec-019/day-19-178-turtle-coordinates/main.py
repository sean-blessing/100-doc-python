from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False

user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win? Enter a color:  ")

# coordinates:
# 0,0 is center.  if height = 400, then 200 y is top, -200 is bottom
# 6 turtles spread across left side, y coords [-125, -75, -25, 25, 75, 125]
y_coords = [-125, -75, -25, 25, 75, 125]
for idx in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[idx])
    new_turtle.penup()
    new_turtle.goto(-230, y_coords[idx])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for t in turtles:
        if t.xcor() > 230:
            is_race_on = False
            print(f"{t.pencolor()} wins!!!")
            if t.pencolor()==user_bet:
                print("You picked correctly!")
            else:
                print("You picked the wrong turtle.  Sorry!")
        dist = random.randint(0, 10)
        t.forward(dist)

screen.exitonclick()
