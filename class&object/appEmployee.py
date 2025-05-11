from Employee import Employee

emp1 = Employee("John", 30, "HR", False, 4000)
emp2 = Employee("Jane", 35, "Finance", True, 4500)


# print(emp1.name , emp1.age, emp1.departments, emp1.is_manager)
# print(emp2.name , emp2.age, emp2.departments, emp2.is_manager)
# print(emp1.name,emp2.name,emp1.departments, emp2.departments)

print(emp1.salary())

print(emp1.departments)
print(emp1.bonus())