#task 4
#ques 1
'''
input_string = "1234abcd"

# Reverse the string using slicing
reversed_string = input_string[::-1]

print("Reversed string:", reversed_string)

#ques2
def count_upper_lower(string):
    uppercase_count = 0
    lowercase_count = 0

    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    print("No. of Uppercase characters:", uppercase_count)
    print("No. of Lowercase characters:", lowercase_count)


# Example usage
input_string = "abcSdefPghijQkl"
count_upper_lower(input_string)

#ques3
def get_unique_elements(lst):
    return list(set(lst))

# Example usage
input_list = [1, 2, 2, 3, 4, 4, 5, 5]
unique_list = get_unique_elements(input_list)

print("Original List:", input_list)
print("Unique List:", unique_list)

#ques 4
input_sequence = input("Enter hyphen-separated words: ")

# Split the input sequence into individual words
words = input_sequence.split("-")

# Sort the words alphabetically
sorted_words = sorted(words)

# Join the sorted words with hyphens
result = "-".join(sorted_words)

print("Sorted sequence:", result)

#ques 5
lines = []
while True:
    line = input("Enter a line (or press Enter to finish): ")
    if line == "":
        break
    lines.append(line.upper())

print("Modified lines:")
for line in lines:
    print(line)

#ques 6
def compute_and_print_sum(num1_str, num2_str):
    num1 = int(num1_str)
    num2 = int(num2_str)
    sum_result = num1 + num2
    print("Sum:", sum_result)


# Example usage
num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")
compute_and_print_sum(num1_str, num2_str)

#ques7
def print_string_with_max_length(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    if len1 > len2:
        print(str1)
    elif len2 > len1:
        print(str2)
    else:
        print(str1)
        print(str2)


# Example usage
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
print_string_with_max_length(string1, string2)

#ques 8
def generate_square_tuple():
    squares = tuple(num ** 2 for num in range(1, 21))
    print(squares)


# Example usage
generate_square_tuple()

#ques 9
def showNumbers(limit):
    for num in range(limit + 1):
        if num % 2 == 0:
            print(num, "EVEN")
        else:
            print(num, "ODD")


# Example usage
showNumbers(3)

#ques10
even_numbers = list(filter(lambda x: x % 2 == 0, range(1, 21)))

print("Even Numbers:", even_numbers)

#ques 11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_squares = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))

print("Even Squares:", even_squares)

#ques12
def compute_division():
    try:
        result = 5 / 0
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")


# Example usage
compute_division()

#ques 13
from functools import reduce

lst = [1, 2, 3, 4, 5, 6, 7]

result = reduce(lambda x, y: x * 10 + y, lst)

print("Flattened number:", result)

#ques 14
numbers = range(1, 101)  # Consider numbers from 1 to 100

result = list(filter(lambda x: x % 3 != 0 and x % 7 == 0, numbers))

print("Values not divisible by 3 but multiple of 7:", result)

#ques 15
# Define the function that multiplies a number by itself
def multiply_self(n):
    return n * n

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Use map to apply the function to each element in the list
squared_numbers = list(map(multiply_self, numbers))

# Print the result
print(squared_numbers)

#ques 16
def foo():
    try:
        return 1
    finally:
        return 2

k = foo()
print(k)  # prints 2

def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('after f?')

a()  # will raise NameError because f and x are not defined

'''

