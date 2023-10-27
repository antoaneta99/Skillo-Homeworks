#Problem 0:
# Create a class "Person" with a special method "__str__" to provide a string representation. Instantiate an object of this class and print it.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}"

person_1 = Person("Maria", 25)
print(person_1)
# Problem 1:
# Define a class "Email" with special methods "__eq__" and "__ne__" to compare two email addresses. Test the equality and inequality operators with different email instances.
class Email:
    def __init__(self, email):
        self.email = email

    def __eq__(self, other):
        return self.email == other.email

    def __ne__(self, other):
        return not self == other

email_1 = Email("antoaneta99@gamil.com")
email_2 = Email("ani99@gmail.com")
print(email_1==email_2)

# Problem 2:
# Create a class "Student" with private attributes for name and age. Implement getter and setter methods for these attributes. Demonstrate their usage.
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age

person_1 = Student("Monika", 27)
print(person_1.get_name())
person_1.set_name("Ivo")
print(person_1.get_name())

# Problem 3:
# Design a class "BankAccount" with methods for deposit, withdrawal, and balance inquiry. Use encapsulation to protect the account balance. Demonstrate proper usage of the class.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Your balance is £{self.__balance}")

    def withdrawal(self, amount):
        self.__balance -= amount
        print(f"Withdrawn amount: £{amount}.\nNew balance: £{self.__balance}")

    def get_balance(self):
        return f"You balance is £{self.__balance}"

acc_1 = BankAccount(0)
acc_1.deposit(400)
acc_1.withdrawal(200)
acc_1.get_balance()
# Problem 4:
# Implement a class "Rectangle" with private attributes for length and width. Include special methods "__eq__" and "__lt__" to compare rectangles based on area and perimeter. Test the comparison operators with multiple instances.
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.perimeter() < other.perimeter()

rect_1 = Rectangle(1, 2)
rect_2 = Rectangle(2, 2)
rect_3 = Rectangle(1, 5)
rect_4 = Rectangle(1, 5)
print(rect_1 == rect_2)
print(rect_1 < rect_2)
print(rect_4 == rect_3)
print(rect_3 < rect_4)
# Problem 5:
# Design an abstract class "Vehicle" with a method "start_engine()". Create two subclasses, "Car" and "Bicycle," implementing the "start_engine()" method differently. Demonstrate polymorphism by calling the method on instances of both subclasses.
from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print(f"Your {self.name} start it's engine.")

class Bicycle(Vehicle):
    def start_engine(self):
        print(f"Your {self.name} has no engine. You got 2 pedals that u can use.")

car_1 = Car("Audi")
bc_1 = Bicycle("BMX")

car_1.start_engine()
bc_1.start_engine()
# PROBLEM 6:
# Implement a class "Book" with special methods "__str__" and "__len__" to provide a string representation and the number of pages. Create instances of "Book" and demonstrate the use of these methods.
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"The book {self.title} is written by {self.author} and is {self.pages} pages."

    def __len__(self):
        return self.pages

book_1 = Book("Harry Potter", "J. K. Rowling", 456)
# print(book_1)
print(str(book_1))
print(len(book_1))
# Problem 7:
# Create a class "Animal" with a special method "__init__" that sets a species attribute. Implement subclasses "Dog" and "Cat" with their own "__str__" methods. Use polymorphism to display species information.
class Animal:
    def __init__(self, breed):
        self.breed = breed

class Cat(Animal):
    def __init__(self, breed):
        super().__init__(breed)

    def __str__(self):
        return f"This cat's breed is {self.breed}."


class Dog(Animal):
    def __init__(self, breed):
        super().__init__(breed)

    def __str__(self):
        return f"This dog's breed is {self.breed}."


cat = Cat("Siams")
dog = Dog("Pekignese")
print(cat, dog)
# Problem 8:
# Design a class "Employee" with encapsulated attributes for name and salary. Implement a subclass "Manager" that inherits from "Employee" and includes an additional attribute for the department. Use getters and setters to access and modify these attributes.
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.__department = department

    def get_dep(self):
        return self.__department

    def set_dep(self, department):
        self.__department = department

employee1 = Employee("Viktor Viktorov", 5000)
manager1 = Manager("Rosen Rosenov", 10000, "F&B")

print(f'Employee Name: {employee1.get_name()}\nEmployee Salary: {employee1.get_salary()}')
print('------------------------------')
print(f'Manager Name: {manager1.get_name()}\nManager Salary: {manager1.get_salary()}\n'
      f'Manager Department: {manager1.get_dep()}')
# Problem 9:
# Create a class called "Employee" that has attributes name, start_date, PIN, phone, address, manager_name, department.
# Decide their access specifiers. Implement methods to calculate employee tenure, and business card info representation.
# i will use datetime module to calculate the tenure of curr employee for more accurate results
from datetime import datetime
class Employee:
    def __init__(self, name, start_date, pin, phone, address, manager_name, department):
        self.__name = name
        self.__start_date = start_date
        self.__pin = pin
        self.__phone = phone
        self.__address = address
        self.__manager_name = manager_name
        self.__department = department

    def tenure_calculation(self):
        start_date = datetime.strptime(self.__start_date, '%d-%m-%Y')
        current_date = datetime.now()
        tenure = current_date.year - start_date.year
        return f"{tenure} years within the company."

    def business_card_creation(self):
        business_card = f"Business card for: {self.__name}\n"
        business_card += f"Starting date: {self.__start_date}\n"
        business_card += f"PIN: {self.__pin}\n"
        business_card += f"Phone: {self.__phone}\n"
        business_card += f"Address: {self.__address}\n"
        business_card += f"Manager name: {self.__manager_name}\n"
        business_card += f"Department: {self.__department}\n"
        return business_card


employee_1 = Employee("Viktor Viktorov", "23-05-2020","123456789", "0888888888", "Sofia, Bulgaria, MLadost", "Rosen Rosenov", "F&B")
print(employee_1.tenure_calculation())
print(employee_1.business_card_creation())

# Problem 10:
# Create an abstract class "Employee" with attributes for name and salary.
# Implement a subclass "Manager" that inherits from "Employee" and includes an additional attribute for the department.
# Ensure that the "Employee" class enforces encapsulation.
# Every employee and manager should have a method to send a message to.
# The message must be stored. Create a class "Team" that has a manager and a list of members.
# Implement a method that sends a message to everyone in the team.
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        self.__message = None

    def send_mess(self, message):
        self._message = message

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.__department = department

    def send_mess(self, message):
        self._message = message


    def get_dep(self):
        return self.__department

class Team:
    def __init__(self, manager, members):
        self.__manager = manager
        self.__members = members

    def send_mess(self, message):
        self.__manager.send_mess(message)
        for member in self.__members:
            member.send_mess(message)
class TeamMember(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def send_message(self, message):
        super().send_mess(message)


manager = Manager("Viktor Viktorov", 6000, "F&B")
team_member1 = TeamMember("Rosen", 4000)
team_member2 = TeamMember("Ivan", 5000)
team = Team(manager, [team_member1, team_member2])

team.send_mess("Meeting at 10AM.")

print(f"Manager's message: {manager._message}")
print(f"Team member_1's message: {team_member1._message}")
print(f"Team member_2's message: {team_member2._message}")


