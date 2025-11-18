# Day 16: Coffee Machine in Object-Oriented Programming

This project refactors the procedural code from Day 15's Coffee Machine into an Object-Oriented Programming (OOP) structure.

## Project Structure

The project is broken down into several classes, each with its own responsibilities:

*   **`MenuItem`**: Models each drink on the menu (e.g., latte, espresso), containing its name, cost, and required ingredients.
*   **`Menu`**: Manages the collection of `MenuItem` objects. It can provide a list of available drinks and find a specific drink by name.
*   **`CoffeeMaker`**: Manages the machine's resources (water, milk, coffee). It can report the resource levels, check if there are enough resources to make a drink, and deduct the resources when a coffee is made.
*   **`MoneyMachine`**: Handles all monetary transactions. It processes coins, checks if the payment is sufficient, provides change, and keeps track of the profit.
*   **`Day_16.py`**: This is the main entry point of the application. It creates objects from the other classes and orchestrates the overall workflow of the coffee machine.

## How it Works

1.  The main script initializes `CoffeeMaker`, `Menu`, and `MoneyMachine` objects.
2.  It enters a loop to continuously prompt the user for their choice of coffee.
3.  The user can also enter "report" to get the current resource and profit status, or "off" to exit the program.
4.  If a drink is chosen, the program checks if there are sufficient resources.
5.  If resources are sufficient, it processes the payment.
6.  If payment is successful, the coffee is "made" (resources are deducted), and the user receives their drink.

This OOP approach makes the code more organized, reusable, and easier to maintain compared to the previous procedural version.
