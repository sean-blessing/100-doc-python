from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        # create right paddle:  width=20, height=100, x_pos=250, y_pos=0, keypress moves up and down by 20 pixels
        # all turtles start as 20 x 20...  need to leave width alone and stretch height x 5
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto((x_cor, y_cor))
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        # x pos doesn't change... only y
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        # x pos doesn't change... only y
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)