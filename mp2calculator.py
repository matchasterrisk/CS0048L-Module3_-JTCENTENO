import sys
global num1
global num2
global userchoice

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
            if caluserchoiceuserchoice==1:
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
                sys.exit()
                
        else:
            print("Invalid Input. Try Again")
            calculator()
            
calculator()