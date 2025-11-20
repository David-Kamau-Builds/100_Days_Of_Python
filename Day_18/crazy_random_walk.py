import random
from turtle import Turtle, Screen, colormode

colormode(255)

t = Turtle()
t.width(8)
t.speed(10)

for _ in range(200):
    t.color(random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255))

    t.right(random.randint(0, 360))
    t.forward(30)

Screen().exitonclick()