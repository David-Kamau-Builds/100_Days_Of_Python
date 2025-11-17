import art

print(art.logo)

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report():
    print("\n--- MACHINE REPORT ---")
    print(f"Water:  {resources['water']}ml")
    print(f"Milk:   {resources.get('milk', 0)}ml")
    print(f"Coffee: {resources['coffee']}g\n")


def process_coins():
    print("Please insert coins.")
    pennies = int(input("How many pennies (1¢)? "))
    nickels = int(input("How many nickels (5¢)? "))
    dimes = int(input("How many dimes (10¢)? "))
    quarters = int(input("How many quarters (25¢)? "))

    total = (
        pennies * 0.01
        + nickels * 0.05
        + dimes * 0.10
        + quarters * 0.25
    )
    return round(total, 2)


def check_resources(drink):
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources.get(item, 0):
            print(f"Sorry, not enough {item}.")
            return False
    return True


def make_coffee(drink):
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Enjoy your {drink}. ☕️")

machine_on = True

while machine_on:

    user_input = input(
        "\nWhat would you like? (espresso/latte/cappuccino)\n"
        "Type 'report' for resources or 'off' to shut down:\n> "
    ).lower()

    if user_input == "off":
        password = input("Enter shutdown password: ")
        if password == "bean os":
            print("Shutting down... Goodbye 👋")
            machine_on = False
        else:
            print("Incorrect password. Machine stays on. 🟢")
        continue

    if user_input == "report":
        print_report()
        continue

    if user_input not in MENU:
        print("Invalid selection. Please try again. 🚫")
        continue

    drink = user_input
    drink_cost = MENU[drink]["cost"]

    if not check_resources(drink):
        continue

    print(f"{drink.title()} costs ${drink_cost}.")
    total_paid = process_coins()
    print(f"You inserted: ${total_paid}")

    if total_paid < drink_cost:
        print(f"Insufficient funds. ${drink_cost - total_paid} short. Money refunded.")
        continue
    elif total_paid > drink_cost:
        change = round(total_paid - drink_cost, 2)
        print(f"Here is your change: ${change}")

    make_coffee(drink)