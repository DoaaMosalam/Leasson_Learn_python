fruits= ["banana", "apple", "orange", "strawberry", "watermelon"]

for i in fruits:
    print(i)
print("=======================================================")

for i in range(len(fruits)):
    print(i)
print("=======================================================")

for i in range(1,4):
    print(i)
print("=======================================================")
# write program take from username car and print price
Cars={
    "BMW":10000000,
    "Ferreri":30000000,
    "Toyota":20000000,
    "Chevrolet":1500000,
    "Suzuki": 1900000
}
found = False
cars_name = input("Enter name car: ")

for name,price in Cars.items():
    if name == cars_name:
        print(f"{cars_name} has a price of {price}")
        found = True
        break
if not found:
    print(f"{cars_name} does not have found")










