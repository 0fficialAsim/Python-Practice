from turtle import Turtle
import pandas
FONT = ( "Verdana", 9, "normal")
ALIGNMENT = "center"

class StateTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.color("black")
        self.count = 0

    def write_StateName(self, position:tuple, name:str):
        self.count+= 1
        self.goto(position)
        self.write(arg=name,font=FONT,align=ALIGNMENT)
        