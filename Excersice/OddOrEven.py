"""
Write a python program that prompts the user to input a number. The
program should then output this number and a message saying whether
it is even or odd.
"""
class OddOrEven:
    def odd_or_even(self):
        number =float(input("Enter Your number:  "))
        if number % 2 == 0:
            print("Number is Even")
        else:
            print("Number is Odd")


odd_or_even = OddOrEven()
print(odd_or_even.odd_or_even())