from art import logo
from os import system, name
from time import sleep

print(logo)
print("Welcome to the Calculator Application!\n")

KeepLoop = False

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def operations(number1, input1, number2):
    if input1 == '+':
        return number1 + number2
    elif input1 == '-':
        return number1 - number2
    elif input1 == '*':
        return number1 * number2
    elif input1 == '/':
        return number1 / number2
    else:
        print("Invalid operation.")
        return None
    



def game():
        count = 0       
        try:
            number1 = int((input("What is your first number?\n")))
            input1 = input("Pick an operation - + * /:\n")
            number2 = int((input("What is your next number?\n")))

            result = operations(number1, input1, number2)
            count += result
            print(f"Your current result is : {count}")

            
            KeepLoo2 = False
            while not KeepLoo2:
                gameAgain = input(f"""Type 'y" to continue calculating with {count}, type 'n' to start a new calcuation, or type 'end' to stop""").lower()
                if gameAgain == 'y':
                    input2 = input("Pick an operation - + * /:\n")
                    number3 = int((input("What is your next number?\n")))
                    count += operations(count, input2, number3)
                    print(f"Your current result is : {count}")

                elif gameAgain =='n':
                    print(f"Your current result is : {count}")
                    sleep(3)
                    count = 0
                    clear()
                    KeepLoo2 = True
                    game()
                else:
                    KeepLoo2 = True
                    print(f"Your current result is : {count}")
                    break
            
        except ValueError:
            print('You entered a non integer value, try again.')
        except ZeroDivisionError:
            print("You cannot diving by zero, try again")

game()


            

