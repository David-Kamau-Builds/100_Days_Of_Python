from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    print(logo)
    user_choice = input(f"What type of coffee would you like? ({options}): ").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                