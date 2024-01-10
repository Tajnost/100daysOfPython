#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random
import os
from time import sleep

def clear(): # Function to clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

def guessingGame():
    clear()
    print(logo)
    computerRandom = random.randrange(1,100) # Takes a random number from 1-100 as a guess
    feed = ""
    counter = 0
    correct = False


    while not correct:
        guess = int(input("| >"))
        
        if computerRandom > guess:
            clear()
            feed = "Your number is too low! Guess again"
            counter +=1
            
        elif computerRandom < guess:
            clear()
            feed = "Your number is too high! Guess again"
            counter +=1 

        elif computerRandom == guess:
                 
            feed = "You guessed correctly!\n| YOU WON \n| YOU WON WOOHOOO"
            correct = True

### This is the entire logic 
        print(logo)           
        print(f"""| > {guess}
|                                           
| {feed}                                    
+-------------------------------------------+

+-------------+
|  Attempts:  |
|    [{counter}/10]   |
+-------------+
""")    
### A player has 10 lives, when it reaches 10, the player looses        
        if counter == 10:
            clear()
            print("GAME OVER !!!!!")
            print("GAME OVER !!!!!")
            print("GAME OVER !!!!!")
            sleep(3)
            correct = True

guessingGame()
sleep(3)
clear()
again1 = input("Do you want to play gain ? 'y' or 'n'").lower()
if again1 == "y":
    guessingGame()
else:
    clear()
    print("Goodbye")