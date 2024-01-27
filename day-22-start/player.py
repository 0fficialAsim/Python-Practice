from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.penup()
        self.shape("turtle")

    def move_fd(self):
        self.fd(MOVE_DISTANCE) 

    def reset(self):
        self.goto(STARTING_POSITION)