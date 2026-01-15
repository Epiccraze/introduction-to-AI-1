import requests
url = "https://uselessfacts.jsph.pl/random.json?Language=en"
def get_random_fact():
    response=requests.get(url)
    if response.status_code==200:
        fact_data=response.json()
        print(f"Did you know? {fact_data['text']}")
    else:
        print("Failed to fetch fact")
while True:
    input("Press Enter to get a random fact or type 'q' to quit...")
    if input().lower() == 'q':
        break
    get_random_fact()