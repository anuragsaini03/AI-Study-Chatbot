#AI Study Buddy
print(".....Welcome to Your AI Study Buddy.....")
print("You can ask me any Question, Type 'Bye' to exit from chat")

#AI Study Buddy

import datetime
import time

print(".....Welcome to Your AI Study Buddy.....")
username = input("Enter your Name: ")

present_time = datetime.datetime.now().hour

#greeting for user

if 5 <= present_time <= 11:
    print("Good Morning ",username)
elif 11 <= present_time <= 17:
    print("Good Afternoon ",username)
elif 17 <= present_time <= 20:
    print("Good Evening ", username)
else:
    print("Good Night ",username)


print("You can ask me any Question, Type 'Bye' to exit from chat")

#here train modal, for specific question

response = {
    "hello" : "Hi, I'm your Study Buddy. How can I help you?",
    "how are you" : "I'm fine, What's about you?",
    "who are you" : "I'm AI Study Buddy, made for your help",
    "motivate me" : "Keep going, Every bug of your project makes you better",
    "happy" : "Great to hear that",
    "What is Python" : "Python is a popular, high-level programming language known for its readability and versatility in software and AI development.",
    "how to study effectively" : "Try the Pomodoro technique: study intensely for 25 minutes, then take a 5-minute break!",
    "i am stuck on a bug" : "Take a deep breath. Try explaining the code line-by-line to a 'rubber duck' or check your syntax error line.",
    "what is an API" : "An API (Application Programming Interface) allows two different software applications to talk to each other.",
    "what is git" : "Git is a version control system that tracks changes in your code and helps you collaborate with others.",
    "i feel overwhelmed" : "It's completely normal to feel this way. Take a 10-minute walk, drink some water, and tackle just one small task next.",
    "i want to quit" : "Remember why you started. Every expert was once a beginner. You've got this!",
    "sad" : "I'm sorry you're feeling down. Remember that progress isn't linear. Be kind to yourself today.",
    "i feel overwhelmed" : "It's completely normal to feel this way. Take a 10-minute walk, drink some water, and tackle just one small task next.",
    "i want to quit" : "Remember why you started. Every expert was once a beginner. You've got this!",
    "sad" : "I'm sorry you're feeling down. Remember that progress isn't linear. Be kind to yourself today.",
    "bye" : "Goodbye! Good luck with your studies, and see you soon!",
    "thank you" : "You're very welcome! Always happy to help a dedicated learner.",
    "clear" : "To clear your mind, take three deep breaths. To clear the terminal, type 'clear' or 'cls'!",
    "help" : "I can help with coding concepts, give motivational boosts, or suggest study tips. Try asking 'what is Git' or 'motivate me'!",
    "what are data types in python" : "Python has several built-in data types: Integers (int), Floats (float), Strings (str), Booleans (bool), Lists (list), Tuples (tuple), and Dictionaries (dict).",
    "difference between list and tuple" : "Lists are mutable (can be changed after creation) and use square brackets []. Tuples are immutable (cannot be changed) and use parentheses ().",
    "what is a dictionary" : "A dictionary in Python is an unordered collection of key-value pairs. Each key must be unique, and it is written using curly braces {}.",
    "how to create a function" : "You define a function in Python using the 'def' keyword, followed by the function name and parentheses. Example: def my_function():",
    "what is a lambda function" : "A lambda function is a small, anonymous function defined with the 'lambda' keyword. It can take any number of arguments but can only have one expression.",
    "what is a syntaxerror" : "A SyntaxError happens when Python cannot understand your code because you violated the rules of the language (like forgetting a colon ':' or closing parenthesis).",
    "what is a nameerror" : "A NameError occurs when you try to use a variable or function that has not been defined or spelled correctly yet.",
    "what is an indentationserror" : "Python relies on spaces/tabs to structure code blocks. An IndentationError means your spaces or tabs are not aligned correctly.",

    
}

#response of modal

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

