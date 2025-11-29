# Day 27: Tkinter, *args, **kwargs and Creating GUI Programs

## Project: Mile to Km Converter

This project introduces graphical user interfaces (GUIs) by building a simple utility application. The program provides a window with an input field for miles, which it then converts to kilometers upon a button click, displaying the result on the screen.

## Key Concepts Practiced

This day was an introduction to creating desktop applications with Python's built-in `tkinter` library and understanding more advanced Python function arguments.

### 1. Tkinter GUI

We learned the basics of creating a graphical user interface.
*   **Window and Labels**: How to create a `Tk` window and display text using `Label` widgets.
*   **Buttons and Entry**: How to capture user interaction with `Button` widgets and get user input with `Entry` (input box) widgets.
*   **Layout Management**: We used the `grid()` geometry manager to position widgets in a structured row and column format. [1, 11] The `padx` and `pady` arguments were used to add spacing around widgets for a cleaner layout. Other layout managers in Tkinter are `pack()` and `place()`. [4, 6]

### 2. Advanced Python Arguments: `*args` and `**kwargs`

We explored how to create functions that can accept a variable number of arguments.

*   `*args` **(Unlimited Positional Arguments)**: The special `*args` syntax in a function definition allows the function to accept any number of positional arguments. [2, 3] These arguments are collected into a tuple inside the function. [5, 12]

*   `**kwargs` **(Unlimited Keyword Arguments)**: The `**kwargs` syntax allows a function to accept any number of keyword arguments (e.g., `name="John"`). [7] These arguments are collected into a dictionary within the function. [5]
