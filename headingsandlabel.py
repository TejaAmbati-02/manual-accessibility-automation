import requests
from bs4 import BeautifulSoup

url = input('Enter the link: ')

result = requests.get(url, verify=False).text
doc = BeautifulSoup(result, "html.parser")

tags = doc.find_all('h1')
attribute = [y['h1'] for y in tags if 'h1' in y.attrs]
#print(str(attribute))

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
    alt_text = tag.get_attribute_list('h1')[0]
    if not alt_text is None and not alt_text == "":
        print("H1 heading", xpath_soup(tag))
        correct += 1
        if len(alt_text) > 66:
            print("Headings should have less than 66 characters")
        else:
            print("Heading have sufficient characters")
    elif not alt_text is None:
        print("H1 tag is empty", xpath_soup(tag))
        missing += 1

if correct > 2:
    print("Number of H1 tag is more then 2")
elif missing > 0:
    print("H1 tag is empty")
else:
    print("Heading and Label condition is passed")


