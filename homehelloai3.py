import re, random
from colorama import Fore, init
init(autoreset=True)
books=[
    "Lonely Planet: Where To Go When",
    "Destinations of a Lifetime",
    "Best in tTravel 2025"]
facts=[
    "Mount Everest is the tallest mountain in the world standing at about 29,000 ft above sea level!",
    "Canada has more lakes than the rest of the world combine. Over 2 million.!",
    "Vatican City is the smallest country in the world, both by area and population!",
    "The Dead Sea is the lowest place on Earth at about 1,410 ft below sea level!"]
weather=[
    "Houston: Roughly 70 degrees fahrenheit",
    "Bangalore: Roughly 80 degrees fahrenheit",
    "Paris: Roughly 65 degrees fahrenhiet",
    "Tokyo: Roughly 50 degrees fahrenheit"]
destinations={
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]}
jokes=[
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus",
    "Why do travelers always feel warm? Because of all their hot spots!"]
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())
def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    preference=input(Fore.YELLOW + "You: ")
    preference=normalize_input(preference)
    if preference in destinations:
        suggestion=random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer=input(Fore.YELLOW + "You: ").lower()
        if answer=="yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
        elif answer=="no":
            print(Fore.RED + "TravelBot: Let's try another.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: I'll suggest again.")
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")
    show_help()
def guide():
    print(Fore.YELLOW + f"TravelBot: {random.choice(books)}")
def temperature():
    print(Fore.YELLOW + f"TravelBot: {random.choice(weather)}")
def fact():
    print(Fore.YELLOW + f"TravelBot: {random.choice(facts)}")
def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location=normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days=input(Fore.YELLOW + "You: ")
    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "-Pack versatile clothes.")
    print(Fore.GREEN + "-Bring chargers/adaptors.")
    print(Fore.GREEN + "-Check the weather forecast.")
def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")
def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "-Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "-Tell weather (say 'weather')")
    print(Fore.GREEN + "-Give books to help choose vacation destinations (say 'guide' or 'books')")
    print(Fore.GREEN + "-Tell interesting facts (say 'facts')")
    print(Fore.GREEN + "-Offer packing tips (say 'packing')")
    print(Fore.GREEN + "-Tell a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")
def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name=input(Fore.YELLOW+ "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")
    show_help()
    while True:
        user_input=input(Fore.YELLOW + f"{name}: ")
        user_input=normalize_input(user_input)
        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "book" in user_input or "guide" in user_input:
            guide()
        elif "weather" in user_input or "temperature" in user_input:
            temperature()
        elif "fact" in user_input:
            fact()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")
if __name__=="__main__":
    chat()