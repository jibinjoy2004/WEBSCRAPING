import requests
from bs4 import BeautifulSoup
def find_meaning(word):
    # Send a GET request to the website
    response = requests.get(f"https://www.vocabulary.com/dictionary/{word}")

    # Parse the HTML response using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the element that contains the definition
    definition = soup.find("p", {"class": "short"})

    # Extract the text of the definition
    meaning = definition.text.strip()

    return meaning
print(find_meaning(word=input('Enter a word')))