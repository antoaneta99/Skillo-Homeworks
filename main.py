import csv
import json
# 1. Create a Python script that reads a text file called "numbers.txt" containing integers and calculates their sum.
numbers_text = "numbers.txt"
sum = 0
with open(numbers_text, 'w') as file:
    file.write("1\n")
    file.write("2\n")
    file.write("3\n")

with open(numbers_text, 'r') as file:
    for line in file:
        try:
            number = int(line.strip())
            sum += number
        except ValueError:
            print(f'Invalid integer on line" {line}')

print(f'Sum of numbers in numbers txt file is: {sum}')

# 2. Write a program that reads a text file, "words.txt," and counts the number of words in it.
text_file = 'some text'

with open(text_file, 'w') as file:
    file.write('some say')

with open(text_file, 'r') as file:
    content = file.read()
    words = content.split()
    word_count =len(words)
print(f"Number of words in text file are: {word_count}")

# 3. Create a Python script that prompts the user to enter student names and their corresponding scores, then stores this data in a CSV file called "student_scores.csv."
def write_to_csv(data):
    with open("student_scores.csv", mode='a') as file:
        writer = csv.writer(file)
        writer.writerow(['Student Name', 'Score'])
        writer.writerows(data)

def add_student():
    student_data = []
    while True:
        student_name = input("Enter student name or type 'done' to finish: ")
        if student_name.lower() == 'done':
            break
        try:
            score = float(input("Enter the student's score: "))
        except ValueError:
            print("Please enter a valid numerical score.")
            score = float(input("Enter the student's score: "))
        student_data.append([student_name, score])

    if not student_data:
        print("No data entered. Exiting.")
        return

    write_to_csv(student_data)
add_student()

# 4. Write a program that reads a CSV file called "employee_data.csv," and for each employee, calculates their total salary
# (considering base salary and bonuses) and saves it in a new CSV file called "total_salaries.csv."
def calculate_total_salary(base_salary, bonuses):
    return base_salary + sum(bonuses)

def read_employee_data(csv_file_path):
    employee_data = []

    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                employee_data.append(row)
    except FileNotFoundError:
        print('File not found.')

    return employee_data

def write_total_salaries(employee_data, output_file_path):
    fieldnames = ['Employee_ID', 'Base Salary', 'Bonuses', 'Total Salary']

    with open(output_file_path, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for employee in employee_data:
            employee_id = employee['Employee_ID']
            base_salary = float(employee['Base Salary'])
            bonuses = [float(bonus) for bonus in employee['Bonuses'].split(',')]
            total_salary = calculate_total_salary(base_salary, bonuses)

            writer.writerow({
                'Employee_ID': employee_id,
                'Base Salary': base_salary,
                'Bonuses': bonuses,
                'Total Salary': total_salary
            })

def add_employee(employee_data):
    employee_id = input("Enter Employee ID: ")
    base_salary = float(input("Enter Base Salary: "))
    bonuses = [float(bonus) for bonus in input("Enter Bonuses (comma-separated): ").split(',')]

    employee_data.append({
        'Employee_ID': employee_id,
        'Base Salary': base_salary,
        'Bonuses': ','.join(map(str, bonuses))
    })


employee_data_path = "employee_data.csv"
total_salaries_path = "total_salaries.csv"

employees = read_employee_data(employee_data_path)

while True:
    print("1. Add Employee")
    print("2. Calculate Total Salaries")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        add_employee(employees)
    elif choice == '2':
        write_total_salaries(employees, total_salaries_path)
        print(f"Total salaries have been calculated and saved to {total_salaries_path}.")
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

# 5. Design a program that reads a JSON file containing a list of products with names and prices. Calculate the total cost of all products and display it.
import json
products = [
    {"name": "Apple", "price": 10.99},
    {"name": "Banana", "price": 20.49},
    {"name": "Milk", "price": 5.99},
    {"name": "Coffee", "price": 15.75},
    {"name": "Cucumber", "price": 8.49}
]

json_filename = "products.json"

with open(json_filename, 'w') as json_file:
    json.dump(products, json_file)

def calculate_total_cost(products):
    total_cost = sum(product['price'] for product in products)
    return total_cost

def read_file():
    json_filename = "products.json"
    try:
        with open(json_filename, 'r') as json_file:
            products = json.load(json_file)
    except FileNotFoundError:
        print(f"Error: File '{json_filename}' not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{json_filename}'.")
        return

    total_cost = calculate_total_cost(products)

    print(f"Total cost of all products: £{total_cost}")

read_file()

# 6. Write a Python script that reads a JSON file, "contacts.json," containing contact information (name, email, phone).
def read_contacts_from_json(filename):
    try:
        with open(filename, 'r') as json_file:
            contacts = json.load(json_file)
        return contacts
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{filename}'.")
        return []

def write_contacts_to_json(contacts, filename):
    with open(filename, 'w') as json_file:
        json.dump(contacts, json_file)

def add_contact():
    contacts = read_contacts_from_json("contacts.json")

    name = input("Enter the contact's name: ")
    email = input("Enter the contact's email: ")
    phone = input("Enter the contact's phone number: ")

    new_contact = {"name": name, "email": email, "phone": phone}
    contacts.append(new_contact)

    write_contacts_to_json(contacts, "contacts.json")
    print("Contact added successfully.")

def create_contact_list():
    while True:
        print("\n1. Add Contact")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
create_contact_list()

# 7. Create a CSV file, "student_data.csv," with student names and their corresponding JSON data containing exam scores.
# Write a program that reads the CSV file and calculates the average score for each student.
def write_student_data_to_csv(student_data):
    with open("student_data.csv", 'a', newline='') as csv_file:
        fieldnames = ['Name', 'Scores']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if csv_file.tell() == 0:
            writer.writeheader()
        writer.writerows(student_data)

def calculate_average(scores):
    return sum(scores) / len(scores) if len(scores) > 0 else 0

def add_student():
    student_data = []

    while True:
        name = input("Enter the student's name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break

        try:
            exam_scores_input = input("Enter the exam scores (comma-separated): ")
            exam_scores = [int(score.strip()) for score in exam_scores_input.split(',')]
        except ValueError:
            print("Invalid input. Please enter exam scores as integers separated by commas.")
            continue

        student_data.append({'Name': name, 'Scores': exam_scores})

        if not student_data:
            print("No data entered. Exiting.")
            return

        write_student_data_to_csv(student_data)

add_student()

with open("student_data.csv", mode='r') as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        student_name = row['Name']
        scores = json.loads(row['Scores'])
        average_score = calculate_average(scores)
        print(f"{student_name}'s average score: {average_score}")


# 9. Provide an example XML file, "inventory.xml," that represents a list of products in a store. Write a Python program to read this XML file and print the names and prices of all products.
import os
import xml.etree.ElementTree as ET

def create_empty_xml(xml_file_path):
    root = ET.Element('inventory')
    tree = ET.ElementTree(root)
    tree.write(xml_file_path)

def print_product_info(xml_file_path):
    if not os.path.isfile(xml_file_path) or os.path.getsize(xml_file_path) == 0:
        print("No product information available.")
        return

    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    for product in root.findall('product'):
        name = product.find('name').text
        price = float(product.find('price').text)

        print(f"Product: {name}, Price: £{price:.2f}")

def add_product(xml_file_path):
    if not os.path.isfile(xml_file_path) or os.path.getsize(xml_file_path) == 0:
        create_empty_xml(xml_file_path)

    try:
        tree = ET.parse(xml_file_path)
    except ET.ParseError:
        create_empty_xml(xml_file_path)
        tree = ET.parse(xml_file_path)

    root = tree.getroot()

    name = input("Enter the product name: ")
    price = input("Enter the product price: ")

    new_product = ET.Element('product')
    name_element = ET.SubElement(new_product, 'name')
    name_element.text = name
    price_element = ET.SubElement(new_product, 'price')
    price_element.text = price

    root.append(new_product)

    tree.write(xml_file_path)

xml_file_path = "inventory.xml"

while True:
    print("1. Print Product Information")
    print("2. Add a New Product")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        print_product_info(xml_file_path)
    elif choice == '2':
        add_product(xml_file_path)
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")