from turtle import Turtle, Screen

crush_the_turtle = Turtle()
crush_the_turtle.shape("turtle")
crush_the_turtle.color("#f22424")


for turtle in range(4):
    crush_the_turtle.forward(100)
    crush_the_turtle.right(90)


crush_the_turtle.left(90)


for turtle in range(15):
    crush_the_turtle.forward(10)
    crush_the_turtle.penup()
    crush_the_turtle.forward(10)
    crush_the_turtle.pendown()


my_screen = Screen()
my_screen.exitonclick()