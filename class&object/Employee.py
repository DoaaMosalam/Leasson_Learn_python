
class Employee:
    def __init__(self, name, age, deprtmanr, is_manager, salary):
        self.name = name
        self.age = age
        self.deprtmanr = deprtmanr
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
        if self.deprtmanr == "Manager":
            return self.salary * 0.20
        elif self.deprtmanr == "Senior":
            return self.salary * 0.15
        else:
            return self.salary * 0.10
