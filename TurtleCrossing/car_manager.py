from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.car_list = []
        self.carspeed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        choice = random.randint(1, 6)
        if choice == 1:
            car_create = Turtle("square")
            car_create.shapesize(stretch_wid=1, stretch_len=2)
            car_create.penup()
            car_create.color(random.choice(COLORS))
            rand_y = random.randint(-250, 250)
            car_create.goto(300, rand_y)
            self.car_list.append(car_create)

    def move_cars(self):
        for car in self.car_list:
            car.backward(self.carspeed)

    def levelup(self):
        self.carspeed += MOVE_INCREMENT

