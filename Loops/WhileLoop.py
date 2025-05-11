i = 1
while i <=10:
    print(i)
    i +=1


# n = input("Enter an Integer number: ")
#
# i, sumN = 1,0
#      #condition
# while i< n+1:
#     sumN += i
#     print(f"The summation of{n} is {sumN} and average is {sumN/n}")
print("**********************************************************************")

Cars={
    "BMW":10000000,
    "Ferreri":30000000,
    "Toyota":20000000,
    "Chevrolet":1500000,
    "Suzuki": 1900000
}

found = False

while not found:

    car_name = input("من فضلك ادخل اسم العربية: ").strip()

    for name, price in Cars.items():
        if name == car_name:
            print(f"سعر {name} هو {price} جنيه.")
            found = True
            break

    if not found:
        print("العربية غير موجودة، حاول مرة أخرى.")
