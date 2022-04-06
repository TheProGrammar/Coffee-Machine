import time
from data import MENU
from data import resources

beverage_list = ["espresso", "latte", "cappuccino"]
accepted_answers = [beverage_list, "off", "report"]


def process_coins():
    print("Coins processed")
    pass


def check_ingredients(coffee_choice):
    """Check if a user drink can be made with the current resource amount"""

    ingredients = MENU[coffee_choice]['ingredients']

    if coffee_choice == 'espresso':
        # Espresso is separated from other drinks because it has no value Milk
        if resources['water'] > ingredients['water'] and resources['coffee'] > ingredients['coffee']:
            return True
        else:
            return False

    else:
        if resources['water'] > ingredients['water'] and resources['milk'] > ingredients['milk'] \
                and resources['coffee'] > ingredients['coffee']:
            return True
        else:
            return False


def make_coffee(coffee_choice):
    print("Drink chosen")
    pass


def print_report():
    print("Checking ingredients. Please wait...")
    time.sleep(2)

    print("Current resources are: \n"
          f"Water: {resources['water']}ml \n"
          f"Milk: {resources['milk']}ml \n"
          f"Coffee: {resources['coffee']}g \n"
          f"Money: ${resources['money']}\n")


running = True

while running:
    user_prompt = input("What would you like? Espresso/Latte/Cappuccino: ")

    if user_prompt == "off":
        print("Goodbye...")
        running = False
        break
    elif user_prompt == "report":
        print_report()
    elif user_prompt in beverage_list:
        print(check_ingredients(user_prompt))
    else:
        print("Please choose valid options only")
        continue
