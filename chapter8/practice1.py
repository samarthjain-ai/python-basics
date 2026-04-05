# 1 write a program to read atext from a file certificate.txtand find
# whether it contains the world live 

file =open("certificate.txt","r")
data0file= file.read()

data0file=data0file.lower()

if "live" in data0file:
    print("yes live world is present in the file ")
else:
    print("No")