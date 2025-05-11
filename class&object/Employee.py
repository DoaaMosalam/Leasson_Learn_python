
class Employee:
    def __init__(self, name, age, departments, is_manager, salary):
        self.name = name
        self.age = age
        self.departments = departments
        self.is_manager = is_manager
        self.salary = salary

    def  salary(self):
            if self.salary >=4200:
                return  "Manager"
            elif self.salary >= 3800:
                return "Senior"
            else:
                return "Junior"

    def bonus(self):
        if self.departments == "Manager":
            return self.salary * 0.20
        elif self.departments == "Senior":
            return self.salary * 0.15
        else:
            return self.salary * 0.10
