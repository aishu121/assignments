'''
#ques 1
import math

C = 50
H = 30

def calculate_value(d):
    result = math.sqrt((2 * C * d) / H)
    return result

# Accept input values for D as comma-separated sequence
input_sequence = input("Enter the values of D (comma-separated sequence): ")

# Split the input sequence and convert values to integers
values = input_sequence.split(",")
d_values = [int(value) for value in values]

# Calculate and print the values according to the formula
for d in d_values:
    q = calculate_value(d)
    print(f"For D = {d}, Q = {q}")

#ques 2
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


# Create an instance of the Square class
square = Square(5)

# Call the area function for the Square instance
square_area = square.area()

# Call the area function for the Shape instance
shape = Shape()
shape_area = shape.area()

# Print the areas
print("Square area:", square_area)
print("Shape area:", shape_area)

#ques 3
class SumToZeroFinder:
    def __init__(self, arr):
        self.arr = arr

    def find_three_elements(self):
        result = []
        n = len(self.arr)

        # Sort the array in ascending order
        self.arr.sort()

        for i in range(n-2):
            # Fix the first element as arr[i]
            left = i + 1
            right = n - 1

            while left < right:
                current_sum = self.arr[i] + self.arr[left] + self.arr[right]

                if current_sum == 0:
                    result.append([self.arr[i], self.arr[left], self.arr[right]])

                    # Move both pointers to find other solutions
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result


# Input array
input_array = [-25, -10, -7, -3, 2, 4, 8, 10]

# Create an instance of SumToZeroFinder
finder = SumToZeroFinder(input_array)

# Find three elements that sum to zero
result = finder.find_three_elements()

# Print the result
print(result)

#ques4
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other):
        total_minutes = self.hours * 60 + self.minutes + other.hours * 60 + other.minutes
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return Time(hours, minutes)

    def displayTime(self):
        print(f"{self.hours} hr {self.minutes} min")

    def displayMinute(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"{total_minutes} minute")


# Create Time objects
time1 = Time(2, 50)
time2 = Time(1, 20)

# Add two Time objects
result = time1.addTime(time2)

# Display the added time
result.displayTime()

# Display the total minutes
result.displayMinute()
'''
#ques 5
class Person:
    def __init__(self, initial_age):
        if initial_age >= 0:
            self.age = initial_age
        else:
            self.age = 0
            print("Age is not valid, setting age to 0")

    def yearPasses(self, num_years):
        self.age += num_years

    def amIOld(self):
        if self.age < 13:
            print("You are young")
        elif 13 <= self.age <= 19:
            print("You are a teenager")
        else:
            print("You are old")


# Create instances of the Person class
person1 = Person(-1)
person2 = Person(4)
person3 = Person(10)
person4 = Person(16)
person5 = Person(18)
person6 = Person(64)
person7 = Person(38)

# Call amIOld method for each instance
person1.amIOld()
person2.amIOld()
person3.amIOld()
person4.amIOld()
person5.amIOld()
person6.amIOld()
person7.amIOld()
