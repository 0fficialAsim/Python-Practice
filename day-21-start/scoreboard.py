from turtle import  Turtle
FONT = ( "Verdana", 30, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.leftScore = 0
        self.rightScore = 0 
        self.ht()
        self.pu()
        self.color("white") 
        self.goto(100,250)  
        self.write(str(self.rightScore),  align=ALIGNMENT, font=FONT) 
        self.goto(-100,250)
        self.write(str(self.rightScore),  align=ALIGNMENT, font=FONT)


    def increase_right(self):
        self.clear()
        self.rightScore +=1
        self.goto(100,250)  
        self.write(str(self.rightScore),  align=ALIGNMENT, font=FONT) 
        self.goto(-100,250)  
        self.write(str(self.leftScore),  align=ALIGNMENT, font=FONT) 


    def increase_left(self):
        self.clear()
        self.leftScore +=1 
        self.goto(-100,250)  
        self.write(str(self.leftScore),  align=ALIGNMENT, font=FONT) 
        self.goto(100,250)  
        self.write(str(self.rightScore),  align=ALIGNMENT, font=FONT) 


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER ", align= ALIGNMENT, font=FONT)