"""
Write a python program that will prompt the user to input a list of 5
integer values. Then it print their summation and average.
"""
# list = []
# summation = 0
# average = 0
# print("Enter 5 Integer Numbers of a list: ")
# for i in range(5):
#     values = input(f"Enter value of a list:{i+1} ")
#     list.append(values)
#     summation += int(values)
#     average = summation / 5
#
# print(list)
# print(f"The summation is {summation} and the average is {average}")

class CalculatorList:
    def __init__(self):
        self.list = []
        # self.sum = 0
        # self.average = 0





    def add_Values(self):
        print("Enter 5 Integer Numbers of a list: ")
        for i in range(5):
            values = int(input(f"Enter the value of {i+1}: "))
            self.list.append(values)
        #     self.sum += int(values)
        #     self.average = self.sum / 5
        #
        # print("Your list:", self.list)
        # print(f"The summation is {self.sum} and the average is {self.average}")

    def cal_sum(self):
        total = 0
        for num in self.list:
            total += num
        return total
    
    def cal_average(self):
        self.cal_sum()
        return self.cal_sum() / len(self.list)

    def display_results(self):
        print("Your list:", self.list)
        print(f"The summation is {self.cal_sum()} and the average is {self.cal_average()}")


lst = CalculatorList()
lst.add_Values()
lst.display_results()