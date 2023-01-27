import requests
from bs4 import BeautifulSoup

url = input('Enter the link: ')

result = requests.get(url, verify=False).text
doc = BeautifulSoup(result, "html.parser")

#tags = doc.find_all('button')
tag1 = doc.find('a')
string1 = "Skip to Navigation"
correct = 0
missing = 0
Content = 0
Navigation = 0
alt_text1 = tag1.get_text()
s= alt_text1.split()
if "Skip" in s:
    correct += 1
    if "Content" in s:
        print("Present: Skip to Content")
    elif "Navigation" in s:
        print("Present: Skip to Navigation")
    else:
        print("Not present")
else:
    print("Not present")


