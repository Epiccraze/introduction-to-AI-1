print("Hello, I am ai chatbot, what's your name?")
name=input()
print("Nice to meet you,", name)
print("How is your mood today Good/Bad")
mood=input().lower()
if mood=="good":
    print("Nice to hear that!")
elif mood=="bad":
    print("Sorry you are having a bad day")
else:
    print("I think you might have entered the wrong thing. Want to try again?")
print("Nice chatting with you today!")