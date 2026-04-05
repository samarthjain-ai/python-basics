str1 = 'hello'
str2 ="subh"
str3 = '''python is fun'''

print(str1)
print(str2)
print(str3)

# string concatenation 
print(str1 +" "+ str2)

#length of string 
print( len(str3))

#indexing 

str = "samarth"
length = len(str)
print(str[0])  #s
print(str[5])  #t

print(length)

#slicing 

str4 = "subhjain"
firsthalf = str4[0:4]
trialfirsthalf = str4[ :4]
print(firsthalf)
print(trialfirsthalf)

secondhalf = str4[4:9]
print(secondhalf)

#negative indexing 






# Q
# take input and print middle3 charaters , last 2 character
str5= input("Enter the value herer :")
mid = len(str5)//2
output1 = str5[mid-1:mid+2]
print(output1)
output2= str5[-2:]
print(output2)

# string method
str6 = "good"
print(str6.upper())
print(str6.lower())
print(str.title())
print(str.replace("samarth","best"))
print(str2.count("a"))
#escape sequence
print("Hello world")
print("hello \n world")
print("Hello \t world")






