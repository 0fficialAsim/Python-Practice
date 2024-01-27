"""
Ping Pong 

Classes:

Score Board:
-Keep score 

Ball:
= Sense when it hits the paddle and moves in direction
= When it reaches the border it gives the last player who touched it a point
= Resets in the middle 

Paddles:
= Ability to move up and down. 

Court ( aka the Screen)
-
"""

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
TOP = 280
BOTTOM = -280
window = Screen() 
window.setup(800, 600)
window.bgcolor("black")
window.title("Pong")
window.listen()
window.tracer(0)  # This method gets rid of the animation and shows frame by frame
                  # With using this methosd we will need to update the screen using a 
                  # while loop 

paddle_r  = Paddle((350,0))
paddle_l  = Paddle((-350, 0 ))
ball = Ball()
scoreboard = Scoreboard()

window.onkeypress(paddle_r.move_up, "Up")
window.onkeypress(paddle_r.move_dn, "Down")

window.onkeypress(paddle_l.move_up, "w")
window.onkeypress(paddle_l.move_dn, "s")
 
game_is_on = True
while(game_is_on):
    time.sleep(ball.time_speed)
    window.update()  #Updates the screen if any movements or new animations were added 
    ball.move()

    #Detect Collision with wall 
    if(ball.ycor() <= BOTTOM or ball.ycor() >= TOP):
        #bounce ball aka change direction.
       ball.y_bounce()

    #Detect Collison with right paddle
    if(ball.distance(paddle_r) < 50 and ball.xcor() > 340 or ball.distance(paddle_l) < 50 and ball.xcor() < -340):
        ball.x_bounce()
        ball.increase_speed()

    #Ball goes out of bounce. 
    if(ball.xcor() >= 370):
        scoreboard.increase_left()
        ball.reset()
        paddle_l.goto(-350, 0 )
        paddle_r.goto(350,0)

    if(ball.xcor() <= -380):
        scoreboard.increase_right()
        ball.reset()
        paddle_l.goto(-350, 0)
        paddle_r.goto(350,0)

    if(scoreboard.leftScore == 10 or scoreboard.rightScore == 10):
        scoreboard.game_over()
        game_is_on = False
        


window.exitonclick()