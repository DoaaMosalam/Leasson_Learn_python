"""
Write a python program that will prompt the user to input a list of 5
integer values. Then it print its maximum and minimum values.
"""
class MaxMin:
    def __init__(self):
        self.list = []


    def CreateValue(self):
        print ("Enter the  5 Integers number of values: ")
        for i in range(5):
            self.list.append(int(input(f"Enter Value is number {i+1} ")))


    def max_min(self):
       if self.list[0] > self.list[1] and self.list[0] > self.list[2] and self.list[0] > self.list[3] and self.list[0]> self.list[4]:
           print(f"Number is maximum {self.list[0]}")
       elif self.list[1] > self.list[2] and self.list[1] > self.list[2] and self.list[1] > self.list[3] and self.list[1]> self.list[4]:
           print(f"Number is minimum {self.list[1]}")
       elif self.list[2] > self.list[0] and self.list[2] > self.list[1] and self.list[2] > self.list[3] and self.list[2] > self.list[4]:
           print(f"Number is maximum {self.list[2]}")
       elif self.list[3] >self.list[0] and self.list[3] > self.list[1] and self.list[3] > self.list[2] and self.list[3] > self.list[4]:
           print(f"Number is minimum {self.list[3]}")
       elif self.list[4]>self.list[0] and self.list[4] > self.list[1] and self.list[4]>self.list[2] and self.list[4]>self.list[3]:
           print(f"Number is maximum {self.list[4]}")
       else:
           print(" Number Two greater than Number two")


    def max(self):
        print(f"Number is Maximum is :{max(self.list)}")


    def min(self):
        print(f"Number is Minimum is : {min(self.list)}")


    def run(self):
        self.CreateValue()
        # self.max_min()

        self.max()
        self.min()





maximum = MaxMin()
maximum.run()