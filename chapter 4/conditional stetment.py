#conditional statements 
#1
marks = int(input("enter you marks :"))

if(marks >= 90):
    print("your gread is A")
elif(marks >=80):
    print("your gread is b")
elif(marks >=70):
    print("your gread is c")
elif(marks >=60):
    print("your gread is D")
else:
    print("your gread is F")

#2
age = int(input("Enter your age here :"))

if(age>=18):
    print("you are eligible to vote")
else:
    print("you are not elibible to vote")

#3
num = float(input("Enter your number here:"))

if(num >= 0):
    print("POSITIVE")
elif(num == 0 ):
    print("zero")
else:
    print("NEGATIVE")
