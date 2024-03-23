from inputs import menu, resources

def report_generator():
    """
    Returns a list containing the remaining machine resources in this order:
    water, milk, coffee
    """
    current_resources = []
    for key, value in resources.items():
        current_resources.append(value)
    return current_resources


def resource_checker(drink):
    """
    Checks if there is sufficient resources to make a given drink.
    Returns True if there is and False if there's not.
    """
    sufficient_resource = True
    drink_ingredients = menu[drink]["ingredients"]
    for key, value in drink_ingredients.items():
        if resources[key] < value:
            print(f"Sorry, there is not enough {key}")
            sufficient_resource = False
    return sufficient_resource


def cost_checker(drink):
    """
    Returns the cost of a given drink.
    """
    cost = menu[drink]["cost"]
    return cost

def income_calculator(quarters, dimes, nickles, pennies):
    """
    Returns the total income given by the user by adding all the coins.
    """
    income = 0
    income = 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies
    return income


def resource_extractor(drink):
    """
    Subtracts the ingredients from the resources.
    """
    ingredients = menu[drink]["ingredients"]
    for ingredient, amount in ingredients.items():
        resources[ingredient] -= amount
    

should_continue = True
machine_money = 0

while should_continue:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        print("The machine is shutting down...")
        should_continue = False
    elif user_input == "report":
       print(f"Water: {report_generator()[0]}ml")
       print(f"Milk: {report_generator()[1]}ml")
       print(f"Coffee: {report_generator()[2]}g")
       print(f"Money: ${machine_money}")
    elif user_input not in menu:  
        print("This is not a valid option!")
        continue
    else:
        if resource_checker(user_input):
            quarters = int(input("How many 0.25 coins? "))
            dimes = int(input("How many 0.10 coins? "))
            nickles = int(input("How many 0.05 coins? "))
            pennies = int(input("How many 0.01 coins? "))
            income = income_calculator(quarters, dimes, nickles, pennies)
            drink_cost = cost_checker(user_input)
            if drink_cost > income:
                print("Sorry that's not enough money. Money refunded.")
            elif drink_cost == income:
                machine_money += income
                resource_extractor(user_input)
                print(f"Here is your {user_input}. Enjoy!")
            else:
                machine_money += drink_cost
                print(f"Here is your refund: ${round(income - drink_cost, 2)}")
                resource_extractor(user_input)
                print(f"Here is your {user_input}. Enjoy!")
