# question 1 

i=1

while (i<=10):
    print(i)
    i+=1

print(" questin 1 is complet😊")
# question 2

j=10

while(j>=1):
    print(j)
    j-=1
    print("j =",j)

print("question 2 is complet😊😊")

# 3 write a progam to print all even number betwee 1 to 50 
#using a while loop 

num = 1

while(num<=50):
    if (num%2 == 0 ):
        print(num)
    num +=1

print("question 3 end here 😊😊😊")


# 4 write a program that print the sum of first n natural number.
# for example , if n = 5 , then output should be 1+2+3+4+5=15

n=int(input("enter a number :"))
sum = 0

while (n>=1):
    sum= (sum+n)
    n-=1
    
print("sum",sum)
print("n=",n)

# writhe a program to print this patten using while loop
#*
#**
#***
#****
#*****

n= 1

while(n<=5):
    print("*"*n)
    n+=1

print("we are out of the while loop,😊😊😊😊")



# 6 subh went to print his name 5 times ,but each time with a 
# number in front of it . write a program using a while loop that prints :
# 1 subh
#2 subh and ...


n=1

while(n<=5):
    print(n,"subh") 
    n+=1

print("Q6 end here😊😊😊😊😊😊")


# Q7 write aprogram to print the mutiplcation table of any number using a while
#loop

n = int(input("Enter a number here :"))
i =1 
while i<=10:
    print(f"{n} ❌ {i} = {n*i}")
    i+=1

print("Question 7 end here ")

# 8 write a program using for and range ()to print all even numbers between 1 and 20 

for num in range(2,20,2):
    print(num)

print("Question 8 end here ")


# 9 write a program to print numbers from 1 to 50 but print "samarth jain"
# instead of numbers that are multiple of 5 

for i in range(1,50,1):
    if (i%5 ==0):
        print("samarth jain")
    else:
        print(i)

print(i)

print("Question 9 and here ")


# 10 write z program  that print  the squre odf  each number from 1 to  10 using a for loop.

for i in range(1,12,1):
    print(i*i)
    i+=1

print("Question 10  end here ")

#11 write a program that  print all numbers from 100 to 1 using for and range 

for i in range (101,0,-1):
    print(i)
   

print("\nQuestion 11 end here " )



#12 user what to print his name five time but in uppercase 

name = input("Enter you name here :")

for item in range(5) :
    print(name.upper())



print("Question 12 end here ")

#13 you are given a list of food items . writte a program to print each food item using a for loop 

food= ["mango","apple","chola bahura "]
for item in range(1):
    print(food)


print("Question 13 end here ")



