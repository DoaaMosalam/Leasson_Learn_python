
name = input("Enter your name: ")
department = input("Enter your department: ")
position = input("Enter your position: ")
salary = int(input("Enter your current salary: " ))

if department.lower() =="Software Engineer" and position.lower() =="Tester ":
    var = salary == salary + 5000
    print("Your salary is: ", salary)
elif department.lower() =="Software Engineer" and position.lower()=="Android ":
    var = salary == salary + 20000
    print("Your salary is: ", salary)
elif department.lower() =="Software Engineer" and position.lower()=="IOS ":
    var = salary == salary +10000
    print("Your salary is: ", salary)
elif department.lower() =="Sales" and position.lower()=="Sales Manager ":
    var = salary == salary +50000
    print("Your salary is: ", salary)
elif department.lower() =="Manger" and position.lower()=="Lead Manager":
    var = salary == salary +100000
    print("Your salary is: ", salary)
else:
    print("your department or position is not listed")

