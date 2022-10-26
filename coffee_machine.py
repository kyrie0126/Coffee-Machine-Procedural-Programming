# Coffee Machine Project

from coffee_machine_menu import drinks, currency

# Initial inventory
inventory = {
    "water": 300,
    "coffee": 100,
    "milk": 200
}

# Initial revenue
revenue = float(0)
out_of_stock = 0


def inventory_check(order_input_prime):
    """Parameter: order_input_prime = order
    Checks for sufficient inventory."""
    order_input = order_input_prime


    def water_check(order_input):
        """Parameter: order_input = order
        Checks for sufficient water in inventory."""
        if drinks[order_input]["ingredients"]["water"] > inventory["water"]:
            message = "Sorry there isn't enough water"
            return message
        else:
            return inventory["water"] - drinks[order_input]["ingredients"]["water"]


    def coffee_check(order_input):
        """Parameter: order_input = order
        Checks for sufficient coffee in inventory."""
        if drinks[order_input]["ingredients"]["coffee"] > inventory["coffee"]:
            print("Sorry there isn't enough coffee")
        else:
            return inventory["coffee"] - drinks[order_input]["ingredients"]["coffee"]


    def milk_check(order_input):
        """Parameter: order_input = order
        Checks for sufficient milk in inventory."""
        if drinks[order_input]["ingredients"]["milk"] > inventory["milk"]:
            print("Sorry there isn't enough milk")
        else:
            return inventory["milk"] - drinks[order_input]["ingredients"]["milk"]


    inventory["water"] = water_check(order_input=order)
    inventory["coffee"] = coffee_check(order_input=order)
    inventory["milk"] = milk_check(order_input=order)


def change_calculator(order_input):
    """parameter: order_input = order
    Takes order as input, prompts user for payment, and calculates change."""
    price = float(drinks[order_input]['price'])
    amount_paid = 0

    quarters = int(input("Quarters: "))
    amount_paid += quarters * 0.25
    print("Remaining Balance: ${:.2f}".format(float(price - amount_paid)))

    dimes = int(input("Dimes: "))
    amount_paid += dimes * 0.1
    print("Remaining Balance: ${:.2f}".format(float(price - amount_paid)))

    nickels = int(input("Nickels: "))
    amount_paid += nickels * 0.05
    print("Remaining Balance: ${:.2f}".format(float(price - amount_paid)))

    pennies = int(input("Pennies: "))
    amount_paid += pennies * 0.01
    # amount_paid = float(quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01)
    if amount_paid < price:
        print("\nInsufficient payment. Please redo transaction")
        change_calculator(order_input=order_input)
    else:
        change = "${:.2f}".format(float(amount_paid - price))
        return change


def print_inventory():
    print("Updated inventory report:\n")
    print(f"Water: {inventory['water']}ml")
    print(f"Milk: {inventory['milk']}ml")
    print(f"Coffee: {inventory['coffee']}g")
    print(f"\nTotal revenue: " + "${:.2f}".format(revenue))


machine_on = True
while machine_on == True:

    # Collect drink order
    order = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()

    # Special order commands - report and off
    if order == "report":
        print_inventory()
        keep_brewing = True
        while keep_brewing == True:
            next_step = str(input("\nWhat would you like to do now?\n"
                                  "  'new order'\n"
                                  "  'view inventory'\n"
                                  "  'turn off'\n")).lower()
            if next_step == "new order":
                keep_brewing = False
            elif next_step == "view inventory":
                print_inventory()
            elif next_step == "turn off":
                machine_on = False
                keep_brewing = False
    elif order == "off":
        print("machine is powering down")
    else:
        inventory_check(order)

    # Payment
    print(f"Your {order} will cost: $" + "{:.2f}".format(float(drinks[order]['price'])))
    print(f"Your change is: {change_calculator(order_input=order)}")
    revenue += float(drinks[order]['price'])
    print(f"\nHere is your {order}. Enjoy!\n")
    keep_brewing = True
    while keep_brewing == True:
        next_step = str(input("\nWhat would you like to do now?\n"
                          "  'new order'\n"
                          "  'view inventory'\n"
                          "  'turn off'\n")).lower()
        if next_step == "new order":
            keep_brewing = False
        elif next_step == "view inventory":
            print_inventory()
        elif next_step == "turn off":
            machine_on = False
            keep_brewing = False


