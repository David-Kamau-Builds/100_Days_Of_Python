import time
from turtle import Turtle, Screen
from car_manager import  CarManager
from player import Player
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)


player = Player()
cars = CarManager()
scores = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()

    cars.move_cars()

    # Detect collision with a car
    for car in cars.cars:
        if car.distance(player) < 28:
            game_is_on = False
            scores.game_over()

    # Detect successful crossing
    if player.ycor() > 250:
        scores.add_score()
        player.finish_line()
        cars.level_up()


screen.exitonclick()