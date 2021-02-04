from turtle import Turtle, Screen

# width=20, height=20, x=0,y=0

INIT_SPEED = .1

class Ball(Turtle):

    #ball needs to know initial heading and the screen its moving inside
    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.goto(0, 0)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed = INIT_SPEED

    def move(self):
        # my version was far more complicated...  converting to instructor version
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.speed = INIT_SPEED