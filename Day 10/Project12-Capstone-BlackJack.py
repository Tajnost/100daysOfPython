import random
from art import logo

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

### Game Logic

# Complete list of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def game():
    print(logo)
    startGame = input("Do you want to play blackjack? 'y' or 'n'")
    answerComputer = 0
    answerPlayer = 0
    card5 = ''

        #### First Hand ####
    if startGame == 'y':

        ### Selection two random cards fr player
        card1 = random.choice(cards)
        card2 = random.choice(cards)
        answerPlayer += sum([card1,card2])


        print (f"Your card is [{card1}, {card2}], current score: {answerPlayer}")

        ### Selecting two random cards for computer
        card3 = random.choice(cards)
        card4 = random.choice(cards)
        answerComputer = sum([card3,card4])
        print (f"Computer's first card: {card3}")

        ### Game logic - to ask a player if he wants to hit or stay
        
        EndHitting = True 
        while EndHitting == True:
            
            askingHit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if askingHit == "y":
                card5 = random.choice(cards)
                answerPlayer += card5
                if card5 == 11:
                    if answerPlayer > 21:
                        answerPlayer -= 10
                print (f"Your card is [{card1}, {card2}, {card5}], current score: {answerPlayer}")
                if answerPlayer > 21:
                    print(f"You loose, computer wins")
                    EndHitting = False
                    return
                
            elif askingHit == "n":
                print(f"Your final hand: [{card1}, {card2}, {card5}], final score: {answerPlayer}")
                if answerPlayer > answerComputer and answerComputer < 18:
                    card6 = random.choice(cards)
                    answerComputer += card6
                    if card6 == 11:
                        if answerComputer > 21:
                            answerComputer -= 10
                    if answerComputer > 21:
                        print(f"Computer final hand: [{card2}, {card3}, {card6}] final score: {answerComputer}")
                        print("Player Wins!")
                        EndHitting = False
                else:
                    print(f"Computer final hand: [{card2}, {card3}] final score: {answerComputer}")
                    if answerComputer > answerPlayer and answerComputer <= 21:
                        print("Computer Wins")
                        EndHitting = False
                    else:
                        print("Player Wins")
                        EndHitting = False
                

game()

    



