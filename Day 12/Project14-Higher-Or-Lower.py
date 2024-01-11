from game_data import data
from art import logo,vs
import random
import os

countDictionary = sum(1 for i in data if type(i) == dict)
randomDictionary = random.randint(0,countDictionary)


def clear(): # Function to clear the screen
    os.system('cls' if os.name=='nt' else 'clear')
clear()
print(logo)

# is A higher than B

def game():
    endlessLoop = False
    count = 0
    while not endlessLoop:
        a, b = random.sample(range(len(data)), 2)

        if a == b:
            endlessLoop = True
            game()
        print(f"Compare A: {data[a]["name"]}, {data[a]["description"]}, from {data[a]["country"]}")

        print(vs)

        print(f"Compare B: {data[b]["name"]}, {data[b]["description"]}, from {data[b]["country"]}")
        
        answer = input("Who has more followers? Type 'A' or 'B'?").lower()

        if answer == "a":
            if data[a]["follower_count"] > data[b]["follower_count"]:
                clear()
                print(logo)
                count +=1
                print(f"You are right! Current score: {count}")
            else:
                clear()
                print(logo)
                print(f"Sorry, that's wrong. Final score: {count}")
                endlessLoop = True
        else:
            if data[a]["follower_count"] < data[b]["follower_count"]:
                clear()
                print(logo)
                count +=1
                print(f"You are right! Current score: {count}")
            else:
                clear()
                print(logo)
                print(f"Sorry, that's wrong. Final score: {count}")
                endlessLoop = True
            

game()