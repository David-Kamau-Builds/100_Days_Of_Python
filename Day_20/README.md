# Day 20: Building the Snake Game (Part 1)

## Project: The Snake Game - Body & Movement

This project begins the creation of the classic Snake game. In this first part, the focus is on setting up the game screen, creating the initial snake body, and implementing the core movement logic. The snake is built to move forward continuously, and we add event listeners to allow the user to change its direction using the arrow keys.

## Key Concepts Practiced

This project heavily relies on Object-Oriented Programming and introduces more advanced control over the `turtle` screen for smoother animations.

### 1. Object-Oriented Design

A `Snake` class is created to manage all the segments of the snake's body. This class is responsible for creating the initial segments, adding new segments, and controlling the snake's movement. This encapsulates the snake's logic, making the main game file cleaner and easier to manage.

### 2. Animation and Screen Control

To create smooth, flicker-free animation, we turn off the automatic screen updates using `screen.tracer(0)`. The screen is then manually updated inside the game loop with `screen.update()`. This gives us precise control over when the screen is redrawn. A short delay is added with `time.sleep()` to control the speed of the game.

### 3. Event Handling for User Input

The `screen.listen()` method is used to make the program listen for keyboard inputs. The `screen.onkey()` function then binds specific methods (e.g., `snake.up()`, `snake.down()`) to the arrow keys, allowing the player to control the snake's direction in real-time.