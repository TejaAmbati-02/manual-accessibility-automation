import requests
from bs4 import BeautifulSoup

url = input('Enter the link: ')

result = requests.get(url, verify=False).text
doc = BeautifulSoup(result, "html.parser")

tags = doc.find_all('a')

correct = 0
missing = 0
for tag in tags:
    alt_text = tag.get_text()
    if not alt_text is None and not alt_text == "":
        print("Title: ", alt_text)
    elif not alt_text is None:
        print("Title is empty")



