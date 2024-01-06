### Function Simple
def greet():
    print("Hello")
    print("Hello2")
    print("Hello3")

greet()


### Function that allows for input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")


greet_with_name("Vid")

### Function, with more than one Input

def greet_with_name(name, name2="Jack"):
    print(f"Hello {name}")
    print(f"How do you do {name2}")


greet_with_name("Vid")

### Calling function with switched ids ( Order does not matter)

greet_with_name(name2="Vid",name="Hello")



#############
# Auditorium - Paint Area Calculator
####################################


# Write your code below this line 👇
import math

def paint_calc(height,width,cover):
  cans = str(math.ceil((height * width) / cover))
  print(f"You'll need {cans} cans of paint.")
  


# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
