##############################
# Simple Rollercoaster check #
##############################

print("Welcome to the rollercoaster!")
bill = 0
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Midlife crysis, you pay 0!")
    else:
        bill = 12
        print("Please pay $12.")


    photo = input("Do you want a photo taken? Y or N.")
    if photo == "Y":
       bill += 3
       print(f"Your bill is {bill} ")
    else:
       print(f"Pay {bill}")
       
       

else:
    print("Haha, too short!")

  



##############################
#       BMI calculator       #
##############################

# Enter your height in meters e.g., 1.55
height = float(input())

# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

bmi = int(weight) / float(height) ** 2


#Write your code below this line 👇

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")



###########################
#       LEAP YEAR         #
###########################
  
# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

leapYear = year % 4
leapYear1 = year % 100
leapYear2 = year % 400

if leapYear == 0:
  if leapYear1 == 0:
    if leapYear2 == 0:      
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")


  ########################
  #    Pizza ordering    #
  ########################

  print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

price = 0

if size == "S":
  price = 15
elif size == "M":
  price = 20 
else:
  price = 25

if add_pepperoni == "Y":
  if size == "S":
    price += 2
  else:
    price += 3
  

if extra_cheese == "Y":
  price +=1
print(f"Your final bill is: ${price}.")


#########################
#     LOVE CALCULATOR   #
#########################

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇


#### Convert all to upperletters
name3 = name1.upper() + name2.upper()

#### Count = TRUE
#### COunt 1 = LOVE
count1 = 0
count2 = 0

for x in 'TRUE':
  count1 += name3.count(x)

for y in 'LOVE':
  count2 += name3.count(y)

tL = int(str(count1) + str(count2))

if tL < 10 or tL > 90:
  print(f"Your score is {tL}, you go together like coke and mentos.")
elif tL > 40 and tL < 50:
  print(f"Your score is {tL}, you are alright together.")
else:
  print(f"Your score is {tL}.")