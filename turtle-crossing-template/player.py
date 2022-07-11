from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('brown')
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.setheading(90)
        self.forward(10)

    def down(self):
        self.setheading(-90)
        self.forward(10)

    def left(self):
        self.setheading(180)
        self.forward(10)

    def right(self):
        self.setheading(0)
        self.forward(10)

    def is_at_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)