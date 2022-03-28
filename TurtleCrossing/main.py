import time
from turtle import Screen
from player import FINISH_LINE_Y, STARTING_POSITION, Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")
carmanager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_cars()
    carmanager.move_cars()

    #collision
    for car in carmanager.car_list:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    #crossing
    if player.ycor() > FINISH_LINE_Y:
        player.goto(STARTING_POSITION)
        carmanager.levelup()
        scoreboard.increse_level()

screen.exitonclick()