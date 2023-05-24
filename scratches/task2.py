'''
#Task 2
# ques 1
# Take input from the user
number = int(input("Enter a number: "))

# Check if the number is divisible by 3 and 5
if number % 3 == 0 and number % 5 == 0:
    print("Consultadd - Python Training")
# Check if the number is divisible by 3
elif number % 3 == 0:
    print("Consultadd")
# Check if the number is divisible by 5
elif number % 5 == 0:
    print("Python Training")
# If the number is not divisible by 3 or 5
else:
    print("Number is not divisible by 3 or 5")
#ques2
# Ask the user to choose an option
option = int(input("Choose an option:\n1 - Addition\n2 - Subtraction\n3 - Division\n4 - Multiplication\n5 - Average\n"))

# Perform the selected operation based on the chosen option
if option == 1:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
elif option == 2:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
elif option == 3:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num2 != 0:
        result = num1 / num2
    else:
        print("Division by zero is not allowed.")
        exit()
elif option == 4:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
elif option == 5:
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    result = (first + second) / 2
else:
    print("Invalid option selected.")
    exit()

# Check if the result is negative
if result < 0:
    print("NEGATIVE")
else:
    print("Result:", result)

# ques 4
while True:
    number = int(input("Enter a number: "))

    if number < 0:
        print("It's Over")
        break
    else:
        print("Good Going")

# ques 5
result = []

# Iterate over the range from 2000 to 3200 (inclusive)
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        result.append(num)

# Print the numbers that meet the condition
print("Numbers divisible by 7 but not a multiple of 5:")
print(result)

# ques 6
#1. output is 1,2,3
#2 When you run this corrected code, it will print the numbers 0, 1, and 2, and then break out of the loop when i reaches 3.
#3 it will print the numbers 0 to 4, and then break out of the loop.

#ques 7
for num in range(7):
    if num == 3 or num == 6:
        continue
    print(num, end=' ')

# ques 8
def count_letters_digits(input_string):
    letters = 0
    digits = 0

    for char in input_string:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1

    return letters, digits

# Accept input from the user
input_string = input("Enter a string: ")
# Call the function to count letters and digits
letter_count, digit_count = count_letters_digits(input_string)

# Print the results
print("Letters:", letter_count)
print("Digits:", digit_count)


#ques9
def guess_lucky_number():
    lucky_number = 7  # The correct lucky number
    while True:
        user_guess = int(input("Guess the lucky number: "))

        if user_guess == lucky_number:
            print("Congratulations! You guessed the correct number!")
            break

        answer = input("Wrong guess. Do you want to continue guessing? (yes/no): ")
        if answer.lower() == "no":
            break

# Call the function to start the game
guess_lucky_number()

#ques 10
counter = 1
lucky_number = 8 # The correct lucky number

while counter <= 5:
    user_guess = int(input("Type in the {} number: ".format(counter)))

    if user_guess == lucky_number:
        print("Good guess!")
    else:
        print("Try again!")

    counter += 1

print("Game over!")

ques 11
counter = 1
lucky_number = 7  # The correct lucky number
guessed_correctly = False

while counter <= 5:
    user_guess = int(input("Type in the {} number: ".format(counter)))

    if user_guess == lucky_number:
        print("Good guess!")
        guessed_correctly = True
        break
    else:
        print("Try again!")

    counter += 1

if guessed_correctly:
    print("Congratulations! You found the number!")
else:
    print("Sorry, but that was not very successful.")

print("Game over!")

'''










