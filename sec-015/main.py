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


def check_resources(order):
    # check resources to verify enough for order
    current_order = MENU[order]
    if enough('water', order) and enough('milk', order) and enough('coffee', order):
        return True
    else:
        return False


def enough(ingredient, order):
    enough = True
    # check if we have enough, unless order doesn't call for the ingredient
    if ingredient in MENU[order]['ingredients']:
        if resources[ingredient] < MENU[order]['ingredients'][ingredient]:
            enough = False
    return enough

def resources_rpt():
    print("Resources Report:")
    print("=================")
    print(f"water: {resources.get('water')}")
    print(f"milk: {resources.get('milk')}")
    print(f"coffee: {resources.get('coffee')}")
    print(f"money: {money}")


def convert_coins_to_dollars(q, d, n, p):
    return q * .25 + d * .1 + n * .05 + p * .01


choice = ""
# amount of $$ in machine
money = 0
while not choice == "off":
    ingr = "water"
    if ingr in resources:
        print(f'Found {ingr}: {resources[ingr]}')
    else:
        print(f'{ingr} not found')
    # prompt what would you like? - espresso, latte, capucino, off, report
    choice = input("What would you like (espresso, latte, capucino)? ")
    if choice == "report":
        # print summary of resources
        resources_rpt()
    elif choice == "off":
        print("Turning off machine...  goodbye!")
    else:
        if check_resources(choice):
            # collect $$
            quarters = input("How many quarters? ")
            dimes = input("How many dimes? ")
            nickels = input("How many nickels? ")
            pennies = input("How many pennies? ")
            money_in = convert_coins_to_dollars(quarters, dimes, nickels, pennies)
            cost = MENU[choice]['cost']
            if money_in >= cost:
                print(f"Here is your {choice}.")
                # add cost to money
                money += cost
                # reduce resources by purchase
                for r in resources:
                    resources[r] -= MENU[choice][r]
                if money_in > cost:
                    # return change to customer
                    print(f"Here is your {money_in - cost} in change.")
            else:
                print(f'Not enough $$ for purchase of {choice}.  Returning you ${money_in}.')

    # off - ends program
    # report - shows status of resources
    # check-resources() - verify enough resources for order
    # process-coing() = if sufficient resources, propmt user for coins & calculate the value
    # transaction_successful?  Check that user has enough coins to purchase their drink
    # -- if yes, then add $$ to machine as profit and resources reduced accordingly
    # -- if yes and too much money, return change
    # -- if no, say 'not enough $$' and return coins
