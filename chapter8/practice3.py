# read only the first line of bio.tex
import os
try:
    with open("newtext.txt","r") as h:
        line1=h.readline()
    print(line1)
except :
    print("subh")



# print how many lines are present in notes.txt

    alllines=h.readlines()
    print(alllines)
    print(len(alllines))


# rename the file 

# os.rename("mast.txt","subh.txt")