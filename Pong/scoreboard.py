from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score_l = 0
        self.score_r = 0
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_l, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.score_r, align="center", font=("Courier", 50, "normal"))