# Day 25: Working with CSV Data and the Pandas Library

## Project: U.S. States Guessing Game

This project is an interactive educational game that tests a user's knowledge of U.S. state geography. A map of the United States is displayed, and the user is prompted to enter the name of a state. If the guess is correct, the state's name is written onto its location on the map.

The game keeps track of correctly guessed states and continues until all 50 states are named. If the user exits early, the game generates a `states_to_learn.csv` file containing all the states they missed, so they can study them later.

## Key Concepts Practiced

This project introduces the **Pandas library**, a powerful tool for data analysis and manipulation in Python.

### 1. Reading CSV Data with Pandas

Instead of manually parsing CSV files, we use `pandas.read_csv()` to load the `50_states.csv` file directly into a **DataFrame**. This is a two-dimensional table-like data structure that is highly optimized for data analysis.

### 2. DataFrames and Series

We interact with the data using Pandas DataFrames and Series:
*   **Accessing a Column (Series)**: We get a list of all state names by accessing the `state` column: `data.state.to_list()`.
*   **Row Selection**: We find the data for a specific state using conditional selection: `data[data.state == answer_state]`. This returns a new DataFrame containing only the row(s) that match the condition.
*   **Accessing Cell Values**: To get the x and y coordinates for a state, we use `.item()` to extract the single value from a Series (e.g., `state_data.x.item()`).

### 3. Writing Data to a CSV File

The project demonstrates how to create a new CSV file from scratch. A list of missed states is converted into a Pandas DataFrame (`pandas.DataFrame(missing_states)`) and then easily saved to a new file using the `.to_csv()` method.

### 4. Integrating Pandas with Turtle

This project shows a practical application of using a data library to drive a GUI. The coordinates read by Pandas are used to tell the Turtle exactly where to write the state names on the screen, combining data processing with graphical output.
