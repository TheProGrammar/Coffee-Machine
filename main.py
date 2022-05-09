import time
from data import MENU
from data import resources

beverage_list = ["espresso", "latte", "cappuccino"]
accepted_answers = [beverage_list, "off", "report"]


def process_coins(coffee_choice):
    """Calculates the amount of money needed for chosen coffee.
    Sums up the inserted coins and gives back change if needed.
    Will repeat the process if not enough coins were inserted."""

    cost = MENU[coffee_choice]["cost"]

    while True:
        print(f"\nThe cost of {coffee_choice} is ${cost}.\n"
              f"Please insert coins.")

        quarters_input = int(input("How many quarters? ")) * 0.25
        dimes_input = int(input("How many dimes? ")) * 0.1
        nickels_input = int(input("How many nickels? ")) * 0.05
        pennies_input = int(input("How many pennies? ")) * 0.01

        total_amount_inserted = round(quarters_input + dimes_input + nickels_input + pennies_input, 2)
        difference_amount = total_amount_inserted - cost

        print(f"You inserted ${total_amount_inserted}.")

        if total_amount_inserted > cost:
            print(f"Your change is: ${round(difference_amount, 2)}")
            update_resources(coffee_choice)
            make_coffee(coffee_choice)
            break
        else:
            print(f"You did not insert enough funds. ${abs(difference_amount)} more is needed.")


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


def not_enough_resources(user_choice):
    print(f"\nThere is not enough ingredients to make your {user_choice}.")
    print("We are sorry about this.")
    print("")


def update_resources(user_choice):
    ingredients = MENU[user_choice]["ingredients"]

    resources["water"] -= ingredients["water"]
    resources["coffee"] -= ingredients["coffee"]
    resources["money"] += MENU[user_choice]["cost"]

    if not user_choice.lower().startswith("e"):
        resources["milk"] -= ingredients["milk"]


def make_coffee(coffee_choice):
    """Simulates the process of making the chosen coffee.
    Will ask user for further action."""

    global running
    print(f"Making your {coffee_choice}...")
    time.sleep(2)
    print("Your coffee is ready! Here you go ☕")

    if input("\nWould you like another drink? Yes or No: ").lower().startswith("y"):
        pass
    else:
        turn_off()
        running = False


def print_report():
    """Print report stating the current amount of resources in the machine"""

    print("Printing report. Please wait...")
    time.sleep(2)

    print("Current resources are: \n"
          f"Water: {resources['water']}ml \n"
          f"Milk: {resources['milk']}ml \n"
          f"Coffee: {resources['coffee']}g \n"
          f"Money: ${resources['money']}\n")


def turn_off():
    """Turn off the machine/program with a goodbye message."""
    print("Turning off...")
    time.sleep(2)
    print("Goodbye")


running = True

while running:
    # Main program loop
    user_prompt = input("What would you like? Espresso/Latte/Cappuccino: ").lower()

    if user_prompt == "off":
        turn_off()
        running = False

    elif user_prompt == "report":
        print_report()

    elif user_prompt in beverage_list:
        if check_ingredients(user_prompt):
            # If machine has enough resources
            process_coins(user_prompt)
        else:
            # In case of insufficient resources
            not_enough_resources(user_prompt)

    else:
        print("Please choose valid options only")
        continue
