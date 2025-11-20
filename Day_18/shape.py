from turtle import Turtle, Screen
import random

my_turtle = Turtle()

my_turtle.left(180)

for sides in range(3, 11):
    angle = 360 / sides
    r = random.random()
    g = random.random()
    b = random.random()
    my_turtle.color(r, g, b)

    for _ in range(sides):
        my_turtle.forward(50)
        my_turtle.right(angle)

screen = Screen()
screen.exitonclick()
