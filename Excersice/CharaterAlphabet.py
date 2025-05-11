"""
Question 3:
Write a python program to input a character from user and check whether
the given character is alphabet, digit or special character.
"""

def check_character_type():
  char = input("Enter a character: ")
  if char.isalpha():
      print(f"{char} is alphabet.")
  elif char.isdigit():
      print(f"{char} is digit.")
  else:
      print(f"{char} is special character.")

check_character_type()