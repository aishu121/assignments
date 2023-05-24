'''
#ques1
def execute_code(code):
    try:
        exec(code)
    except SyntaxError:
        print("SyntaxError detected in the code.")

# Correct code
code1 = 'print("Hello, world!")'
execute_code(code1)

# Code with syntax error
code2 = 'print("Hello, world!"'
execute_code(code2)

#ques2
import sys

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"File {filename} not found. Please check the file name and try again.")
        return False
    return True

def main():
    while True:
        if len(sys.argv) != 2:
            print("Please provide a file name as a command-line argument.")
            sys.argv = [sys.argv[0], input("Enter file name: ")]
        else:
            if read_file(sys.argv[1]):
                break
            else:
                sys.argv = [sys.argv[0]]

if __name__ == "__main__":
    main()

#ques 3
def check_digits():
    num = input("Enter a four digit number: ")
    if len(num) != 4 or not num.isdigit():
        raise ValueError("The length is too short/long !!! Please provide only four digits")
    return num

try:
    number = check_digits()
    print(f"You entered {number}")
except ValueError as e:
    print(e)

#ques 4
class Login:
    def __init__(self):
        self.username = "admin"
        self.password = "password123"
        self.attempts = 0

    def ask_credentials(self):
        while self.attempts < 3:
            username = input("Enter username: ")
            password = input("Enter password: ")
            retype_password = input("Re-Type password: ")

            if username != self.username:
                print("Invalid username.")
                self.attempts += 1
            elif password != self.password or password != retype_password:
                print("Password incorrect or passwords do not match.")
                self.attempts += 1
            else:
                print("Login successful!")
                return
        print("Maximum attempts exceeded. Please try again later.")


login = Login()
login.ask_credentials()
'''