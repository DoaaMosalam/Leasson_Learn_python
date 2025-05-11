"""
Write a python program of a four-function calculator. The program
should ask the user to enter a number, an operator, and another number. It
should then carry out the specified arithmetical operation: adding,
subtracting, multiplying, or dividing the two numbers.
"""


class Calculator:
    def __init__(self):
        self.operators = ['+', '-', '*', '/']
        self.number = 0

    def calc(self):
        while True:
            num1 = input("Enter a number one: ")
            oper = input("Enter an operator: ")
            num2 = input("Enter a number two: ")
            if oper == "+":
                print(f"{num1} + {num2} = {float(num1) + float(num2)}")
            elif oper == '-':
               print(f"{num1} - {num2} = {float(num1) - float(num2)}")
            elif oper == '*':
               print(f"{num1} * {num2} = {float(num1) * float(num2)}")
            elif oper == '/':
               print(f"{num1} / {num2} = {float(num1) / float(num2)}")
            else:
                print(f"{num1} != {num2}")

calculator = Calculator()
calculator.calc()
