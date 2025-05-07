import sys
import random

global attempts
global random_integer
random_integer = random.randint(1, 100)
attempts=0


def gameinner():
    global attempts
    userguess=int(input("Guess the number(1-100):"))
    if userguess == random_integer:
        print("")
    elif userguess > random_integer:
        print("Too high...guess lower!")
        attempts+=1
        gameinner()
    else:
        print("Too low...guess higher!")
        attempts+=1
        gameinner()

def game():
    print(random_integer)
    gameinner()




def numgame():
    while True:
        print ("--Number Guessing Game--")
        print("1. Play")
        print("5.Exit")
        gameuserchoice= int(input("Enter your operation:"))

        if (gameuserchoice>0) and (gameuserchoice<=2):
            if gameuserchoice==1:
                game()
                print("Congrats! You guessed the number in ",attempts," attempt(s)")
                break
            else:
                print("Exiting Number Guessing Game")
                sys.exit()
                
        else:
            print("Invalid Input. Try Again")
            numgame()

            
numgame()