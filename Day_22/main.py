import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 200))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Bounce on ceiling/floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Bounce on paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 and ball.x_move > 0:
        ball.bounce_x()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -320 and ball.x_move < 0:
        ball.bounce_x()

    # Detect R scoring
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L scoring
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
