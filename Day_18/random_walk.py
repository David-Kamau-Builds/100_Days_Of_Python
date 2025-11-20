from turtle import Turtle, Screen
import random

direction = [0, 90, 180, 270]

random_walk = Turtle()
random_walk.width(10)
random_walk.speed(10)

for _ in range(200):
    r = random.random()
    g = random.random()
    b = random.random()
    random_walk.color(r, g, b)
    random_walk.forward(30)
    random_walk.setheading(random.choice(direction))

screen_exit = Screen()
screen_exit.exitonclick()