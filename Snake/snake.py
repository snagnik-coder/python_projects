from turtle import Turtle

DISTANCE = 20

class Snake:
    def __init__(self):
        self.snake_blocks = []
        for i in range(3):
            t = Turtle("square")
            t.penup()
            t.color("white")
            t.backward(20 * i)
            self.snake_blocks.append(t)
    
    def move(self):
        for num in range(len(self.snake_blocks) - 1, 0, -1):
            new_x = self.snake_blocks[num - 1].xcor()
            new_y = self.snake_blocks[num - 1].ycor()
            self.snake_blocks[num].goto(new_x, new_y)
        self.snake_blocks[0].forward(DISTANCE)

    def up(self):
        if self.snake_blocks[0].heading() != 270:
            self.snake_blocks[0].setheading(90)

    def down(self):
        if self.snake_blocks[0].heading() != 90:
            self.snake_blocks[0].setheading(270)

    def left(self):
        if self.snake_blocks[0].heading() != 0:
            self.snake_blocks[0].setheading(180)
    
    def right(self):
        if self.snake_blocks[0].heading() != 180:
            self.snake_blocks[0].setheading(0)

    def add_segment(self, position):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.snake_blocks.append(new_seg)

    def extend(self):
        self.add_segment(self.snake_blocks[-1].position())
