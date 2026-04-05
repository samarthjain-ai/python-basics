
# function defination with parameter
def average(a=10,b=20):  # defolt value 
    averagevalue= (a+b)/2
    print(averagevalue)


# function calling with arguments

average(5,10)
average(7,10)
average(80,98)
average()

# 1 write a function show_age (name'age) that print: " samarth jainis 18 years old"

def show_age(name = "samarth jain",age = 18):
    print(f"{name} is {age} year old")

show_age()
show_age("subh",19)

# 2 cerate a function add_numbers (a,b) that print both the sum and difference 

def add_numbers (a=24,b=23):
    sum=a+b
    difference= a-b
    print(sum)
    print(difference)

add_numbers()

# 3 write a function fav_food(food) that , print "saumya didi loves <food>"

def fav_food(food = " chola bhatura "):
   print ("saumya didi loves ",food)

fav_food()