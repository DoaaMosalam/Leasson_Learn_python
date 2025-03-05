
def maxNum(num1,num2,num3):
    if num1 >=num2 and num1 >=num3:
        print("Number 1 is the max number" + str(num1))
        return num1
    elif num2 >=num1 and num2 >=num3:
        print("Number 2 is the max number" + str(num2))
        return num2
    else:
        print("Number 3 is the max number" + str(num3))
        return num3
print("The max number is " + str(maxNum(10,20,30)))

#================================================================================================
