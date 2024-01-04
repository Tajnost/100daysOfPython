import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Tajno Password Generate \n")
print(len(letters))

questionLetters = int(input("How many letters would you like in your password? \n"))
questionSymbols = int(input("How many symbols would you like? \n"))
questionNumbers = int(input("How many numbers would you like? \n"))

password = ""

# Generats randoms letters
for i in range(questionLetters):
    randomLetter = random.randint(0,51)
    password += letters[randomLetter]

# Generats random Symbols
for y in range(questionSymbols):
    randomSymbols = random.randint(0,8)
    password += symbols[randomSymbols]

#Generats random Numbers
for z in range(questionNumbers):
    randomNumbers = random.randint(0,9)
    password += numbers[randomNumbers]

# Prints password
print("Here if your password generated:")
print(password + "\n")

print("Here if your same password shuffled around :")

# Converts password to a list, and then shuffels it and combines it back <3
stringPassword = list(password)
print(''.join(random.sample(stringPassword,len(stringPassword))))
