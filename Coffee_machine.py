import json

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

def load_resources():
    """Load resources from a file."""
    try:
        with open('resources.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 0
        }

def save_resources(resources):
    """Save resources to a file."""
    with open('resources.json', 'w') as file:
        json.dump(resources, file)

resources = load_resources()

def is_resource_sufficient(order_ingredients):
    """Checks if resources are sufficient to make the drink."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    try:
        print("Please insert coins.")
        quarters = int(input("How many quarters? ")) * 0.25
        dimes = int(input("How many dimes? ")) * 0.10
        nickels = int(input("How many nickels? ")) * 0.05
        pennies = int(input("How many pennies? ")) * 0.01
        return quarters + dimes + nickels + pennies
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return process_coins()

def make_coffee(drink_name, order_ingredients):
    """Deducts the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    resources["money"] += MENU[drink_name]["cost"]
    print(f"Here is your {drink_name}. Enjoy!")

def report():
    """Prints a detailed report of resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")
    for drink, details in MENU.items():
        print(f"{drink.capitalize()}: Cost ${details['cost']}")

def coffee_input():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino/report/off) ").lower()

        if choice == "off":
            save_resources(resources)
            print("Machine turned off")
            break

        elif choice == "report":
            report()

        elif choice in MENU:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if payment >= drink["cost"]:
                    change = round(payment - drink["cost"], 2)
                    if change > 0:
                        print(f"Here is ${change} in change.")
                    make_coffee(choice, drink["ingredients"])
                else:
                    print("Sorry, that's not enough money. Money refunded.")

        else:
            print("Invalid choice. Please try again.")

coffee_input()