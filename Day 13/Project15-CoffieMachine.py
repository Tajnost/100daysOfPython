MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarters" : 0.25,
    "dimes" : 0.10,
    "nickles" : 0.05,
    "pennies" : 0.01,
}

# for r in resources:
#     try:
#         remaining = resources[r] - MENU["espresso"]["ingredients"][r]
#         if remaining > resources[r]:
#             print(f"{remaining}")
        
#     except:
#         ''



## espresso_cost = MENU["espresso"]["cost"]
## espresso_water = MENU["espresso"]["ingredients"]["water"]

remaining_resources = {}

def userChoice():
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    return choice
      
    

def response():
    calculate = 0
    print("Please insert coins")
    for z in coins:
        calculate += round(coins[z] * int(input(f"How many {z.title()}? ")),2)
    return calculate

def gameLogic(calculate, choice):
    
    if calculate >= MENU[choice]["cost"]:
        if calculate == MENU[choice]["cost"]:
            print(f"Here is your latter !! Enjoy !!")   
        else:
            returning = round(calculate - MENU[choice]["cost"],2)
            print(f"Here is your ${returning} in change")
            print(f"Here is your latter !! Enjoy !!")
    else:
        print(f"${calculate} is too little money.Money refunded.The price of the {choice} is ${MENU[choice]["cost"]}")
    
    #######====== User Input and OFF and REPORT choices =========#######
   


def gameplan():
    startOfmachine = False
    global resources
    while not startOfmachine:
        
        choice = userChoice()

        if choice == "report":
            for i in resources:
                print(f"{i.title()} : {resources[i]}")

        elif choice == "off":
            startOfmachine = True
        
        elif choice == "espresso" or "latte" or "cappuccino":      
            for r in resources:
                try:
                    if MENU[choice]["ingredients"][r] <= resources[r]:
                        resources[r] -= MENU[choice]["ingredients"][r]
                        print(resources[r])  
                    else:   
                        startOfmachine = True
                        print("Now enough resources")
                        break    
                except:
                    '' 

            else:    
                calculate = response()
                gameLogic(calculate,choice)

gameplan()






    #######==========================================================#######
    


