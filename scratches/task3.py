'''
# task 3 ques 1
#Create a list of 10 elements of four different data types like int, string, complex and float.
my_list = [10, "Hello", 3+4j, 3.14, "World", 5.5, 2, 1+2j, 4.7, "Python"]
print(my_list)

#ques2
my_list = [10, 20, 30, 40, 50]

# Slicing to get elements at specific indices
slice1 = my_list[1:3]  # Get elements from index 1 to 2 (exclusive of 3)
slice2 = my_list[2:]  # Get elements from index 2 till the end
slice3 = my_list[:4]  # Get elements from the start till index 3 (exclusive of 4)
slice4 = my_list[:]  # Get all elements (copy the list)

print("Original List:", my_list)
print("Slice 1:", slice1)
print("Slice 2:", slice2)
print("Slice 3:", slice3)
print("Slice 4:", slice4)

#ques3
def calculate_sum_and_product(lst):
    total_sum = 0
    total_product = 1

    for num in lst:
        total_sum += num
        total_product *= num

    return total_sum, total_product
# Example usage
my_list = [2, 3, 4, 5]
sum_result, product_result = calculate_sum_and_product(my_list)

print("List:", my_list)
print("Sum:", sum_result)
print("Product:", product_result)

#ques4
def find_largest_smallest(lst):
    if not lst:  # Check if the list is empty
        return None, None

    smallest = largest = lst[0]  # Assume the first element is both the smallest and largest

    for num in lst:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return smallest, largest


# Example usage
my_list = [10, 5, 8, 20, 3]
smallest_num, largest_num = find_largest_smallest(my_list)

print("List:", my_list)
print("Smallest number:", smallest_num)
print("Largest number:", largest_num)

#ques 5
def remove_even_numbers(lst):
    new_list = []

    for num in lst:
        if num % 2 != 0:
            new_list.append(num)

    return new_list


# Example usage
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = remove_even_numbers(original_list)

print("Original List:", original_list)
print("New List (without even numbers):", new_list)

#ques 6
# Generate a list of numbers from 1 to 30 (both inclusive)
numbers = list(range(1, 31))

# Take the first and last 5 elements
first_five = numbers[:5]
last_five = numbers[-5:]

# Calculate the squares of the numbers
first_five_squares = [num ** 2 for num in first_five]
last_five_squares = [num ** 2 for num in last_five]

# Combine the squares of the first and last 5 elements
result = first_five_squares + last_five_squares

print("Result:", result)

#ques 7
list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]

# Replace the last element of list1 with list2
list1[-1:] = list2

print("Result:", list1)


#ques8
a = {1: 10, 2: 20}
b = {3: 30, 4: 40}

# Create a new dictionary by concatenating dictionaries a and b
result = {**a, **b}

print("Result:", result)

#ques 9
n = 5

# Create the dictionary with numbers and their squares
result = {x: x*x for x in range(1, n+1)}

print("Result:", result)

#ques 10
input_numbers = input("Enter comma-separated numbers: ")

# Split the input string into a list of numbers
numbers_list = input_numbers.split(",")

# Convert each number to a string using list comprehension
numbers_as_strings = [str(num) for num in numbers_list]

# Convert the list to a tuple
numbers_tuple = tuple(numbers_as_strings)

print("List:", numbers_as_strings)
print("Tuple:", numbers_tuple)


'''



