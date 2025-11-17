# Day 15 - Coffee Machine Simulator

## Overview
Day 15 of the 100 Days of Python challenge involves creating a coffee machine simulator. This program mimics the functionality of a real coffee machine, allowing users to order different types of coffee, process payments, and manage machine resources. The machine continues to operate until it is manually shut down.

## Machine Features
- **Menu Options**: Offers three coffee choices: espresso, latte, and cappuccino.
- **Resource Management**: Tracks the available water, milk, and coffee. It checks if there are enough ingredients before making a drink.
- **Coin-Operated**: Accepts payments in pennies, nickels, dimes, and quarters.
- **Transaction Processing**: Calculates the total money inserted and provides change if the user overpays. Refunds money if the payment is insufficient.
- **Admin Commands**:
  - `report`: Displays the current levels of all resources.
  - `off`: Shuts down the machine, protected by a simple password.
- **User Feedback**: Provides clear messages for successful orders, insufficient resources, and transaction outcomes.
- **Visuals**: Includes ASCII art for a branded logo.

## Key Concepts
- **Data Structures**: Utilizes dictionaries (`MENU`, `resources`) to manage complex data like drink recipes, costs, and ingredient stock.
- **Modular Functions**: The program is broken down into logical functions (`print_report`, `process_coins`, `check_resources`, `make_coffee`) for better organization and readability.
- **Global Scope**: The `resources` dictionary is treated as a global variable that is modified by various functions to reflect the machine's state.
- **Program Loop**: A `while` loop keeps the machine running, processing user commands until the `off` command is successfully executed.
- **Input Handling and Validation**: The program processes user input for drink choices and commands, with checks for invalid selections.
- **String Formatting**: F-strings are used to create dynamic and readable output for users, such as reports and transaction details.

## Tasks
- [x] Create data structures to store the menu (recipes and costs) and machine resources.
- [x] Implement a `print_report()` function to display current resource levels.
- [x] Implement a `check_resources()` function to verify if there are enough ingredients for a selected drink.
- [x] Implement a `process_coins()` function to handle monetary transactions and return the total amount paid.
- [x] Implement a `make_coffee()` function to deduct ingredients from the resources after a successful order.
- [x] Build the main program loop that prompts the user for input.
- [x] Handle user commands: `espresso`, `latte`, `cappuccino`, `report`, and `off`.
- [x] Process transactions by comparing the cost with the money paid and providing change or a refund.
- [x] Ensure the main loop terminates correctly when the `off` command is used with the correct password.
- [x] Integrate ASCII art for a better user experience.

## Project Structure
- `Day_15.py` — The main script containing all the logic for the coffee machine simulator.
- `art.py` — A module that stores the ASCII logo art.

## Notes
- The program uses a global `resources` dictionary, which is directly modified by the `make_coffee` function.
- The `off` command includes a simple password ("bean os") as a fun way to demonstrate conditional logic for administrative functions.
- The `check_resources` function uses `resources.get(item, 0)` to safely check for ingredients like 'milk', which might not be required for all drinks (e.g., espresso).
- Floating-point precision for currency is handled by rounding calculations to two decimal places.