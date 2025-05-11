

class Students:
    def __init__(self,id,first_name,last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name


    def InfoStudent(self):
        print("Enter your details: ")
        self.id = int(input("Enter your ID: "))
        self.first_name = input("Enter your first name: ")
        self.last_name = input("Enter your last name: ")
        print(f"Your full name is: {self.first_name} {self.last_name}\n Your ID: {self.id} ")





