from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
   def __init__(self):
        super().__init__()
        self.level = 0
        self.ht()
        self.penup()
        self.goto(-230,260)
        self.write( f"Level {self.level}", move=False, align= "center", font= FONT)

   def increase_level(self):
       self.clear()
       self.level += 1
       self.write( f"Level {self.level}", move=False, align= "center", font= FONT)
   
   def end_game(self):
       self.goto(0,0)
       self.write("GAME OVER ", align= "center", font=FONT)

   def beat_game(self):
       self.goto(0,0)
       self.write("ACCOMPLISHED!", align= "center", font=FONT)