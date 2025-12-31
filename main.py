import coffee_data, art

def get_report():
    """Updates the report text to include current cash in coffee machine"""
    rep = coffee_data.resources
    rep["money"] = money

    return rep

def formatted_report(rep):
    """Formats the report text and displays it."""
    for key, value in rep.items():
        if key == "water" or key == "milk":
            print(f"{key.title()}: {value}ml")
        elif key == "coffee":
            print(f"{key.title()}: {value}g")
        elif key == "money":
            print(f"{key.title()}: ${value}")


def check_resources(order):
    """Gets data from resources and ingredients for the coffee order,
    and compare/check values for each key. Return True/False if there are enough resources or not."""
    current_resources = coffee_data.resources
    # print(current_resources)
    order_ingredients = coffee_data.MENU[order]["ingredients"]
    # print(order_ingredients)
    is_enough = False
    for key in current_resources and order_ingredients:
        r_key = current_resources[key]
        i_key = order_ingredients[key]

        if r_key >= i_key:
            # print(f"There are enough {key}")
            is_enough = True
        elif r_key < i_key:
            print(f"Sorry, there is not enough {key}")
            is_enough = False
            break
    return is_enough

def process_coins(cost):
    """Asks user to insert coins to pay for the coffee cost.
    Calculates total paid by user and check if user put in enough coins.
    If user put in more coins than the cost. Calculate the change"""
    quarters = 0.25; dimes = 0.10; nickles = 0.05; pennies = 0.01
    sum_quarters = float(int(input("How many quarters? ")) * quarters)
    sum_dimes = float(int(input("How many dimes? ")) * dimes)
    sum_nickles = float(int(input("How many nickles? ")) * nickles)
    sum_pennies = float(int(input("How many pennies? ")) * pennies)

    total_paid = sum_quarters + sum_dimes + sum_nickles + sum_pennies
    change = round(total_paid - cost,2)
    print(f"Total paid: ${total_paid}")
    if total_paid < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return -1
    elif total_paid >= cost:
        return change

def make_coffee(order):
    """This make_coffee function takes the coffee ingredients and subtracts from current resources.
    Returns updated report"""
    current_resources = get_report()
    order_ingredients = coffee_data.MENU[order]["ingredients"]
    # print(order_ingredients)

    for key in current_resources and order_ingredients:
        r_key = current_resources[key]
        i_key = order_ingredients[key]

        ingredient_left = r_key - i_key
        current_resources[key] = ingredient_left

    print(f"Here is your {order} {art.emoji}. Enjoy!")

    return current_resources


machine_on = True
money = 0.00

while machine_on:
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    print(art.shop_logo)
    print("Welcome to the Coffee Cup!!")
    coffee_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # print(coffee_order)
    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    # TODO: 3. Print report.
    if coffee_order == "off":
        machine_on = False
        break
    elif coffee_order == "report":
        report = get_report()
        print(formatted_report(report))
    else:
        # TODO: 4. Check resources sufficient
        enough = check_resources(coffee_order)
        if enough:
            price = coffee_data.MENU[coffee_order]["cost"]
            print(f"The price for {coffee_order} is ${price}")
            # TODO: 5. Process coins.
            print("Please insert coins.")
            extra_change = process_coins(price)

            # TODO: 6. Check if transaction is successful
            if extra_change == -1:
                continue
            else:
                if extra_change >= 0:
                    print(f"Here is ${extra_change} in change.")
                    # Adds coffee money to the coffee machine in the report
                    money += price
                    # TODO: 7. Make Coffee
                    make_coffee(coffee_order)
                    continue
        else:
            print("Sorry, you don't have enough ingredients.")
            break
