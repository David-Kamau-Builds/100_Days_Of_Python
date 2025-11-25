# Day 23: The Turtle Crossing Game

## Project: Turtle Crossing Capstone Project

This project is a capstone challenge that brings together all the Object-Oriented Programming concepts learned so far. The game, similar to the classic "Frogger," involves a player (a turtle) trying to cross a busy road filled with randomly generated, moving cars.

The player moves forward with the "Up" arrow key. If the player is hit by a car, the game is over. If the player successfully reaches the other side, they level up, and the cars begin to move faster, increasing the difficulty.

## Key Concepts Practiced

This project is a comprehensive exercise in OOP design, focusing on the separation of concerns and the interaction between multiple custom classes.

### 1. OOP Design with Separated Concerns

The application is broken down into three distinct classes, each with a single responsibility:
*   **`Player` Class**: Manages the turtle that the user controls. It handles the starting position, the forward movement, and the logic for detecting when it has reached the finish line.
*   **`CarManager` Class**: Responsible for creating, managing, and moving all the car objects. It randomly generates new cars and contains the logic for increasing their speed when the player levels up.
*   **`Scoreboard` Class**: Handles the display of the current level. It updates the score on the screen and shows the "GAME OVER" message.

### 2. Dynamic Difficulty Scaling

A key feature of this game is that it gets progressively harder. When the player successfully crosses the screen, the `CarManager`'s `level_up()` method is called. This method increases the `move_increment` for all cars, making the game more challenging with each new level.

### 3. Collision Detection with Multiple Objects

The main game loop iterates through a list of all active car objects (`cars.cars`) and uses the `distance()` method to check if the player has collided with any of them. This demonstrates how to handle collision detection against a group of objects rather than just a single one.