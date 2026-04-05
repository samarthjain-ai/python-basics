# list in python 

food = ["chole bathure","mango","apple","gulab jamun"]
print(len(food))

print("first value of the list:",food[0])
print("third value of the list:",food[3])


#indexing

masks = [ 99,87,8,67,88]
print(masks)

masks[1]=100
print(masks)


#slicing
print(masks[1:3])

print(max(masks))
print(min(masks))
masks.append(92)
print(masks)
masks.sort()
print(masks)
masks.pop(1)
print(masks)
masks.remove(100)
print(masks)
masks.insert(1,275)
print(masks)










# tahe 3 food and store in list,print list and length
food1 = input("Enter you food 1 :")
food2 = input("Enter you food 2 :")
food3 = input("Enter you food 3 :")

foodlist= []
foodlist.append(food1)
foodlist.append(food2)
foodlist.append(food3)

print(foodlist)