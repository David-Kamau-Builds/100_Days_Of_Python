# Day 18 - Turtle & GUI Programming

## Overview
Day 18 of the 100 Days of Python challenge dives into GUI programming using Python's built-in `turtle` module. This day's projects focus on creating graphical art, from simple shapes to complex, randomized patterns. The culmination is a replica of a Damien Hirst "spot painting," which involves extracting colors from an image and using the turtle to place dots on a canvas.

## Setup & Installation
This project requires an external library, `colorgram.py`, to extract colors from an image. You can install it using pip:
```bash
pip install colorgram.py
```

## Project Features & Mini-Projects
- **Basic Shapes**: Scripts to draw simple geometric shapes like squares and dashed lines (`my_turtle.py`).
- **Overlapping Polygons**: A script that draws a series of polygons (from a triangle to a decagon) with random colors (`shape.py`).
- **Random Walk**: Two scripts that make the turtle move in a random direction for a set number of steps, creating abstract line art. One uses random RGB colors (`random_walk.py`, `crazy_random_walk.py`).
- **Spirograph**: A program that draws a complex spirograph pattern by repeatedly drawing circles at a slight angle to each other (`my_spirograph.py`).
- **Color Extraction**: A helper script (`color_extract.py`) that uses the `colorgram` library to extract a palette of colors from a JPG image (`image.jpg`).
- **Hirst Spot Painting**: The main project (`main.py`) that uses the extracted color palette to generate a 10x10 grid of colored dots, mimicking a Damien Hirst painting.

## Key Concepts
- **Turtle Graphics**: Using the `Turtle` and `Screen` classes to create a canvas and draw on it.
  - **Turtle State**: Controlling the turtle's position, heading, color, pen size, and speed.
  - **Movement**: Using methods like `forward()`, `right()`, `left()`, `setheading()`.
  - **Drawing Control**: Using `penup()`, `pendown()`, and `dot()` to control drawing.
- **GUI Programming**: Creating a graphical window that stays open until the user clicks to exit (`Screen().exitonclick()`).
- **Tuples**: Using tuples to represent RGB color data (e.g., `(255, 0, 0)`).
- **Modules**: Importing and using Python's built-in `random` module and the external `colorgram` library.
- **Color Modes**: Switching the turtle's color mode to accept RGB values from 0-255 using `colormode(255)`.
- **Code Organization**: Breaking down the day's work into multiple, single-purpose scripts.

## Tasks
- [x] Draw a square and a dashed line using the turtle.
- [x] Create a script to draw multiple polygons with random colors.
- [x] Implement a "random walk" with random directions and colors.
- [x] Generate a spirograph pattern with changing colors.
- [x] Write a script to extract a color palette from an image file using `colorgram`.
- [x] Use the extracted colors to create a 10x10 Hirst-style spot painting.
- [x] Structure the final painting logic to draw dots in an evenly spaced grid.

## Project Structure
- `main.py`: Main script for the Hirst spot painting.
- `color_extract.py`: Utility script to get colors from an image.
- `my_turtle.py`: Basic turtle drawing exercises.
- `shape.py`: Draws various geometric shapes.
- `random_walk.py`: Implements a random walk with cardinal directions.
- `crazy_random_walk.py`: Implements a random walk with 360-degree freedom.
- `my_spirograph.py`: Draws a circular spirograph pattern.
- `image.jpg`: The source image for color extraction.

## Notes
- The use of `colormode(255)` is essential for working with the RGB tuples extracted by `colorgram`.
- The Hirst painting script demonstrates how to programmatically create a structured layout, moving the turtle to the start of each new row.
- This day serves as a great introduction to the concepts of procedural art generation and working with graphical libraries in Python.