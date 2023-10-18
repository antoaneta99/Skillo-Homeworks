# Problem 4: Online Shopping Cart
# Create a Python program that simulates an online shopping cart using a global dictionary variable.
# Every customer has unique id as a key. Define functions to add items to the cart, remove items,
# calculate the total price, and display the contents of the cart.
# Allow the user to interact with the cart by adding and removing items.
shopping_carts = {}


def add_item(customer_id, item_name, item_price, quantity):
    customer_id = str(customer_id)
    item_price = float(item_price)
    if customer_id not in shopping_carts:
        shopping_carts[customer_id] = {}
    if item_name in shopping_carts[customer_id]:
        shopping_carts[customer_id][item_name]['price'] = item_price
        shopping_carts[customer_id][item_name]['quantity'] += quantity
    else:
        shopping_carts[customer_id][item_name] = {'price': item_price, 'quantity': quantity}


def remove_item(customer_id, item_name, quantity):
    customer_id = str(customer_id)
    if item_name not in shopping_carts[customer_id]:
        print('Item not available in the cart.')
    if customer_id in shopping_carts and item_name in shopping_carts[customer_id]:
        if shopping_carts[customer_id][item_name]['quantity'] > quantity:
            shopping_carts[customer_id][item_name]['quantity'] -= quantity
            print(f'{item_name} has been removed {quantity} times.')
        else:
            print("Quantity of the current item in the cart, is less than what you entered.")


def calculate_total(customer_id):
    customer_id = str(customer_id)
    total = 0
    if customer_id in shopping_carts:
        for item_name, item_details in shopping_carts[customer_id].items():
            price = item_details['price']
            quantity = item_details['quantity']
            total += price * quantity
    return total


def display_cart(customer_id):
    customer_id = str(customer_id)
    if customer_id in shopping_carts:
        print(f"Shopping cart for customer {customer_id}:")
        for item_name, item_details in shopping_carts[customer_id].items():
            price = item_details['price']
            quantity = item_details['quantity']
            print(f"{item_name}: £{price} x {quantity}")
        print(f"Total Price: £{calculate_total(customer_id)}")
    else:
        print(f"You don't have any items in the cart.")



cart_on = True
while cart_on:
    print('Online Shopping Cart')
    print('1. Add item to the cart.')
    print('2. Remove item from cart.')
    print('3. View cart.')
    print('4. Exit.')

    choice = input('Enter your choice (1/2/3/4): ')
    if choice == '1':
        customer_id = int(input('Enter your customer ID: '))
        item_name = input('Enter item name: ')
        item_price = float(input('Enter item price: '))
        quantity = int(input('Enter quantity: '))
        add_item(customer_id, item_name, item_price, quantity)
        print(f'{quantity} {item_name}(s) added to the cart.')
    elif choice == '2':
        customer_id = int(input('Enter your customer ID: '))
        item_name = input('Enter item name: ')
        quantity = int(input('Enter quantity you want to remove: '))
        remove_item(customer_id, item_name, quantity)
    elif choice == '3':
        customer_id = int(input("Enter your customer ID: "))
        display_cart(customer_id)
    elif choice == '4':
        cart_on = False
    else:
        print("Please choice a valid option!")


