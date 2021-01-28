from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        #self.setundobuffer(1000)
        #self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        print(f"score = {self.score}")
        self.write("score", move=False, align="center", font=("Arial", 24, "normal"))

