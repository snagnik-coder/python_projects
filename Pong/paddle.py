from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()

    def go_up(self):
        y_new = self.ycor() + 20
        if y_new < 250:
            self.goto(self.xcor(), y_new)
    
    def go_down(self):
        y_new = self.ycor() - 20
        if y_new > -250:
            self.goto(self.xcor(), y_new)