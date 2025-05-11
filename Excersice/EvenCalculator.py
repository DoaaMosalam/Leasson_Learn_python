"""
Write a python program that will prompt the user to input a list of 5
integer values. Then it print the summation and average of its contained
even numbers.
"""
class EvenCalculator:
    def __init__(self):
        self.list = []

    def add_values(self):
        print("Enter 5 Integer Numbers: ")
        for i in range(5):
            values = input(f"Value number is: {i+1} ")
            self.list.append(int(values))
        print(f"Values of the list: {self.list}")


    def sum(selfs):
        total=0
        for num in selfs.list:
            if num % 2 ==0:
                total += num
                return total


    def average(self):
        self.sum()
        average = self.sum()/len(self.list)
        return average


    def print_result(self):
        print(f"The sum of the even numbers is: {self.sum()}")
        print(f"The average of the even numbers is: {self.average()}")

cal_list = EvenCalculator()
cal_list.add_values()
cal_list.print_result()
