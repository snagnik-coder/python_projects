from turtle import Screen
import time
from scoreboard import Scoreboard
from food import Food
from snake import Snake

screen = Screen()
screen.setup(width = 600, height = 600)
screen.title("Snake")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #collision
    if snake.snake_blocks[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()
    
    #collision with wall
    if snake.snake_blocks[0].xcor() < -280 or snake.snake_blocks[0].xcor() > 280 or snake.snake_blocks[0].ycor() < -280 or snake.snake_blocks[0].ycor() > 280:
        game_on = False
        if scoreboard.high_score < scoreboard.score:
            scoreboard.high_score = scoreboard.score
        scoreboard.score = 0
        scoreboard.gameover()

    for seg in snake.snake_blocks[1:]:
        if snake.snake_blocks[0].distance(seg) < 10:
            game_on = False
            scoreboard.gameover()
screen.exitonclick()