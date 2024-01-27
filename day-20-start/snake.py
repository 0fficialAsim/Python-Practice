from turtle import Turtle
STARTING_POSITIONS= [(0, 0 ) , (-20, 0) , (-40,0)]
UP = 90
DOWN = 270 
LEFT = 180
RIGHT = 0 
class Snake:
    def __init__(self) -> None:
       self.segments = []
       self.create_snake()
       self.head = self.segments[0]
       

    def create_snake(self): 
        for pos in STARTING_POSITIONS:
            body_part = Turtle()
            body_part.penup()
            body_part.shape("square")
            body_part.color("white")
            body_part.setpos(pos)
            self.segments.append(body_part)
   
    def add_seg(self):
        curr_end = self.segments[len(self.segments) - 1]
        new_end = Turtle()
        new_end.color("white")
        new_end.shape("square")
        new_end.pu()
      
        self.segments.append(new_end)
        new_end.goto(curr_end.position())
        

        """
       x = curr_end.xcor()
        y = curr_end.ycor() 
        if(curr_end.heading() == RIGHT  ):
            new_end.goto(x - 20 , y)
            self.segments.append(new_end)
        elif(curr_end.heading() == LEFT):
            new_end.goto(x + 20 , y)
            self.segments.append(new_end)
        elif(curr_end.heading() == UP):
            new_end.goto(x  , y - 20 )
            self.segments.append(new_end)
        elif(curr_end.heading() == DOWN):
            new_end.goto(x  , y + 20 )
            self.segments.append(new_end)
       """ 
        

    def move_up(self):
        if(self.segments[0].heading() != DOWN):
             self.segments[0].setheading(UP)
     
    def move_dn(self):
       if(self.segments[0].heading() != UP):
             self.segments[0].setheading(DOWN)

    def move_left(self):
       if(self.segments[0].heading() != RIGHT):
             self.segments[0].setheading(LEFT)


    def move_right(self):
        if(self.segments[0].heading() != LEFT):
             self.segments[0].setheading(RIGHT)

    
    def move(self):
         for seg_num in range( len(self.segments) - 1 , 0 , -1):
            new_x = self.segments[seg_num - 1].xcor() 
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
         self.head.fd(20)
         self.head.color("white")


