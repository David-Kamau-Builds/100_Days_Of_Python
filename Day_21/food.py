import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh(None)

    def refresh(self, snake_segments):
        while True:
            random_x_axis = random.randint(-280, 280)
            random_y_axis = random.randint(-280, 280)
            self.goto(random_x_axis, random_y_axis)

            if snake_segments is None:
                break

            is_on_snake = any(self.distance(segment) < 15 for segment in snake_segments)
            if not is_on_snake:
                break