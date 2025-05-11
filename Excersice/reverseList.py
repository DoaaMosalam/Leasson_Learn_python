"""
Write a python program that print the values of a list in a reverse order
"""

class ReverseList:
    def __init__(self):
        self.list = []

    def print_reversedList(self):
        self.list = ["A", "B", "C", "D", "E", "F"]
        r = self.list[::-1]
        print(f"Reversed List is: {r}")


reverseList = ReverseList()
reverseList.print_reversedList()





