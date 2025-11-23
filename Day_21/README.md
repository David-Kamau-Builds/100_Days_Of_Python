# Day 21: Building the Snake Game (Part 2)

## Project: Snake Game - Collision Detection, Scoring, and Inheritance

This project completes the core mechanics of the classic Snake game. Building on the foundation from Day 20, this part introduces food, a scoreboard, and the logic to detect collisions. The game is now fully playable: the snake grows when it eats, the score increases, and the game ends if the snake hits a wall or itself.

## Key Concepts Practiced

This project deepens the use of Object-Oriented Programming, focusing on class inheritance and the interaction between different objects.

### 1. Class Inheritance

The `Food` and `Scoreboard` classes inherit from the `Turtle` class. This is a powerful OOP concept that allows our custom classes to gain all the attributes and methods of the parent `Turtle` class (like `shape()`, `color()`, `goto()`), while also allowing us to add specialized methods (`refresh()`, `increase()`).

### 2. Collision Detection

The game loop now includes logic to check for different types of collisions:
*   **Collision with Food**: We use the `distance()` method to check if the snake's head is close to the food. If so, the food moves to a new random location, the score is increased, and the snake grows longer.
*   **Collision with Wall**: We check if the snake's head has moved beyond the boundaries of the screen.
*   **Collision with Tail**: We iterate through the snake's own segments to see if the head has collided with any part of its body.

If a wall or tail collision occurs, the game loop stops, and a "GAME OVER" message is displayed.

### 3. Slicing in Python

When checking for collision with the tail, we use list slicing (`snake.segments[1:]`) to create a new list containing all segments of the snake *except* for the head. This is an elegant way to avoid having the snake's head immediately collide with itself.