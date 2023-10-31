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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

MONEY = 0


def machine():
    should_continue = True
    while should_continue:
        orders = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if orders == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${MONEY}")
        elif orders == "off":
            should_continue = False
        elif orders == "espresso" or orders == "latte" or orders == "cappuccino":
            if check_resources(orders):
                process_coins(orders, MENU[orders]["cost"])
        else:
            print("Wrong prompt")


def check_resources(coffee_type):
    if "water" in MENU[coffee_type]["ingredients"]:
        if resources["water"] < MENU.get(coffee_type)["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            return False
    if "milk" in MENU[coffee_type]["ingredients"]:
        if resources["milk"] < MENU.get(coffee_type)["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return False
    if "coffee" in MENU[coffee_type]["ingredients"]:
        if resources["coffee"] < MENU.get(coffee_type)["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
    return True


def transaction_completed(coffee_type):
    global MONEY
    if "water" in MENU[coffee_type]["ingredients"]:
        less_water = (
            resources.get("water") - MENU.get(coffee_type)["ingredients"]["water"]
        )
        resources["water"] = less_water
    if "milk" in MENU[coffee_type]["ingredients"]:
        less_milk = resources.get("milk") - MENU.get(coffee_type)["ingredients"]["milk"]
        resources["milk"] = less_milk
    if "coffee" in MENU[coffee_type]["ingredients"]:
        less_coffee = (
            resources.get("coffee") - MENU.get(coffee_type)["ingredients"]["coffee"]
        )
        resources["coffee"] = less_coffee
    MONEY += MENU.get(coffee_type)["cost"]


def process_coins(coffee_type, cost):
    print("Please insert coins.")
    money_putted = int(input("How many quarters?: ")) * 0.25
    money_putted += int(input("How many dimes?: ")) * 0.1
    money_putted += int(input("How many nickles?: ")) * 0.05
    money_putted += int(input("How many pennies?: ")) * 0.01
    if money_putted > cost:
        change = round(money_putted - cost, 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {coffee_type} ☕️.Enjoy!")
        transaction_completed(coffee_type)
    elif money_putted == cost:
        print(f"Here is your {coffee_type} ☕️.Enjoy!")
        transaction_completed(coffee_type)
    else:
        print("Sorry that's not enough money. Money refunded.")


machine()
