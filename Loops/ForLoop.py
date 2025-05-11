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
print("=======================================================")
# Zip
courses = ['CS500','DB500','CS521','CS503','CS523']
grade = [100,80,70,85,90]
for v_course,v_grade in zip(courses,grade):

        print(f"{v_course} is {v_grade}.")
print("=======================================================")

lst = [1,2,3,4,5]
# x = list(map(int,lst))
# print(x)
for i in lst:
    print(i)
print("=======================================================")

# create list taken item from user

list =[]
for i in range(3):
    list.append(input("Enter number: "))
    print(list[i])
print("=======================================================")
# List comprehensive
#    add value before for loop
x = [i**2 for i in range(11)]
print(x)

print("===========================================================")
x=[1, 2, 3, 4, 5]
new_list=[i*2 for i in x]
print(new_list)

















