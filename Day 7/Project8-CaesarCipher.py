print(
'''        
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88   \n'''        
)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

goAgain = False




def goGo():
        
      ### Asking Users
      direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
      text = input("Type your message:\n").lower()
      shift = int(input("Type the shift number:\n"))
      password = "" # Defining password for later

      if direction == "encode": ## Entire Encoded function
        for i in text:  ## Checks each cractacter in string
          if i in alphabet: ## Compares and checks is i character i in alphabet, and if same
            x = alphabet.index(i) + shift ## This is the logic for coding, it checks the alphabet index of i, and then shifts it by the amount inputed 
            password += alphabet[x] ## appends the shifted amount
          else:
            password += i 
        print(f"This is your text:\n{password}")     
      elif direction == "decode":
        for i in text:  
          if i in alphabet:
            x = alphabet.index(i) - shift
            password += alphabet[x]
          else:
            password += i
        print(f"This is your text:\n{password}")          
      else:
        print("You chose poorly") 

### While loop that checks if we wanna go again or not ###      
while goAgain == False:
  goGo()   
  askAgain = input("Do you want to go again? Yes or No \n").lower()
  if askAgain == "no":
    goAgain = True
    
