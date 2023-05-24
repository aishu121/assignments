'''
#task 1
# ques 1
a,b,c=1,2.01,'string'

# ques 2
x=2j+10
y=22
z=2j+10
x=y
y=z
print(" x is equal to ",x)
print("y is equal to",y)

# ques 3
#swapping numbers using a third variable
num1= 20
num2= 40
num3= 20
num1=num2
num2=num3
print("num1 is eual to",num1)
print("num2 is equal to",num2)
# swapping numbers with out using a third variable
num1=20
num2=40
num1,num2=num2,num1
print("num 1 is",num1)
print("num 2 is",num2)

#ques 4
# Taking input from the user in Python 2.x
user_input = raw_input("Enter your input: ")
# Printing the user input in Python 2.x
print "Python 2.x:", user_input

#ques 5
# Ask the user to enter the first number
num1 = int(input("Enter the first number (between 1 and 10): "))

# Validate the first number
while num1 < 1 or num1 > 10:
    num1 = int(input("Invalid input. Please enter the first number between 1 and 10: "))

# Ask the user to enter the second number
num2 = int(input("Enter the second number (between 1 and 10): "))

# Validate the second number
while num2 < 1 or num2 > 10:
    num2 = int(input("Invalid input. Please enter the second number between 1 and 10: "))

# Add the two numbers
z = num1 + num2

# Add 30 to z
result = z + 30

# Print the final result
print("The final result is:", result)

# ques 6 :
# Ask the user to enter a value
value = input("Enter a value: ")

# Get the data type of the entered value
data_type = type(eval(value))

# Print the data type of the entered value
print("The data type of the input value is:", data_type)
#ques 7
upperCamelCase = "Upper Camel Case"
lowerCamelCase = "Lower Camel Case"
snake_case = "Snake Case"
UPPERCASE = "Uppercase"

# ques 8
a = 10  # Assigning an integer value to 'a'
  # Output: 10

a = "Hello"  # Assigning a string value to 'a' (different data type)
print(a)  # Output: Hello
# yes the value changes evrey time you assign a new value to it .
'''


