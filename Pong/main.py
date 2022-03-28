from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width = 800, height = 600)
screen.tracer(0)

scoreboard = Scoreboard()
pad1 = Paddle()
pad1.goto(350, 0)
pad2 = Paddle()
pad2.goto(-350, 0)
ball = Ball()

screen.listen()
screen.onkey(pad1.go_up, "Up")
screen.onkey(pad1.go_down, "Down")
screen.onkey(pad2.go_up, "w")
screen.onkey(pad2.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.level)
    screen.update()
    ball.move()
    if ball.xcor() > 330 and ball.distance(pad1) < 50:
        ball.xconst = - ball.xconst
    elif ball.xcor() < -330 and ball.distance(pad2) < 50:
        ball.xconst = -ball.xconst
    elif ball.xcor() > 380:
        ball.res_pos()
        scoreboard.score_l += 1
        scoreboard.update_score()
    elif ball.xcor() < -380:
        ball.res_pos()
        scoreboard.score_r += 1
        scoreboard.update_score()
        
    

screen.exitonclick()