#######
### This is just a attempt, to get familiar with Turtle Library
########


import turtle as t
from random import randint,random

turtle = t.Turtle()
turtle.shape("turtle")
turtle.color("red")
turtle.home()
turtle.position()
screen = t.Screen()
screen.setup(width=800, height=620)
screen.bgcolor("white")
screen.title("Turtle Window")
t.colormode(255)
#### Moves turtle in a square ####

#for _ in range(0,4):
#    turtle.forward(100)
#    turtle.right(90)

#### Move Turtle into a dotted line ####
#for i in range(50):
#    turtle.pendown()
#    turtle.forward(10)
#    turtle.penup()
#    turtle.forward(10)

### Draws a stuff
#count = 3
#while True:
#    if count < 11:
#        for _ in range(count):
#            print(count)
#            rotate = 360 / count
#            turtle.forward(100)
#            turtle.right(rotate)
#        count += 1
#        turtle.color(randint(0, 255), 
#        randint(0, 255), 
#        randint(0, 255)) 
#    else:
#        False

# Random Walk
#### Move Turtle into a dotted line ####

# while True:
#     turtle.pensize(3)
#     turtle.speed(50)
#     turtle.color(randint(0, 255), 
#         randint(0, 255), 
#         randint(0, 255)) 
#     turtle.forward(10)
#     turtle.setheading(90*randint(1,3))


####### Random Circle - Spirograph

turtle.speed(50)
y = 0 # or # current.heading = turtle.heading()
z = 0
while z != 1:
    y += 2
    z = int(360/y)

    turtle.pensize(2)
    turtle.circle(100)
    turtle.right(4) # or # turtle.setheading(current_heading + 10)
    turtle.color(randint(0, 255), 
    randint(0, 255), 
    randint(0, 255)) 

    


screen = t.mainloop()


### Bottom
#screen = Screen() ## Initialize Screen class
#screen.setup (width=0.9, height=0.9)
#screen.exitonclick() ## Screen stays until it is clicked on