
text = "opportunity"

print(text)
print(text[0])     # o

print(text + " learning software engineering")  # opportunity learning software engineering

print(text +"\n" + "learning software engineering")
print(text + "\t" + "learning software engineering")  # opportunity    learning software engineering
print(text + "\b" + "learning software engineering")  # opportunitylearning software engineering
print(text.find("p")) # 1

print(text.index("p")) # 1
print(text.lower()) # opportunity
print(text.upper()) # OPPORTUNITY
print(text.islower()) # True
print(text.isupper()) # False
print(text.upper().isupper())
print(text.split("p")) # ['o', '', ortunity']
print(text.replace("p", "P")) # oPPortunity
print(text.startswith("o")) # True
print(text.endswith("y")) # True
print(text.count("p")) # 2


