# 

food={"paneer","chole bathura","mango"}
print(type(food))
print(food)
food.add("kunafa")
food.remove("chole bathura")
print(food)

empty= set()
print(type(empty))


# question 
# you are given a list of programming languages:
# ["python","java","c++","python","java","c"]
# convert it into a set and print how many unique languages divya knows

programminglist =  ["python","java","c++","python","java","c"]

# how to convert a list into set 

programmingset = set(programminglist)
print(type(programminglist))
print(type(programmingset))
print("divya knows these many langvges",len(programmingset))