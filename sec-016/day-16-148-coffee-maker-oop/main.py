from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
menu = Menu()
mm = MoneyMachine()

done = False

while not done:
    choice = input(f"What would you like ({menu.get_items()})? ")
    if choice == "off":
        done = True
    elif choice == "report":
        cm.report()
    elif choice in menu.get_items():
        drink = menu.find_drink(choice)
        # does machine have enough resources for the drink requested?
        if cm.is_resource_sufficient(drink):
            if mm.make_payment(drink.cost):
                cm.make_coffee(drink)
    else:
        print("Invalid item selected.  Try again.")