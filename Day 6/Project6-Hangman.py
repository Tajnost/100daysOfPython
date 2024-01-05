#######################################
# Pick a random word and check answer #
#######################################
import random
from time import sleep

word_list = ["ardvark", "baboon", "camel"]
#Izbere Random Besedo
randomList = random.choice(word_list)
dolzina = len(randomList)
print(randomList)

# Izpiše črtice
crtice = ""
for i in randomList:
    crtice += "_"
print(crtice)

crtica2 = ""
ugotovljeno = False
zivljenje = 6

while ugotovljeno != True:

    guess = input("Guess a letter\n").lower()

    if guess in randomList:
        crtica2 = ""
        for stetje in range(dolzina):
            if randomList[stetje] == guess:
                crtica2 += guess
            else:
                crtica2 += crtice[stetje]  
        crtice = crtica2
        print(crtice)
    else:
        zivljenje -= 1 
        print(f"Narobe zgubili ste zivljenje. Imate še {zivljenje} zivljenj!")
        print(crtice)
        if zivljenje == 5:
            print(" O ")
            print("/|\\")
            print("/ \\")
        elif zivljenje == 4:
            print(" O ")
            print("/|\\")
            print("/ ")
        elif zivljenje == 3:
            print(" O ")
            print("/|\\")
            print("  ")
        elif zivljenje == 2:
            print(" O ")
            print("/|")
            print("  ")
        elif zivljenje == 1:
            print(" O ")
            print(" |")
            print("  ")



if "_" not in crtice or zivljenje == 0:
    ugotovljeno = True

print("Game Over")