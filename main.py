# Problem 0:
# Complete the following function so that it returns the sum of the elements in the list passed as an argument
def sum_elements(arr):
    result = 0
    for n in arr:
        result += n
    return result

# print(sum_elements([1,2,3,4]))
# print(sum_elements([0]))
# print(sum_elements([]))
# print(sum_elements([-1, 1]))

# Problem 1: Simple Calculator Function
# Define a function called `simple_calculator` that takes two numbers and an operator ('+', '-', '*', or '/') as
# arguments and returns the result of the operation.
def simple_calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
result = simple_calculator(5, 3, "+")
print(result)

# Problem 2: Area of Shapes
# Create a module named `geometry` with functions to calculate the area of common
# shapes like a square, rectangle, triangle, and circle. Import this module and use it to calculate
# the areas of different shapes.
import geometry
square_area = geometry.square_area(5)
print("Area of square:", square_area)

rectangle_area = geometry.rectangle_area(4, 6)
print("Area of rectangle:", rectangle_area)

triangle_area = geometry.triangle_area(8, 3)
print("Area of triangle:", triangle_area)

circle_area = geometry.circle_area(4)
print("Area of circle:", circle_area)

# Problem 3: Temperature Conversion
# Write a program that converts temperatures between Celsius and Fahrenheit.
# Create two functions, one for each conversion, and use them in a program to convert temperatures
# provided by the user.
def celcius_to_fah(c):
    return (c * 9/5) + 32

def fah_to_celsius(f):
    return (f - 32) * 5/9

input_user = input("Would you like to convert from celsius to fahrenheit or the other way around?\n")
if input_user == "celsius to fahrenheit":
    celsius_input = int(input("How many degrees would you like to convert? "))
    result = celcius_to_fah(celsius_input)
    print(result)
elif input_user == "fahrenheit to celsius":
    fahrenheit_input = int(input("How many degrees would you like to convert? "))
    result = fah_to_celsius(fahrenheit_input)
    print(result)




