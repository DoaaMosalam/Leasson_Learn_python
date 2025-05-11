"""
Write a python program that will prompt the user to input 5 integer values
to be stored in a list.
"""

class CreateList:
    def __init__(self):
        self.numbers = []

    def add(self):
        for i in range(5):
            numbers = input(f"Enter 5 integers numbers{i+1}")
            self.numbers.append(numbers)
        print(f"List of numbers is: {self.numbers}")



createList = CreateList()
createList.add()
