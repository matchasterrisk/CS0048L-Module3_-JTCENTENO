import sys

global scores
global n_subjects
global totalscores
n_subjects=0
scores=[]

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
                sys.exit()
                
        else:
            print("Invalid Input. Try Again")
            studentgradecalc()

            
studentgradecalc()