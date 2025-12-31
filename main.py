import coffee_data, art

def get_report():
    """Updates the report text to include current money in coffee machine"""
    rep = coffee_data.resources
    rep["money"] = money

    return rep


def check_resources(order):
    """Returns true when the order can be made, False if ingredients are insufficient."""
    current_resources = coffee_data.resources
    order_ingredients = coffee_data.MENU[order]["ingredients"]
    is_enough = False
    for key in current_resources and order_ingredients:
        r_key = current_resources[key]
        i_key = order_ingredients[key]

        if r_key >= i_key:
            is_enough = True
        elif r_key < i_key:
            print(f"Sorry, there is not enough {key} to make {order}.")
            is_enough = False
            break

    return is_enough


def process_coins(cost):
    """Returns the total from the coins inserted."""
    quarters = 0.25; dimes = 0.10; nickles = 0.05; pennies = 0.01
    total_paid = float(int(input("How many quarters? ")) * quarters)
    total_paid += float(int(input("How many dimes? ")) * dimes)
    total_paid += float(int(input("How many nickles? ")) * nickles)
    total_paid += float(int(input("How many pennies? ")) * pennies)

    change = round(total_paid - cost,2)
    print(f"Total paid: ${total_paid}")
    if total_paid < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return -1
    elif total_paid >= cost:
        return change


def make_coffee(drink):
    """Deducts ingredients needed from the resources. Returns updated resources"""
    current_resources = get_report()
    order_ingredients = coffee_data.MENU[drink]["ingredients"]

    for key in current_resources and order_ingredients:
        ingredient_left = current_resources[key] - order_ingredients[key]
        current_resources[key] = ingredient_left
    print(f"Here is your {drink} {art.emoji}. Enjoy!")

    return current_resources


machine_on = True
money = 0

while machine_on:
    print(art.shop_logo)
    print("Welcome to the Coffee Cup!!")
    coffee_order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee_order == "off":
        machine_on = False
        break
    elif coffee_order == "report":
        report = get_report()
        print(f"Water: {report["water"]}ml")
        print(f"Milk: {report["milk"]}ml")
        print(f"Coffee:{report["coffee"]}g")
        print(f"Money: ${report["money"]}")
    else:
        enough = check_resources(coffee_order)
        if enough:
            price = coffee_data.MENU[coffee_order]["cost"]
            print(f"The price for {coffee_order} is ${price}")
            print("Please insert coins.")
            extra_change = process_coins(price)

            if extra_change == -1:
                continue
            else:
                if extra_change >= 0:
                    print(f"Here is ${extra_change} in change.")
                    # Adds coffee money to the coffee machine in the report
                    money += price
                    make_coffee(coffee_order)
                    continue
        else:
            print("Please try again.")