################
# COIN FLIPP  #
################

import random
HeadOrTail = random.randint(0,1)

if HeadOrTail == 1:
  result = "Heads"
else:
  result = "Tails"

print(result)


#################
# RANDOM BANKER #
#################


#Angela, Ben, Jenny, Michael, Chloe
names_string = 0
names = names_string.split(", ")
import random

x = random.choice(names)

print(f"{x} is going to buy the meal today!")

####### or ######### 

names = names_string.split(", ")

import random

# Get the total number of items in list.
num_items = len(names)
# Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, num_items - 1)
# Choose and print a random name.
print(names[random_choice]) 


#########################
#    TREASURE HUNTER    #
#########################

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
positionArray = position.split()

if positionArray[0][0] == "A":
  if positionArray[0][1] == "1":
    line1[0] = "X"
  elif positionArray[0][1] == "2":
    line2[0] = "X"
  else:
    line3[0] = "X"
elif positionArray[0][0] == "B":
  if positionArray[0][1] == "1":
    line1[1] = "X"
  elif positionArray[0][1] == "2":
    line2[1] = "X"
  else:
    line3[1] = "X"
else:
  if positionArray[0][1] == "1":
    line1[2] = "X"
  elif positionArray[0][1] == "2":
    line2[2] = "X"
  else:
    line3[2] = "X"
    


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")


