from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


def get_high_score_from_file():
    with open("data.txt") as file:
        contents = file.read()
        # contents should have the high score but its a string.
        # return high score variable from contents
        return int(contents)




class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # get high score from file
        self.high_score = get_high_score_from_file()
        # need to change color of scoreboard to white so it shows up!
        self.color("white")
        # turtle icon still shows so we need to hide it
        self.hideturtle()
        # hide pen then move score to top of screen
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score: {self.score} High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_new_high_score_in_file()
        self.score = 0
        self.update_score()

    def set_new_high_score_in_file(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
