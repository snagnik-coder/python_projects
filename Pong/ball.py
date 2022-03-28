from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.yconst = 10
        self.xconst = 10
        self.level = 0.1

    def move(self):
        if self.ycor() >= 280 or self.ycor() <= -280:
           self.yconst = -self.yconst
           self.level *= 0.9
        x_new = self.xcor() + self.xconst
        y_new = self.ycor() + self.yconst
        self.goto(x_new, y_new)

    def res_pos(self):
        self.goto(0, 0)
        self.level = 0.1
        self.xconst = -self.xconst
