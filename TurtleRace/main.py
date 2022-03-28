from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height = 400)
choice = screen.textinput(title = "Make your bet", prompt = "Which color turtle will win the race?")
color_palette = ["purple", "blue", "green", "yellow", "orange", "red"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtle_list = []
winner_turtle = ""

for turtle_index in range(len(color_palette)):
    t = Turtle(shape = "turtle")
    t.color(color_palette[turtle_index])
    t.penup()
    t.goto(x = -230, y = y_positions[turtle_index])
    turtle_list.append(t)

race_on = False

if choice:
    race_on = True

while race_on:
    for t in turtle_list:
        if t.xcor() > 230:
            winner_turtle = t.pencolor()
            race_on = False
        distance = random.randint(0, 10)
        t.forward(distance)

if winner_turtle == choice.lower():
    print(f"Congrats. Your guess is correct. The {winner_turtle} turtle won.")
else:
    print(f"Oops! The {winner_turtle} turtle won.")

screen.exitonclick()