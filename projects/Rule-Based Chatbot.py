# rule based Ai python chatbot

import datetime
import time

name= input("swagat h, entet your name :")
presentHour= datetime.datetime.now().hour

if  5 <= presentHour <=11:
    print("good morning",name)
elif 11<= presentHour <= 17:
    print("good afternoon",name)
elif 17 <= presentHour <= 20:
    print("good evening",name)
else:
    print("good night",name)

print("Welcome to Your ChatBot")
print(" You can ask me basic question, Type'bbye'to exit from the bot") 

# Chatbot Memory Creation { dictionary of responses }

responses={
    "hello":"hi,Welcome. how can i halp you",
    "how are you": "I am very fine.Thank you for asking",
    "who are you":' I am samert AI chatbot',
    "motivate me":"keep going . every bug of your project make you a better developerr",
    "thank you":"great to here that",
    "Function kay hota hai ":"Go and chapter 7",

}
# method/function to get response of chatbot
def getresponseBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
        
    return" I am not able to tell that  yet . mai jald hi ye sikh luga"
        

# take user input
while True:
    userinput= input("please ask your question:")
    reply= getresponseBot(userinput)
    print("Bot responce:" , reply)

    if "bye" in userinput.lower():
        break
