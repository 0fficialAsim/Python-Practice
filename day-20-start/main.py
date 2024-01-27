from turtle import Screen 
from snake import Snake
from food import Food
import time 
from scoreboard import Scoreboard

#Screen Setup
window = Screen()
window.setup(width=600, height=600) #Keyword arguments 
window.bgcolor("black")
window.title("Snake Game")
window.tracer(0)
window.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

window.onkey(snake.move_up, "Up")
window.onkey(snake.move_dn, "Down")
window.onkey(snake.move_left, "Left")
window.onkey(snake.move_right,"Right")



#Updating current position of the snake
game_is_on = True
while(game_is_on):
    window.update()
    time.sleep(.1)
    snake.move()


    #Detect Collision w/Food
    if(snake.head.distance(food) <= 15):
       snake.add_seg()
       food.spawn()
       scoreboard.update()
       snake.head.color("green")

    #Detect Collision w/Wall
    if(snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 ):
        scoreboard.game_over()
        game_is_on = False

    #Detect Colition with tail
    for segment in snake.segments:
        if(segment == snake.head):
            pass
        elif(snake.head.distance(segment) < 10 ):
            game_is_on = False




window.exitonclick()

