from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Aria", 16, "normal")

STARTING_POSITION= (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 250

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.setposition(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def finish_line(self):
        self.setposition(STARTING_POSITION)
