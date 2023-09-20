Coffee Machine Code
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

Money = 0


def process_coins():
    """Counts the coins and returns the total"""
    print("Please insert coins")
    quarters = int(input("How many quarters?"  ))
    dimes = int(input("How many dimes?"  ))
    nickles = int(input("How many nickles?"  ))
    pennies = int(input("How many pennies?"  ))
    total = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return total


def check_resources(drink, resources):
    """This function checks the resources are available in the coffee machine"""
    choice = MENU[drink]
    ingredients = choice["ingredients"]
    water_for_choice = int(ingredients["water"])
    milk_for_choice = int(ingredients["milk"])
    coffee_for_choice = int(ingredients["coffee"])
    water_resource = int(resources["water"])
    milk_resource = int(resources["milk"])
    coffee_resource = int(resources["coffee"])
    if water_for_choice >= water_resource:
        print("Sorry out of water")
        return False
    elif milk_for_choice >= milk_resource:
        print("Sorry out of milk")
        return False
    elif coffee_for_choice >= coffee_resource:
        print("sorry out of coffee")
        return False
    else:
        return "True"



def check_price(drink, total):
    """This function checks the price is correct"""
    global Money
    choice = MENU[drink]
    cost = choice["cost"]
    print(f"Cost of {drink} is ${cost} ")
    if total >= cost:
       total -= cost
       print(f" Here is your ${total} change. Money Refunded")
       return True
    else:
        total < cost
        print("Insufficient money. Money refunded")
        return False


def report(resources):
    """This function prints the report of the resources of the machine"""
    global Money
    for key, value in resources.items():
        print(f"{key} {value}")
    print(Money)

def make_coffee(drink, resources):
    """This function is used to deduct the resources according to the drink chosen by the user"""
    global Money
    choice = MENU[drink]
    ingredients = choice["ingredients"]
    water_for_choice = int(ingredients["water"])
    milk_for_choice = int(ingredients["milk"])
    coffee_for_choice = int(ingredients["coffee"])
    water_resource = int(resources["water"])
    milk_resource = int(resources["milk"])
    coffee_resource = int(resources["coffee"])
    new_water = water_resource - water_for_choice
    new_milk = milk_resource - milk_for_choice
    new_coffee = coffee_resource - coffee_for_choice
    resources["water"] = new_water
    resources["milk"] = new_milk
    resources["coffee"] = new_coffee
    cost = float(choice["cost"])
    Money = Money + cost
    print(f"Here is your {drink}. Enjoy!")

serve_continue = True

while serve_continue:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "report":
        report(resources)
    elif user_choice == "off":
        serve_continue = False
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        if check_resources(user_choice, resources):
            total = process_coins()
            check_price(user_choice, total)
            make_coffee(user_choice, resources)
        else:
            serve_continue = False
