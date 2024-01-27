from turtle import Turtle
UP = 90
DOWN = 270 

class Paddle(Turtle):
    def __init__(self, position):
       super().__init__()
       self.shape("square")
       self.color("white")
       self.pu()
       self.shapesize(stretch_wid=5, stretch_len= 1)
       self.goto(position)
       self.speed(10)
 
    def move_up(self):
        if(self.ycor() !=300):
            new_y = self.ycor() + 10
            self.goto(self.xcor(), new_y)

    def move_dn(self):
        if(self.ycor() != -300):    
            new_y = self.ycor() - 10
            self.goto(self.xcor(), new_y)
