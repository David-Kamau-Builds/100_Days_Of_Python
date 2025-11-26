import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("blue")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x_axis = random.randint(-280, 280)
        random_y_axis = random.randint(-280, 260)
        self.goto(random_x_axis, random_y_axis)