"""
Write a python program to input an alphabet and check whether it is
vowel or consonant.
Note: Vowel alphabets are: {a, e, o, u, i}
All other alphabets are consonant
"""

class Alphabet:
    def vowel_consonant(self):
        alphabet = ['a','e','i','o','u']
        alpha = input('Enter alphabet:  ')
        for letter in alpha.lower() or alpha.upper():
            if letter in alphabet:
                print("letter is Vowel")
            else:
                print("letter is consonant")


alphabet = Alphabet()
print(alphabet.vowel_consonant())

