
from turtle import Turtle
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        pos = [0,-20,-40]
        for i in range(3):
            self.add_segment((0,pos[i]))

    def add_segment(self,pos):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.pu()
        new_turtle.goto(pos)
        self.segments.append(new_turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())



    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num  - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

