import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
cars = CarManager()
player = Player()
screen.onkeypress(player.move_fd, "Up")



game_is_on = True
curr_level = scoreboard.level
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.spawn_traffic()
    if(player.ycor() >= 280):
        #score level increases, update time sleep to go faster 
        player.reset()
        scoreboard.increase_level()
        curr_level = scoreboard.level
    
    if(cars.move_traffic(curr_level, player) == True):
        scoreboard.end_game()
        game_is_on = False
    elif(curr_level == 10):
        scoreboard.beat_game()
        game_is_on = False   

screen.exitonclick()