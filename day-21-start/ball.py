from turtle import Turtle
touch_edge = False
TOP = 300
BOTTOM = -300
class Ball(Turtle): 
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.xmove = 10 
        self.ymove = 10 
        self.time_speed = .1
    def move(self):
        x = self.xcor() + self.xmove
        y  = self.ycor() + self.ymove
        self.goto(x,y)

    def y_bounce(self):
        self.ymove *= -1 
    
    def x_bounce(self):
        self.xmove *= -1
        self.time_speed *= .9
    def reset(self):
        self.goto(0,0)
        self.xmove*= -1
        self.time_speed =.1
    
    def increase_speed(self):
        new_speed = self.speed() + 1
        self.speed(new_speed )