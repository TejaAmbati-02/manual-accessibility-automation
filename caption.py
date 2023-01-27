import requests
from bs4 import BeautifulSoup

url = input('Enter the link: ')

result = requests.get(url, verify=False).text   
doc = BeautifulSoup(result, "html.parser")

tags = doc.find_all('video')
attribute = [y['track'] for y in tags if 'track' in y.attrs]
print(str(attribute))

def xpath_soup(element):
    if element is None:
        return '/html'
    components = []
    child = element if element.name else element.parent
    for parent in child.parents:  # type: bs4.element.Tag
        siblings = parent.find_all(child.name, recursive=False)
        components.append(
            child.name if 1 == len(siblings) else '%s[%d]' % (
                child.name,
                next(i for i, s in enumerate(siblings, 1) if s is child)
                )
            )
        child = parent
    components.reverse()
    if not components:
        return '/html'
    return '/%s' % '/'.join(components)

correct = 0
missing = 0
for tag in tags:
    alt_text = tag.get_attribute_list('track')[0]
    if not alt_text is None:
        print("Caption is present", xpath_soup(tag))
        correct += 1
    else:
        print("Caption is missing", xpath_soup(tag))
        missing += 1

print("Number of Video having Caption: ", correct)
print("Number of Video not having Caption: ", missing)

