# Problem 0:
# Write a program that takes an integer input from the user and checks if it's odd or even.
# Use an if-else statement to print the result.
user_input = int(input("Type a number: "))
if user_input % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")

# Problem 1:
# Write a Python program to find the sum of all even numbers from 1 to 100 using a loop.
# Make use of control flow constructs like the for loop and conditional statements.
result = 0
for num in range(1, 101):
    if num % 2 == 0:
        result += num
print(result)

# Problem 2:
# Write a Python script that prompts the user in the console a simple problem
# ( how much does 5 + 17 equal to ) until the user provides a correct answer.
answer = 5 + 17
while True:
    user_answer = int(input("How much does 5 + 17 equals to: "))
    if user_answer == answer:
        print("Answer is correct.")
        break
    else:
        print("Incorrect. Try again.")


# Problem 3:
# Write a Python script that iterates over the first 1000 numbers and prints "Fizz" if the number is divisible by 3,
# "Buzz" if it's divisible by 5, and "FizzBuzz" if it's divisible by both 3 and 5.
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)


# Problem 4:
# Design a Python program that simulates a simple guessing game. The program should generate a random number between 1 and 100 and ask the user to guess it.
# Provide hints like "Too high" or "Too low" until the user guesses the correct number.
# Use a while loop for this game.
import random
rand_num = random.randint(1, 100)
game_on = True
while game_on:
    user_input = int(input("Guess a number: "))
    if user_input == rand_num:
        print(f"Correct! The number was: {rand_num}")
        game_on = False
    elif user_input > rand_num:
        print("Number too high. Try Again!")
    elif user_input < rand_num:
        print("Number too low. Try Again!")

# Problem 5:
# Modify problem 2 so that every time the user is prompted the problem is different.
# Think of a way to design that and come up with a proper solution for that.
import random
rand_int_1 = random.randint(1, 101)
rand_int_2 = random.randint(1, 101)
correct_answer = rand_int_1 + rand_int_2
game_on = True
while game_on:
    user = int(input(f'What does {rand_int_1} + {rand_int_2} evaluates to: '))
    if user == correct_answer:
        print(f"Well done! The correct answer is {correct_answer}.\n")
        user_new = input("Would you like to continue?\nType 'yes' or 'no':\n")
        if user_new == "yes":
            rand_int_1 = random.randint(1, 101)
            rand_int_2 = random.randint(1, 101)
            correct_answer = rand_int_1 + rand_int_2
        else:
            game_on = False
    if user > correct_answer:
        print('Answer too high. Try again')
    elif user < correct_answer:
        print('Answer too low. Try again')

# Problem 6:
# Write a Python program that takes an integer input from the user and prints the multiplication
# table for that number from 1 to 10 using a for loop.
user_input = int(input("Type a number: "))
for i in range(1, 11):
    result = user_input * i
    print(f"{user_input} x {i} = {result}")


# Problem 7:
# Create a Python program that checks if a given integer is a prime number.
# Use a for loop to iterate through possible divisors and use an if-else statement to determine if it's prime.
number = int(input('Enter a number: '))
is_prime = False
if number == 1:
    print(f'{number} is not a prime number.')
elif number > 1:
    for i in range(2, number):
        if number % i == 0:
            is_prime = True
    print(f'{number} is prime.')

# Problem 8: Pattern Printing
# Write a program that takes an integer 'n' as input and prints the following pattern using nested for loops:
num = int(input("Write a number: "))
for i in range(1, num+1):
    for j in range(1, i+1):
        print(j, end='')
    print('')





