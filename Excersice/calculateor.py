import operator


# def calculator_mean_median():
#         """This method calculates the mean and median of a given dataset."""
#         print("hi")
#         print(calculator_mean_median.__doc__)
#
# calculator_mean_median()

numOne =  float(input("Enter the first number: "))
operator = input("Enter the operator: ")
numTwo = float(input("Enter the second number: "))

if operator == "+":
    print("Addition of two numbers is: ", numOne + numTwo)
elif operator == "-" and numOne >=0 and numOne > numTwo:
    print("Subtraction of two numbers is: ", numOne - numTwo)
elif operator == "-" and numOne >=0 and numOne< numTwo:
    print("Subtraction of two numbers is:  ", numOne - numTwo)
elif operator == "-" and numTwo == 0:
    print("The number don't division on zero.")
elif operator == "*" and numOne * numTwo:
    print("Multiplication of two numbers is: ", numOne * numTwo)
elif operator == "/" and numTwo !=0:
    print("Division of two numbers is: ", numOne / numTwo)






"""class calculator:
    numOne =  float(input("Enter the first number: "))
    operator = input("Enter the operator: ")
    numTwo = float(input("Enter the second number: "))

    def add(operator):
        if operator.numOne + operator.numTwo:
            print("Addition of two numbers is: ", operator.numOne+ operator.numTwo)
            return  operator.numOne + operator.numTwo



def sub(operator):
 if operator.numOne >=0 and operator.numOne > operator.numTwo:
    print("Subtraction of two numbers is: ", operator.numOne - operator.numTwo)
    return operator.numOne - operator.numTwo
 elif operator.numOne >=0 and operator.numOne< operator.numTwo:
     print("Subtraction of two numbers is:  ", operator.numOne - operator.numTwo)
     return -1 * (operator.numOne - operator.numTwo)
 elif operator.numTwo == 0:
     print("The number don't division on zero.")
     return 0
 else:
     print("Invalid input")



def multiply(operator):
    if operator.numOne * operator.numTwo:
        print("Multiplication of two numbers is: ", operator.numOne * operator.numTwo)
        return operator.numOne * operator.numTwo


def divide(opertor):
    if opertor.numTwo !=0:
        print("Division of two numbers is: ", operator.numOne / operator.numTwo)
        return operator.numOne / operator.numTwo

def mod(operator):
    if operator.numOne % operator.numTwo:
        print("Modulus of two numbers is: ", operator.numOne % operator.numTwo)
        return operator.numOne % operator.numTwo


def result():
    if calculator.operator == "+":
        print(calculator.add(calculator))
    elif calculator.operator == "-":
        print(calculator.sub(calculator))
    elif calculator.operator == "*":
        print(calculator.multiply(calculator))
    elif calculator.operator == "/":
        print(calculator.divide(calculator))
    elif calculator.operator == "%":
        print(calculator.mod(calculator))"""












