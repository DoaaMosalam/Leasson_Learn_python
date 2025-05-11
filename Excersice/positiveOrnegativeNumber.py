"""
Write a python program that prompts the user to input a number. The
program should then output this number and a message saying whether it
is positive, negative, or zero.
"""

def checkNumber():
    number = int(input("Enter a number: "))
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")
checkNumber()
print("================================================================================")
class NumberChecker:
    def __init__(self):
        self.number = 0


    def get_input(self):
        try:
            self.number = int(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            self.get_input()  # Ask again if input is not valid



    def check_number(self):
        if self.number > 0:
            return "positive"
            # print("The number is positive.")
        elif self.number < 0:
            return "negative"
            # print("The number is negative.")
        else:
            return "zero"
            # print("The number is zero.")

    def result(self):
        sign = self.check_number()
        print(f"your number is {self.number}.")
        print(f"\nThe number is {sign}.")
# Using the class
checker = NumberChecker()
checker.get_input()
checker.result()
