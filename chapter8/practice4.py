# f =open("notes.txt","w") 

# f.write("today i learn file handling.\n")
# f.write("today is my day \n")
# f.close
# f=open("notes.txt","r")
# print(f.read())
# f.close

# f= open("notes.txt","w")
# f.write("i compleat my file handling session")

# ✅ Q1. Write a program to count the number of lines in a file.
f=open("notes.txt" , "r")
linenum =f.readlines()
print("Number of lines are : ",len(linenum))
f.close

#✅ Q2. Write a program to count how many words are in a file. 

with open("notes.txt","r") as f:
    text=f.read()
    words =text.split()
    print("number of words :",len(words))

#✅ Q3. Write a program to copy content from one file to another.

with open("notes.txt", "r") as f1:
    data = f1.read()

with open("copy.txt", "w") as f2:
    f2.write(data)

print("File copied successfully!")


#Q4. Write a program to count how many characters (letters) are in a file — excluding spaces and newlines.

with open("notes.txt","r") as f:
    text =f.read()


clean_text=text.replace(" ","").replace("\n","")

print("number of characters :",len(clean_text))



# 5 Q4. Write a program to count how many characters (letters) are in a file — excluding spaces and newlines.
with open("notes.txt","r") as f:
    read=f.read()

with open("subh.txt","w")as w:
    write=w.write(read)


with open("subh.txt") as d:
    done=d.read()
    print(done)