"""
Write a python program that print the values of a list.
"""
class ValueList:
    def __init__(self):
        self.list=[]

    def printValues(self):

        for lst in range(5):
            values = input("Enter value of a list: ")
            self.list.append(values)
        print(self.list)

valueList = ValueList()
valueList.printValues()