#with keyword 

file = open("report.text","r")
data= file.read()
file.close()

with open("report.txt","r") as d:
    data= d.read()
    print("file data",data)

with open("newtext.txt","r") as f:
    line1= f.readline()
    line2= f.readline()
    line3= f.readline()
    line4= f.readline()
    data=f.read
    print("line1: ",line1)
    print("line2",line2)
    print("line3",line3)
    print("line4",line4)


readLinemethod = f.readline()
print(readLinemethod)

