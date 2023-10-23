# HW-5
# 1. Create a list with the numbers from 1 to 10 and print it.
list_1 = []
for i in range(1, 11):
    list_1.append(i)
print(list_1)
# 1.1. Create a list with the numbers from 1 to 1000 and print it.
list_2 = []
for i in range(1, 1000 + 1):
    list_2.append(i)
print(list_2)


# 2. Reverse the order of the elements in the list from problem 1 and print the result.
list_1.reverse()
print('Reversed list_1: ', list_1)
list_2.reverse()
print('Reversed list_1: ', list_2)


# 3. Given a list of words, create a new list containing the lengths of each word.
words = ['banana', 'strawberry', 'sour cherry', 'mango', 'something']
words_length = []
for word in words:
    words_length.append(len(word))
print(words_length)
# 3.1. Given a list of words, create a new dictionary mapping every word to it's length.
words_length_dict = {}
for word in words:
    length = len(word)
    words_length_dict[word] = length
print(words_length_dict)


# 4. Write a function that takes a list and returns the sum of all even numbers in the list.
def even(n):
    sum = 0
    for number in n:
        if number % 2 == 0:
            sum += number
    return sum

example_list = [2, 3, 6, 77, 88, 33, 44, 56, 7, 8, 20]
result = even(example_list)
print(result)


# 5. Given a tuple of integers, find the maximum and minimum values without using built-in functions
def min_max(tuple_example):
    max_value = tuple_example[0]
    min_value = tuple_example[0]
    for number in tuple_example:
        if number > max_value:
            max_value = number

        if number < min_value:
            min_value = number
    return min_value, max_value

tuple_ex = (1, 2, 3, 4, 5, 6, 7, 8)
min_value, max_value = min_max(tuple_ex)
print(f'Min value: {min_value}\nMax value: {max_value}')


# 6. Implement a basic queue structure ( as a global var ) by defining two functions `enqueue` and `dequeue.
queue = []
def enqueue(item):
    global queue
    queue.append(item)
def dequeue():
    global queue
    if len(queue) == 0:
        print("Queue is empty")
    else:
        return queue.pop(0)
enqueue(1)
enqueue(2)
enqueue(3)
print("Queue", queue)
item = dequeue()
if item is not None:
    print("Dequeued item: ", item)
print("Queue: ", queue)


# 7. Create a dictionary that maps students to their bank account number. Some students may have multiple bank accounts.
students_acc = {
    'Radoslav': ['5657556567677', '555768678'],
    'Ani': ['123456789', '1234777777', '7737372872'],
    'Gabi': ['636499367'],
    'Velislav': []
}


# 8. Think of a function that can hash lists. Implement it and test it.
def hash_function(input_list):
    tuple_list = tuple(input_list)
    return hash(tuple_list)

list_1 = [9, 10, 11, 12, 13]
hash_1 = hash_function(list_1)
print('Hash of list1: ', hash_1)


# 9. Write a function that counts the frequency of each word in a given string and returns a dictionary with the result.
def count(some_string):
    word_freq = {}
    words = some_string.split()
    for word in words:
        word = word.strip(".,!?/()").lower()
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq
# strip to remove any additional (.!?:,) for a better counting
example_text = "This is an example text. This is an example text with repeated words. Example. Text. text."
result = count(example_text)
print(result)


# 10. Create two sets with some common elements and find their intersection.
set_1 = {"radoslav", 1, 2, 3}
set_2 = {1, 5, "radoslav"}
intersection_result = set_1.intersection(set_2)
print(intersection_result)


# 11. Given two sets, write a function that determines if one set is a subset of the other.
def is_subset(set1, set2):
    return set1.issubset(set2)

result_is_subset = is_subset(set_1, set_2)
print(result_is_subset)


# 12. Write a function to remove duplicates from a list using a set.
def remove_dupl(example_list):
    list_to_set = set(example_list)
    set_to_list = list(list_to_set)

    return set_to_list

some_list = [1,1,1,2,2,2,3,3,3,4,4]
result = remove_dupl(some_list)
print(result)


# 13. Use list comprehension to create a list of the squares of even numbers from 1 to 30.
even_numbers = [x **2 for x in range(2, 31, 2)]
print(even_numbers)


# 14. Given a list of words, create a dictionary where the keys are the words and the values are their lengths, using dictionary comprehension.
words = ['banana', 'strawberry', 'sour cherry', 'mango', 'something']
words_length_dict2 = {word: len(word) for word in words}
print(words_length_dict2)


# 15. Write a program that generates a set of prime numbers less than 100 using list comprehensions and sets.
# Hint: Write a function that checks if a number is prime or not.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numers = {num for num in range(2, 100) if is_prime(num)}
print(prime_numers)