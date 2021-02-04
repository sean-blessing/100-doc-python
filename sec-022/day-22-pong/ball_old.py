from turtle import Turtle, Screen

# width=20, height=20, x=0,y=0

class Ball(Turtle):
    #ball needs to know initial heading and the screen its moving inside
    def __init__(self, init_heading, bound_screen):
        super().__init__("circle")
        self.bound_screen = bound_screen
        self.color("white")
        self.goto(0, 0)
        self.setheading(init_heading)
        self.penup()

    def move(self, heading):
        #is ball at upper or lower bound of screen?
        #need to subtract from canvheight to prevent ball from moving off screen
        upper_bound = self.bound_screen.canvheight - 20
        lower_bound = upper_bound * -1
        ball_x = self.xcor()
        #print(f"ball_x = {ball_x}, upper_bound = {upper_bound}, lower_bound = {lower_bound}")
        if ball_x >= upper_bound:
            #print(f"UPPER BOUND HIT.  heading = {heading}")
            #upper bound reached... bounce!
            if heading == 135:
                #print("changing heading to 225")
                heading = 225
            elif heading == 45:
                #print("changing heading to 315")
                heading = 315
        elif ball_x <= lower_bound:
            #print("LOWER BOUND HIT")
            #lower bound reached... bounce!
            if heading == 315:
                heading = 45
            elif heading == 225:
                heading = 135
        # ball should accept a heading and move 20 pixels in that direction
        self.setheading(heading)
        self.forward(10)