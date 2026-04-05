# just for wake up my mind 
for i in range(6):
    print(i*i)

# logic drill 
# given a positive integer n write a function that returns the sum of its digits and count of even number 

def analyze_number(n):
    sum_digit=0
    even_digit=0
    while n>0:
        digit=n%10
        sum_digit+= digit

        if digit%2==0:
            even_digit+=1

        n//=10

    return sum_digit,even_digit

n=int(input("Enter your number here : "))
s,ev=analyze_number(n)
print("sum=",s)
print("digit=",ev)

print("hello")