# Day 22: Building the Pong Game

## Project: The Classic Pong Game

This project is a complete implementation of Pong, the classic two-player arcade game. The game features two paddles, controlled by the players, and a ball that bounces between them. The objective is to score points by getting the ball past your opponent's paddle.

The game is built using an Object-Oriented approach, with separate classes for the ball, the paddles, and the scoreboard. This modular design makes the code clean, organized, and easy to manage.

## Key Concepts Practiced

This project reinforces the OOP principles learned in previous days, focusing on the interaction between different objects to create a cohesive application.

### 1. OOP and Class Interaction

The entire game is broken down into distinct objects that communicate with each other:
*   **`Paddle` Class**: Manages the creation and movement of a player's paddle. Two instances of this class are created.
*   **`Ball` Class**: Controls the ball's appearance, movement, and bouncing logic. It has methods to reverse its direction (`bounce_y`, `bounce_x`) and reset its position.
*   **`Scoreboard` Class**: Inherits from `Turtle` to handle the display of scores for both players. It has methods to update the score when a player scores a point.

In the main game loop, we call methods on these objects to make the game run (e.g., `ball.move()`, `scoreboard.l_point()`).

### 2. Game Logic and Collision Detection

The core of the game is the `while` loop in `main.py`, which handles animation and game logic:
*   **Movement and Animation**: The screen's tracer is turned off for manual updates, creating smooth animation as the ball and paddles move.
*   **Collision with Walls**: The ball's y-coordinate is checked to see if it has hit the top or bottom wall, triggering a bounce.
*   **Collision with Paddles**: The `distance()` method is used to detect if the ball is close to a paddle. An additional check on the x-coordinate ensures the bounce happens at the correct time.
*   **Detecting a Score**: The ball's x-coordinate is checked to see if it has gone past a paddle, which triggers a score update and resets the ball's position.
