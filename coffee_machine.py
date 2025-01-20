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

def coffee_machine():
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    price = 0
    insufficent = "Resources are insufficient!"
    if user_input == "espresso":
        price = MENU["espresso"]["cost"]
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            return insufficent
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            return insufficent
        else:
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    elif user_input == "latte":
        price = MENU["latte"]["cost"]
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            return insufficent
        elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            return insufficent
        elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            return insufficent
        else:
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
    elif user_input == "cappuccino":
        price = MENU["cappuccino"]["cost"]
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            return insufficent
        elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            return insufficent
        elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            return insufficent
        else:
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
    elif user_input == "report":
        return resources
    elif user_input == "off":
        closed = "Closed"
        return closed
    else:
        invalid_input = "Invalid input"
        return invalid_input
    
    print(f"It is {price}$")
    user_money = float(input("Insert money: "))
    if user_money < price:
        insufficent_funds = "Insufficent funds"
        return insufficent_funds
    print(f"Here is your exchange: {user_money-price}$")
    print("Enjoy your coffee!")


while True:
    print(coffee_machine())