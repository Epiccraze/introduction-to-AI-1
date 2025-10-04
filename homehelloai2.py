import colorama # pyright: ignore[reportMissingModuleSource]
from colorama import Fore, Style # pyright: ignore[reportMissingModuleSource]
from textblob import TextBlob # pyright: ignore[reportMissingImports]
colorama.init()
def get_valid_name():
    user_name=input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL} ").strip()
    result=user_name.isalpha()
    if result==False:
        print("Invalid Name")
        user_name="Mystery"
    return user_name
def show_processing_animation():
    print(f"{Fore.RED}Loading...")
    print(f"{Fore.RED}Loading...")
    print(f"{Fore.RED}Loading...")
def analyze_sentiment():
    polarity=TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type="Positive"
        color=Fore.GREEN
        emoji="😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color=Fore.RED
        emoji="😢"
    else:
        sentiment_type="Neutral"
        color=Fore.YELLOW
        emoji="😐"
    return polarity, sentiment_type, color, emoji
print(f"{Fore.CYAN},👋Welcome to Sentiment Spy!🕵️{Style.RESET_ALL}")
user_name=get_valid_name()
conversation_history=[]
print(f"\n{Fore.CYAN}Hello, Agent {user_name}!")
print(f"Type a Sentence and I will analyze your sentences with TextBlob and show you the sentiment.")
print(f"Type {Fore.YELLOW}'reset'{Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN}, {Fore.YELLOW}'exit'{Fore.CYAN}, or {Fore.YELLOW}'help'.{Style.RESET_ALL}\n")
while True:
    user_input=input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()
    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue
    if user_input.lower()=="exit":
        print(f"\n{Fore.BLUE}???? Exiting Sentiment Spy. Farewell, Agent {user_name}! {Style.RESET_ALL}")
        break
    elif user_input.lower()=="help":
        print(f"Type a Sentence and I will analyze your sentences with TextBlob and show you the sentiment.")
        print(f"Type {Fore.YELLOW}'reset'{Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN}, {Fore.YELLOW}'exit'{Fore.CYAN}, or {Fore.YELLOW}'help'.{Style.RESET_ALL}\n")
    elif user_input.lower()=="reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}???? All conversation history cleared!{Style.RESET_ALL}")
        continue
    elif user_input.lower()=="history":        
        if conversation_history:
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type=="Positive":
                    color=Fore.GREEN
                    emoji="😊"
                elif sentiment_type=="Negative":
                    color=Fore.RED
                    emoji="😢"
                else:
                    color=Fore.YELLOW
                    emoji="😐"
                print(f"{idx}, {color}{emoji} {text} "f"(Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        continue
    p, s, c, e = analyze_sentiment()
    conversation_history.append((user_input, p, s))
    show_processing_animation()
    print(f"{c}{e} {s} sentiment detected! "f"(Polarity: {p:.2f}){Style.RESET_ALL}")
