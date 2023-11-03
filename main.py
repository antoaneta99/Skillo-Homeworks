# Homework 8
# Problem 0:
# Fix the mistakes in the following snippet:
items = {"Coffee": 2.2, "Tea": 1.5, "Chocolate": 2.5}
income = 0

for item in items.keys():
    qty = int(input(f"How many {item}s have you sold? "))
    income += qty * items[item]
print(f"\nThe income today was £{income:0.2f}")

# Problem 1:
# Rewrite the following function so it is exception safe
def get_integer_input():
    try:
        num = int(input("Enter an integer: "))
        return num
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return get_integer_input()

number = get_integer_input()
print("You entered:", number)

# Problem 2:
# Research and understand how does selections sort work.
# Debug and fix the following code to make it correct
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
