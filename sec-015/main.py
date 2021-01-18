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

#prompt what would you like? - espresso, latte, capucino, off, report
#off - ends program
#report - shows status of resources
#check-resources() - verify enough resources for order
#process-coing() = if sufficient resources, propmt user for coins & calculate the value
#transaction_successful?  Check that user has enough coins to purchase their drink
#-- if yes, then add $$ to machine as profit and resources reduced accordingly
#-- if yes and too much money, return change
#-- if no, say 'not enough $$' and return coins
