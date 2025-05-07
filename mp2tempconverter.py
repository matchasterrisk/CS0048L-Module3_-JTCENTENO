import sys

global celsius
global fahrenheit

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
            sys.exit()
            
    else:
        print("Invalid Input. Try Again")
        tempconverter()

tempconverter()