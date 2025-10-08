answer="yes"
print("Hello, I am ai chatbot, what's your name?")
name=input()
print("Nice to meet you,", name)
while answer=="yes":
    print("How is your mood today? Good/Bad")
    mood=input().lower()
    if mood=="good":
        print("Nice to hear that!")
    elif mood=="bad":
        print("Sorry you are having a bad day")
    else:
        print("I think you might have entered the wrong thing.")
    hobby=input ("What is one of your favorite hobbies?")
    print("I also love doing",hobby)
    answer=input("Would you like to continue? Yes/No").lower()
print("Nice chatting with you today,",name)