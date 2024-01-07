from art import logo # Importing Logo from art.py


print(logo)

print("Welcome to the secret auction program.\n")

LoopTrue = False
completeList = []

while LoopTrue == False: # This part makes it, so you can loopp manytime <3

    def bidding(name,bid):
        bidList = []
        bidList = {
            "Name": name,
            "Bid" : bid
            }
        completeList.append(bidList)
        
########## Inputs
        
    name = input("What is your name? \n")
    bid = int(input("What is your bid?: \n"))

    bidding(name,bid)
    print(completeList)


########## Checking for all bidders
    otherS = input("Are there any other bidders? Type 'yes' or 'no' ! \n" )
    print(otherS)
    if otherS == "no":
        LoopTrue = True

###### Code for max bet checking
maxBet = max(completeList, key=lambda x: x['Bid'])
print(f"The Winner of the secret auction is : {maxBet['Name']} with a bet of {maxBet['Bet']}")







    