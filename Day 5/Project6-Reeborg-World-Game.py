#############
# This is a code for Reeborg World - Maze Challenge 
# The goal of this game was
# Reeborg was exploring a dark maze and the battery in its flashlight ran out.
#
#Write a program using an if/elif/else statement so Reeborg can find the exit.



def turn_right():
    turn_left()
    turn_left()
    turn_left()   

#### Edge Case Debug ###
while front_is_clear():
        move()
turn_left()


while at_goal() == False:

   if wall_in_front():
     if right_is_clear():
        turn_right()
        move()
     elif wall_on_right():
        turn_left()
   elif front_is_clear() and right_is_clear():
        turn_right()
        move()
   if front_is_clear() and right_is_clear():
        turn_right()
        move()
   elif front_is_clear() == True:
     move()
   
