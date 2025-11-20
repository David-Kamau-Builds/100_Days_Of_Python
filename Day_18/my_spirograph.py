from turtle import Turtle, colormode, Screen
import random

my_spiral = Turtle()
colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b

def my_circle(angle):
    for i in range(int(360/angle)):
        my_spiral.pensize(2)
        my_spiral.speed("fastest")
        my_spiral.color(random_color())
        my_spiral.circle(200)
        my_spiral.setheading(my_spiral.heading() + angle)

my_circle(3)

screen = Screen()
screen.exitonclick()