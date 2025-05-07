import sys
global task
global tasks
tasks=[] 

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
                sys.exit()
                
        else:
            print("Invalid Input. Try Again")
            todolist()
            
todolist()