import turtle
import colorgram, random
from turtle import Screen, Turtle, colormode
rgb_colors = []
colors = colorgram.extract('a.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))
squirtle = Turtle()
colormode(255)
squirtle.penup()
squirtle.speed("fastest")
squirtle.hideturtle()
squirtle.setheading(225)
squirtle.forward(300)
squirtle.setheading(0)
for i in range(10):
    for _ in range(10):
        squirtle.dot(20, random.choice(rgb_colors))
        squirtle.penup()
        squirtle.forward(50)
    squirtle.left(90)
    squirtle.forward(50)
    squirtle.left(90)
    squirtle.forward(500)
    squirtle.left(180)
screen = Screen()
screen.exitonclick()