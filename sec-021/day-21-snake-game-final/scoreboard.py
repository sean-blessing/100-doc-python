from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # need to change color of scoreboard to white so it shows up!
        self.color("white")
        # turtle icon still shows so we need to hide it
        self.hideturtle()
        # hide pen then move score to top of screen
        self.penup()
        self.goto(0, 260)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)
