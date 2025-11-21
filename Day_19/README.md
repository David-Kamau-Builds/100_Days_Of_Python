# Day 19: Turtle Race & Event Listeners

## Project: Turtle Race Game

This project creates a fun, interactive turtle racing game using Python's `turtle` module. Multiple turtles of different colors race from the right side of the screen to the left. Before the race starts, the user is prompted to place a bet on which turtle they think will win.

The race begins with a countdown, and then the turtles move forward at random speeds. The first turtle to cross the finish line is declared the winner. A message then appears, informing the user if their bet was correct.

## Key Concepts Practiced

This project reinforces and builds upon concepts from previous days, particularly Object-Oriented Programming (OOP) and the `turtle` graphics library.

### 1. State Management

We use a global boolean variable, `race_running`, to control the state of the application. The turtles only move if this variable is `True`. When a turtle crosses the finish line, this variable is set to `False` to stop the race for all turtles.

### 2. Multiple Object Instances

Building on OOP principles, we create multiple `Turtle` instances, each with its own color and starting position. These instances are stored in a list, making it easy to manage and move each turtle.

### 3. Higher-Order Functions & Event Listeners

A core focus of this project is handling user input and events:

*   **`screen.textinput()`**: Used to get the user's bet via a popup dialog box.
*   **`screen.ontimer()`**: This is a higher-order function used to create a game loop. It calls the `move_turtle` function repeatedly for each turtle after a short delay, which animates the race without freezing the program. This is a more advanced way to handle animation compared to a simple `while` loop.

By combining these concepts, we've created a more complex and interactive graphical application than in previous lessons.