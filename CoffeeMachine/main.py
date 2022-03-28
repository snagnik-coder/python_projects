from menu import MENU
from menu import resources

def coffee_machine(money):
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    money_received = 0
    if choice == "off":
        return
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
        coffee_machine(money)

    if choice not in ["espresso", "cappuccino", "latte"]:
        print("Invalid input")
        coffee_machine(money)

    if resources['water'] < MENU[choice]['ingredients']['water']:
        print("Sorry there is not enough water.")
        coffee_machine(money)
    if choice != "espresso":
        if resources['milk'] < MENU[choice]['ingredients']['milk']:
            print("Sorry there is not enough milk.")
            coffee_machine(money)
    elif resources['coffee'] < MENU[choice]['ingredients']['coffee']:
        print("Sorry there is not enough coffee.")
        coffee_machine(money)

    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    money_received = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if money_received < MENU[choice]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        coffee_machine(money)
    money += MENU[choice]['cost']
    change = money_received - MENU[choice]['cost']
    resources['water'] -= MENU[choice]['ingredients']['water']
    if choice != "espresso":
        resources['milk'] -= MENU[choice]['ingredients']['milk']
    resources['coffee'] -= MENU[choice]['ingredients']['coffee']
    if change > 0:
        print(f"Here is ${change} in change.")
    print(f"Here is your {choice} ☕. Enjoy!")
    coffee_machine(money)


coffee_machine(0)