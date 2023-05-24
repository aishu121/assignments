#ques 1
def find_uppercase_chars(input_string):
    uppercase_chars = [char for char in input_string if char.isupper()]
    return uppercase_chars
input_string = input("Enter a string: ")
uppercase_chars = find_uppercase_chars(input_string)
print("Uppercase characters:", uppercase_chars)

ques2 :
def construct_student_subject_dict(students, subjects):
    student_subject_dict = {student: subject for student, subject in zip(students, subjects)}
    return student_subject_dict

# Sample input
students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']

# Call the function to construct the dictionary
student_subject_dict = construct_student_subject_dict(students, subjects)

# Print the result
print(student_subject_dict)

#ques 4
def reverse_string(input_string):
    length = len(input_string)
    for index in range(length - 1, -1, -1):
        yield input_string[index]

# Input string
input_string = "Consultadd Training"

# Create a generator object
reverse_generator = reverse_string(input_string)

# Convert the generator to a reversed string
reversed_string = "".join(reverse_generator)

# Print the reversed string
print(reversed_string)

#ques 5
def uppercase_decorator(function):
    def wrapper():
        original_result = function()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase_decorator
def greet():
    return "Hello, World!"

# Call the decorated function
result = greet()

# Print the modified result
print(result)


