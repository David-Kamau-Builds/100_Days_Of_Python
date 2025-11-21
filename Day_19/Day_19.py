import random
import time
from turtle import Turtle, Screen



COLORS = ["Red", "Blue", "Green", "Yellow", "Purple", "Black"]
START_Y = [120, 70, 20, -30, -80, -130]
MOVE_OPTIONS = [5, 10, 15, 20, 25, 30, 35]
FINISH_LINE_X = -350


screen = Screen()
screen.title("Turtle Race!")
screen.setup(width=900, height=600)
screen.tracer(0)


text_writer = Turtle()
text_writer.hideturtle()
text_writer.penup()


def create_racers():
    turtles = []
    for color, y in zip(COLORS, START_Y):
        t = Turtle("turtle")
        t.penup()
        t.color(color)
        t.setheading(180)
        t.goto(440, y)
        turtles.append(t)
    return turtles

racers = create_racers()


def countdown():
    text_writer.goto(0, 200)
    for n in ["3", "2", "1", "GO!"]:
        text_writer.clear()
        text_writer.write(n, align="center", font=("Arial", 40, "bold"))
        screen.update()
        time.sleep(1)
    text_writer.clear()


race_running = False
user_bet = ""

def move_turtle(t):
    global race_running
    if not race_running:
        return

    t.forward(random.choice(MOVE_OPTIONS))
    screen.update()

    if t.xcor() < FINISH_LINE_X:
        race_running = False
        announce_winner(t)
        return

    screen.ontimer(lambda: move_turtle(t), 100)


def announce_winner(winner):
    winner_color = winner.color()[0]
    text_writer.goto(0, 0)
    text_writer.clear()

    if user_bet.lower() == winner_color.lower():
        msg = f"{winner_color} turtle wins.  You guessed right!"
    else:
        msg = f"{winner_color} turtle wins.  Your guess was {user_bet}."

    text_writer.write(msg, align="center", font=("Arial", 28, "bold"))


def get_bet():
    while True:
        bet = screen.textinput("Place your bet",
                               "Which turtle wins? (Red/Blue/Green/Yellow/Purple/Black): ")
        if bet and bet.capitalize() in COLORS:
            return bet.capitalize()


def start_race():
    global race_running, user_bet
    user_bet = get_bet()
    countdown()
    race_running = True
    for t in racers:
        move_turtle(t)


screen.listen()

start_race()
screen.exitonclick()
screen.mainloop()