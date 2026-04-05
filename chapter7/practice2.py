# 1 write a function square(num) that returns the square of a number ,

def square(num=10):
    return num**2

print(square(5))

# 2 write a function that thakes a string and returns the count of vowels and 
# consonats seprately.


def func(userInput):

    # define vowels 
    vowels = "aeiouAEIOU"

    countVowel=0
    countConsonants = 0

#samarth234
    for eachChar in userInput:
        if(eachChar.isalpha()):
            if(eachChar in vowels):
                countVowel= countVowel+1
            else:
                countConsonants+=1

    return countVowel,countConsonants

# Function call

vowels , consonent =func("samarth jain")

print(vowels,consonent)

#define a funstion convert_to_upper(words) that returne the uppercasr version of the string 


def convert_to_upper(words = "samarth jain"):
    print(words.upper())

convert_to_upper("subh")

# creat a function full_name(fname,lname) that returns the full name
#joined with a space 


