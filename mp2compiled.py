#imported libraries
import sys
import random
#global variables for calculator
global num1
global num2
#global variables for tempconverter
global celsius
global fahrenheit
#global variables for todolist
global task
global tasks
tasks=[] 
#global variables for number guessing game
global attempts
global random_integer
random_integer = random.randint(1, 100)
attempts=0
#global variables for student grade calculator
global scores
global n_subjects
global totalscores
n_subjects=0
scores=[]

#FUNCTIONS

#calculator part
def add(num1,num2):
    sumval=num1+num2
    print("The sum is:",sumval)
def subtract(num1,num2):
    difference=num1-num2
    print("The difference is:",difference)
def multiply(num1,num2):
    product=num1*num2
    print("The product is:",product)
def divide(num1,num2):
    quotient=num1/num2
    print("The quotient is:",quotient)

def calculator():
    while True:
        print ("--Calculator--")
        print("1. Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exit")
        caluserchoice= int(input("Enter your operation:"))
        if (caluserchoice>0) and (caluserchoice<=5):
            if caluserchoice==1:
                num1=int(input("Enter the first number:"))
                num2=int(input("Enter the second number:"))
                add(num1,num2)
                break
            elif caluserchoice==2:
                num1=int(input("Enter the first number:"))
                num2=int(input("Enter the second number:"))
                subtract(num1,num2)
                break
            elif caluserchoice==3:
                num1=int(input("Enter the first number:"))
                num2=int(input("Enter the second number:"))
                multiply(num1,num2)
                break
            elif caluserchoice==4:
                num1=int(input("Enter the first number:"))
                num2=int(input("Enter the second number:"))
                divide(num1,num2)
                break
            else:
                print("Exiting calculator")
                mainmenu()
                
        else:
            print("Invalid Input. Try Again")
            calculator()





#temperature converter part
def c_to_f(celsius): 
    fahrenheit= ((9/5)*celsius)+32
    print(celsius," Celsius is:", f"{fahrenheit:.2f}"," degrees Fahrenheit")
    
def f_to_c(fahrenheit):
    celsius=((fahrenheit-32)*(5/9))
    print(fahrenheit," Fahrenheit is:",f"{celsius:.2f}"," degrees Celsius" )

def tempconverter():
    print ("--Temperature Converter--")
    print("1. Convert Celsius to Fahrenheit")
    print("2.Convert Fahrenheit To Celsius")
    print("3.Exit")
    tcuserchoice= int(input("Enter your operation:"))

    if (tcuserchoice>0) and (tcuserchoice<=3):
        if tcuserchoice==1:
            celsius=int(input("Enter the Temperature in Celsius:"))
            c_to_f(celsius)
        elif tcuserchoice==2:
            fahrenheit=int(input("Enter the Temperature in Fahrenheit:"))
            f_to_c(fahrenheit)
        else:
            print("Exiting Temperature Converter")
            mainmenu()
            
    else:
        print("Invalid Input. Try Again")
        tempconverter()





#to do list codes
def add_task(task):
    tasks.append(task)
    print(task," added to the list")
    

def view_tasks():
    print("---To-Do List---")
    for i in range(len(tasks)):
        print(i+1,".",tasks[i])

def rem_task(remtaskchoice):
    removedtask=tasks.pop(remtaskchoice-1)
    print(removedtask," has been removed")

def todolist():
    while True:
        print ("-- To-Do List System --")
        print("1. Add a Task")
        print("2.Remove a Task")
        print("3.View Tasks")
        print("4.Exit")
        tdluserchoice= int(input("Enter your operation:"))
        if (tdluserchoice>0) and (tdluserchoice<=4):
            if tdluserchoice==1:
                task=input("Enter the task you want to add:")
                add_task(task)
                todolist()
                break
            elif tdluserchoice==2:
                view_tasks()
                remtaskchoice=int(input("Please choose which task to remove."))
                rem_task(remtaskchoice)
                todolist()
                break
            elif tdluserchoice==3:
                view_tasks()
                todolist()
                break
            else:
                print("Exiting To Do List System")
                mainmenu()
                
        else:
            print("Invalid Input. Try Again")
            todolist()





#number guessing game part
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
                mainmenu()
                
        else:
            print("Invalid Input. Try Again")
            numgame()





#student grade calculator part
def add_score():
    global n_subjects
    sub_name=input("Enter the subject:")
    sub_score=int(input("Enter the score:"))
    scores.append(sub_score)
    print("Score Added.")
    n_subjects+=1

    
def average():
    global n_subjects
    global totalscores
    totalscores=0
    for i in range(len(scores)):
        totalscores+=scores[i]
    finalaverage=totalscores/n_subjects
    print("Average Grade:",f"{finalaverage:.2f}")

def studentgradecalc():
    while True:
        print ("--Student Grade Calculator--")
        print("1.Add Score")
        print("2.Calculate Average")
        print("3.Exit")
        sgcuserchoice= int(input("Enter your operation:"))

        if (sgcuserchoice>0) and (sgcuserchoice<=3):
            if sgcuserchoice==1:
                add_score()
            elif sgcuserchoice==2:
                average()
            else:
                print("Exiting Student Grade Calculator")
                mainmenu()
        else:
            print("Invalid Input. Try Again")
            studentgradecalc()





#main menu for the system
def mainmenu():
    while True:
        print ("--Main Menu--")
        print("1. Calculator")
        print("2. Temperature Converter")
        print("3. To-Do List")
        print("4. Number Guessing Game")
        print("5. Student Grade Calculator")
        print("6. Exit")
        userchoice= int(input("Enter your operation:"))

        if (userchoice>0) and (userchoice<=6):
            if userchoice==1:
                calculator()
                break
            elif userchoice==2:
                tempconverter()
                break
            elif userchoice==3:
                todolist()
                break
            elif userchoice==4:
                numgame()
                break
            elif userchoice==5:
                studentgradecalc()
                break
            else:
                print("Exiting System")
                sys.exit()
                
        else:
            print("Invalid Input. Try Again")
            calculator()
            
mainmenu()