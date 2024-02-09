from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_running = True

while is_running:
    options = menu.get_items()
    user_input = input(f"What would you like? ({options}): ")
    if user_input == "off":
        is_running = False

    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(user_input)
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)