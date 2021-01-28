from turtle import Turtle

UP = 90;
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []

        for pos in self.starting_positions:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(pos)
            self.segments.append(new_segment)
        self.head = self.segments[0]

    def move(self):
        start_idx = len(self.segments) - 1
        for idx in range(start_idx, 0, -1):
            this_seg = self.segments[idx]
            next_seg = self.segments[idx - 1]
            this_seg.setx(next_seg.xcor())
            this_seg.sety(next_seg.ycor())
        # self.segments[0].setx(self.segments[0].xcor() + 20)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
