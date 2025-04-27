

convert_moth = {"Jan": "January",
                "Feb": "February",
                "Mar": "March",
                "Apr": "April",

}
print (convert_moth["Jan"])
print (convert_moth.get("Mar"))
print(convert_moth.get("mar")) #outpur is None

convert_arabic_month ={
    0 : "safer",
    1 : "Rabi al-awwal",
    2 : "Rabi al-thani",
    3 : "Jumada al-awwal",
}
print (convert_arabic_month[0])
print (convert_arabic_month.get(1))

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# Modifying Values in a Dictionary
print(f"The alien is {alien_0['color']}")
alien_0['color'] = 'yellow'
print(alien_0)
# remove item from dictionary
del alien_0['points']
print(alien_0)

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
print("All Favorite Language ara: ")
for key, value in favorite_languages.items():
    print(f"{key}: {value}")
language = favorite_languages['sarah'].title()
print(f"Language favorite sarah is:  {language}")
# Using get() to Access Values
'''
You’ll learn more about how to handle errors like this in general in
Chapter 10. For dictionaries specifically, you can use the get() method to set
a default value that will be returned if the requested key doesn’t exist.
The get() method requires a key as a first argument. 
'''
language_value = favorite_languages.get('point','No point value assigned.')
print(language_value)
# Looping Through All Key-Value Pairs
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
print(user_0)
for key, value in user_0.items():
    print(f"{key.title()}: {value.title()}")
# looping from value
for  value in user_0.values():
    print(f" {value.title()}")

#     A List of Dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
alien_list = [alien_0, alien_1, alien_2]
for item in alien_list:
    print(alien_list)
#     List in dictinary
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
for topping in pizza['toppings']:
    print(topping)
print(f"You ordered a {pizza['crust']}-crust pizza "
          "with the following toppings:")
