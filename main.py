import csv
import json
# 2. Write a program to reverse a given string without using string slicing.
def reversing(string):
    str = ''
    for i in string:
        str = i + str
    return str
print(reversing('bro'))

#0. Create a program that checks if a given word or phrase is a palindrome (reads the same forwards and backward).
string = 'bob'
is_palindrome = reversing(string)
if is_palindrome:
    print('yes')
else:
    print('no')
# 1. Write a function that checks if a given number is prime or not.
def prime(n):
    if n > 1:
        for i in range(2, int(n/2) + 1):
            if n % i == 0:
                print(f' {n} is NOT a prime number.')
                break
            else:
                print(f'{n} is prime number.')
    else:
        print(f'{n} is NOt a prime number.')
prime(5)
# 2. Write a program to reverse a given string without using string slicing.
# def reversing(string):
#     str = ''
#     for i in string:
#         str = i + str
#     return str
# print(reversing('bro'))
# 3. Create a program that checks if two given strings are anagrams of each other.
# 4. Write a program that counts the number of words in a given string.
def words_count(str):
    words = str.split()
    word_count = len(words)
    print(f"Number of words in text file are: {word_count}")
words_count('some str some str some str....')
# 5. Create a program that reads a CSV file, "sales.csv," containing sales data, and a JSON file, "products.json," with product information. Calculate the total revenue for each product and save it in a new CSV file called "product_revenue.csv."
def read_csv(file_path):
    file_path = 'sales.csv'
    data = []
    with open(file_path, 'w') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

def read_json(file_path):
    with open(file_path, 'r') as jsonfile:
        data = json.load(jsonfile)
    return data

def calculate_product_revenue(sales_data, product_data):
    product_revenue = {}
    for sale in sales_data:
        product_id = sale['product_id']
        quantity = int(sale['quantity'])
        price = float(sale['price'])
        if product_id in product_revenue:
            product_revenue[product_id] += quantity * price
        else:
            product_revenue[product_id] = quantity * price

    product_revenue_list = []
    for product_id, revenue in product_revenue.items():
        product_name = product_data.get(product_id, 'Unknown Product')
        product_revenue_list.append({'product_id': product_id, 'product_name': product_name, 'revenue': revenue})

    return product_revenue_list

def save_product_revenue_to_csv(product_revenue, output_file):
    with open(output_file, 'w', newline='') as csv_file:
        fieldnames = ['product_id', 'product_name', 'revenue']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(product_revenue)
sales_data = read_csv("sales.csv")
product_data = read_json("products.json")
product_revenue = calculate_product_revenue(sales_data, product_data)
save_product_revenue_to_csv(product_revenue, "product_revenue.csv")
# 6. Develop a Python script that reads a JSON file called "inventory.json" with information about products and their quantities. Create a new CSV file, "low_stock.csv," containing the names of products with a quantity less than 10.
def filter_low_stock(products, threshold=10):
    low_stock_products = [product for product in products if product['quantity'] < threshold]
    return low_stock_products

def write_low_stock_csv(low_stock_products, output_file_path):
    fieldnames = ['Product', 'Quantity']

    with open(output_file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for product in low_stock_products:
            writer.writerow({
                'Product': product['name'],
                'Quantity': product['quantity']
            })

def add_product(products):
    name = input("Enter the product name: ")
    quantity = int(input("Enter the product quantity: "))

    products.append({
        'name': name,
        'quantity': quantity
    })

    print(f"Product '{name}' added successfully.")

def save_to_json(products, json_file_path):
    with open(json_file_path, 'w') as json_file:
        json.dump(products, json_file, indent=2)


input_json_path = "inventory.json"
output_csv_path = "low_stock.csv"

try:
    with open(input_json_path, 'r') as json_file:
        products = json.load(json_file)
except FileNotFoundError:
    print(f"File {input_json_path} not found. Creating a new JSON file.")
    products = []

while True:
    print("1. Add Product")
    print("2. Calculate and Save Low Stock")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        add_product(products)
    elif choice == '2':
        low_stock_products = filter_low_stock(products)
        write_low_stock_csv(low_stock_products, output_csv_path)
        save_to_json(products, input_json_path)
        print(f"Low stock products have been saved to {output_csv_path}.")
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

# 7. Write a program that is given a number and an array and checks if there is a pair of numbers in the array that has a sum equal to the given number. ( two-sum problem )
def has_pair_with_sum(arr, target_sum):
    seen_numbers = set()

    for num in arr:
        complement = target_sum - num

        if complement in seen_numbers:
            return True
        seen_numbers.add(num)
    return False

try:
    target_sum = int(input("Enter the target sum: "))
    numbers = [int(x) for x in input("Enter the array of numbers (space-separated): ").split()]
    result = has_pair_with_sum(numbers, target_sum)

    if result:
        print("There is a pair with the given sum.")
    else:
        print("No pair found with the given sum.")
except ValueError:
    print("Invalid input. Please enter valid integers.")