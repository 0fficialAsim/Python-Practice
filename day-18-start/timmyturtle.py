from turtle import Turtle, Screen
import random


screen = Screen()
screen.colormode(255)
timmy_turtle = Turtle()
timmy_turtle.shape("turtle")
timmy_turtle.color("purple") 

timmy_turtle.speed(1)
def reset():
    timmy_turtle.home()
    timmy_turtle.clear()
#SQUARE
"""
for turn in range(4):
    timmy_turtle.forward(100)
    timmy_turtle.right(90)
"""


#DASHED LINE 
"""
for lines in range(20):
    timmy_turtle.forward(10)
    timmy_turtle.pu()
    timmy_turtle.forward(10)
    timmy_turtle.pd()
"""

#Shapes

def move_forward():
    timmy_turtle.forward(100)
def change_angle(sides:int):
    timmy_turtle.right(360/sides)

num_of_sides = 2  
for shape in range(10):
    num_of_sides+=1
    timmy_turtle.pencolor(random.randint(0,255),random.randint(0,255), random.randint(0,255) )
    timmy_turtle.speed(num_of_sides)
    for line in range(num_of_sides): 
        move_forward()
        change_angle(num_of_sides) 


#Random walk 
reset()
timmy_turtle.pensize(8)
timmy_turtle.speed(0)
directions = [0, 90, 180, 270]

for walk in range(200):
    timmy_turtle.pencolor(random.randint(0,255),random.randint(0,255), random.randint(0,255))
    timmy_turtle.setheading(random.choice(directions))
    timmy_turtle.forward(30)

reset()

def draw_donut(gap_size):
    timmy_turtle.pensize(2)
    timmy_turtle.speed(9)
#Drawing a Donut 
    for _ in range( int(360 / gap_size) ):
        timmy_turtle.circle(100)
        timmy_turtle.pencolor(random.randint(0,255),random.randint(0,255), random.randint(0,255))
        adjust = timmy_turtle.heading() + gap_size
        timmy_turtle.setheading(adjust)
 
 
draw_donut(5)
  














screen.exitonclick() 