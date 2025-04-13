
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
print(text.count("p")) # 2'

favorite_language = 'Hello, All Software Engineering. '
favorite_language += 'I am learning Python. '
print(favorite_language)

favorite_language.rstrip() # removes trailing whitespace
"""strip() remove space from after and before string"""
message = '    My name Jone, Welcome to python courses        '
print(message.strip())
""" Join """
jobs =["Android","Laravel","Node", "Web developer","IT"]
x = " - ".join(jobs)
print(x)
""

print(favorite_language)
#string index
word_phrase='be yourself'
print(word_phrase[0])

""" Negative Index"""
print(word_phrase[-1])
"""
specifying steps in slice Operation
"""
newsPapers= "new York times"
print(newsPapers[0:12:4])



