from turtle import Turtle
import random
import time 
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.traffic = []
        self.carSpeed = STARTING_MOVE_DISTANCE
        self.currLevel = 0 
       
    
    def spawn_traffic(self):
            
            chance = random.randint(1,6)
            if(chance == 1):
                car = Turtle()
                rand_x = random.randint(300 ,600)
                rand_y = random.randint(-240, 300)
                car.penup()
                car.shape("square")
                car.shapesize(stretch_wid= 1 ,stretch_len= 2)
                car.color(random.choice(COLORS))
                car.goto(300, rand_y)
                car.setheading(180)
                self.traffic.append(car)
            '''
            count = 0
            while(count != 100):
            #time.sleep(.3)
                chance = random.randint(1,6)
                rand_x = random.randint(300 ,600)
                rand_y = random.randint(-260, 300)
                if(chance <= 2):
                    car = Turtle()
                    car.penup()
                    car.shape("square")
                    car.shapesize(stretch_wid= 1 ,stretch_len= 2)
                    car.color(random.choice(COLORS))
                    car.goto(rand_x, rand_y)
                    car.setheading(180)
                    self.traffic.append(car)
                count += 1
                '''
            
        

    def move_traffic(self, level:int, player):
        if(level > self.currLevel):
            self.carSpeed += MOVE_INCREMENT
            self.currLevel += 1

        for car in self.traffic:
            car.fd(self.carSpeed)
            if(car.distance(player) <= 25):
                 return True 
        
            '''
            if(car.xcor() <= -310):
                rand_x = random.randint(300,500)
                rand_y = random.randint(-260, 300)
                car.goto(300, rand_y)
            '''
            
        