# my to do list 

print("nice to see you 😊")
print("make your to do list")
tasks=[]

def todo_list():
    print("\n ----TO-DO-LIST----")
    print("1. Add task")
    print("2. view task")
    print("3. mark as done ")
    print("4. Remove task")
    print("5. Exit")

    

while True:
        todo_list()
        choise = input("Enter you choise here:")

        if (choise ==1):
            todaydate = input("Enter todays date ")
            task= input("Enter your today task here :")


            todo={
            "todaydate":todaydate,
            "task":task,
        }
            tasks.append(todo)
            print("Your tasks are saved sucesfuly 😊")

        elif (choise ==2):
             print("your tasks ")

        elif (choise ==3) :
             print("mark as do")

        elif (choise ==4) :
             print("Remove task")
        elif (choise==5) :
             print("Exit")

        else:
             print("plese enter the valid statment")





