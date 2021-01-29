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

    # instructor's solution was WAY easier!!!
    def append_seg(self):
        # add segment to snake
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        # position the new new segment at end of the snake
        # detect direction of last segment and add new one behind
        last_idx = len(self.segments) - 1
        last_seg = self.segments[last_idx]
        # get position of last_seg
        seg_x = last_seg.xcor()
        seg_y = last_seg.ycor()
        if last_seg.heading() == LEFT:
            # add new segment to right
            # get position of last segment and add 20 to x
            seg_x = seg_x + 20
        elif last_seg.heading() == RIGHT:
            # add new segment to left
            # get position of last segment and subtract 20 from x
            seg_x = seg_x - 20
        elif last_seg.heading() == UP:
            # add new segment below
            # get position of last segment and subtract 20 from y
            seg_y = seg_y - 20
        elif last_seg.heading() == DOWN:
            # add new segment above
            # get position of last segment and add 20 to y
            seg_y = seg_y + 20
        new_segment.setx(seg_x)
        new_segment.sety(seg_y)
        self.segments.append(new_segment)
