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

profit = 0
resources = {
    "water": 500,
    "milk": 500,
    "coffee": 500,
}

def print_report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}ml')
    print(f'Money: ${round(profit, 2)}')

def sufficient_resources(ingredients):
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f'Sorry, not enough {item}.')
            return False
    return True

def process_coins():
    print('Please insert coins.')
    total = int(input('How many quarters? ')) * 0.25
    total += int(input('How many dimes? ')) * 0.10
    total += int(input('How many nickels? ')) * 0.05
    total += int(input('How many pennies? ')) * 0.01

    return total

def is_transition_successful(money_received, drink_cost):
    if money_received < drink_cost:
        print('Not enough coins. Money refunded.')
        return False
    elif money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'Here is your change in the amount of ${change}')
        global profit
        profit += drink_cost
        return True

def make_coffee(drink, ingredients):
    if sufficient_resources(ingredients):
        print(f'Here is your {drink}. Enjoy!')
        for item in ingredients:
            resources[item] -= ingredients[item]
    else:
        print(f'Not enough ingredients! Money refunded.')

def main():
    is_on = True
    
    while is_on:
        choice = input('What would you like (espresso, latte, or cappuccino)? ').lower()

        if choice == 'off':
            is_on = False
        elif choice == 'report':
            print_report()
        elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
            drink = MENU[choice]
            drink_cost = drink["cost"]
            money_received = process_coins()

            if is_transition_successful(money_received, drink_cost):
                make_coffee(choice, drink["ingredients"])
            else:
                print('Not enough money. Try again.')
        else:
            print('Not a valid choice. Please try again.')
            continue

main()