#AI Study Buddy
print(".....Welcome to Your AI Study Buddy.....")
print("You can ask me any Question, Type 'Bye' to exit from chat")

response = {
    "hello" : "Hi, I'm your Study Buddy. How can I help you?",
    "how are you" : "I'm fine, What's about you?",
    "who are you" : "I'm AI Study Buddy, made for your help",
    "motivate me" : "Keep going, Every bug of your project makes you better",
    "happy" : "Great to hear that",
    "What is Python" : "Python is a popular, high-level programming language known for its readability and versatility in software and AI development.",
    
}

def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in response:
        if eachKey in userQuestion:
            return response[eachKey]
        # else:
        #     print("I'm not able to tell yet. I'm in learning Phase")
    return "I'm not able to tell yet. I'm in learning Phase"

# Take user input

while True:

    userInput = input("Please ask your Question: ")
    reply = getResponseOfBot(userInput)
    print("Bot Respose: ",reply)


    if "bye" in userInput.lower():
        break