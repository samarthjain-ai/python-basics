# Expense Tracker Peoject 

Expenses= [] # list of all expenses in form of dictionary 
print("WELCOME TO EXPENSE TRACKER : Khrch Kam karo 😉 ")

while True:
    print("====MENU====")
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice= int(input("please Enter Your Choice Here :"))


#1. ADD EXPENSES 
    if(choice ==1):
        date= input("Enter The Expenses date : ")
        chtegory= input("Enter Where You Spend (Food , Treaval, Drinks, Stay ,Etc.):")
        Description= input("Enter For What You Spand (Trip , Party, Function , on your self):")
        amount= float(input("Enter the Amount :"))

        expense={
            "date":date,
            "category":chtegory,
            "Description":Description,
            "amount":amount
        }

        Expenses.append(expense)
        print( "\n done 😊 Expenses Add Succesfully")


#2. View All Expenses
    elif(choice ==2):
        if ( len(Expenses)==0 ):
            print("No Expenses Added")
        else:
            print("==== Your Expense ======")
            count=1
            for eachExpens in Expenses:
                print(f"Expense number{count} => {eachExpens["date"]}, {eachExpens["category"]},{eachExpens["Description"]},{eachExpens["amount"]}")
                count= count+1


#3. View Total Spending 
    elif(choice ==3):
        total=0
        for eachExpens in Expenses :
            total=total+eachExpens["amount"]

        print("\n total Expanses",total)



#4. Exit
    elif(choice == 4 ):
        print("thank you for using my system")
        break
    else:
        print("INVALID CHOICE,TRY AGAIN")








    
    



