import random

pickYourOption = input("Choose - Rock, Paper or Scissor").lower()

randomPick = random.randint(0,2)

if pickYourOption == "rock":
    if randomPick == 0:
        print("Its a Tie")
    elif randomPick == 1:
        print("You loose. Paper beats rock")
    else:
        print("You win")
elif pickYourOption == "paper":
    if randomPick == 0:
        print("You win!")
    elif randomPick == 1:
        print("Its a tie!")
    else:
        print("You loose!")
elif pickYourOption == "scissor":
    if randomPick == 1:
        print("You win!")
    elif randomPick == 2:
        print("Its a tie!")
    else:
        print("You loose!")
else:
    print("That is not a valid response!")