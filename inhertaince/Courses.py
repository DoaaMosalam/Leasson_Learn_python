
from Students import Students
# degree own about level study

class Courses(Students):
    COURSE_LEVELS = {
        1:["CS500","OR500","DB500","AS500","MS500"],
        2:["CS503" , "MS521" , "CS504" , "IT500" , "CS522"],
        3:["MS506","CS507","MS505","CS510","CS209"],
        4:["CS100","CS200","CS300","CS300","CS400","CS500"]
    }
    def __init__(self, id, first_name, last_name):
        super().__init__(id, first_name, last_name)
        self.level = None
        self.grade = {}

    def choose_level_and_enter_grades(self):
        self.level = int(input("Enter your level (1 or 2): "))

        if self.level not in self.COURSE_LEVELS:
            print("Invalid level.")
            return
        subjects = self.COURSE_LEVELS[self.level]
        print(f"Courses for level {self.level}: {', '.join(subjects)}")
        total = 0
        for level in self.COURSE_LEVELS[self.level]:
            while True:
                try:
                    grade = float(input(f"Enter your grade for {level}: "))
                    if 0<= grade <= 100:
                        self.grade[level] = grade
                        total += grade
                        break
                    else:
                        print("Grade must be between 0 and 100.")
                except ValueError:

                    print("Please enter valid number.")

                continue
        self.gpa = total / len(self.COURSE_LEVELS[self.level])
    # =====================================================================================================
    def calculate_gpa(self):
        for subjects, grade in self.grade.items():
            print(f"  {subjects}: {grade}")

        print(f"Average GPA: {self.gpa:.2f}")

        if self.gpa >= 95:
            print("Congratulation, Your GPA is A+")
        elif self.gpa >= 90:
            print("Congratulation,Your GPA is A")
        elif self.gpa >= 80:
            print("Congratulation,Your GPA is B+")
        elif self.gpa >= 70:
            print("Congratulation, Your GPA is B")
        elif self.gpa >= 60:
            print("Your GPA is C")
        else:
            print("You Failed")



    def display(self):
        self.InfoStudent()
        self.choose_level_and_enter_grades()
        self.calculate_gpa()


courses = Courses(13123,"","")
courses.display()




            
       
        