from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

# try: 
#     html = urlopen('https://www.pulzo.com/')
# except HTTPError as e:	
#     print(e)
# except URLError as e:
#     print('the server could not be found')
# else:
#     print('It worked')
#     bs = BeautifulSoup(html.read(), 'html.parser')
#     print(bs.title)
    
#     try:
#         badContent = bs.nonExistentTag.anotherTag
#     except AttributeError as e:
#         print('Tag was not found')
#     else:
#         if badContent == None:
#             print('Tag was not found')
#         else:
#             print('badContent')

def getTitle(url): # Mi función se llama obtener titulo
    try:
        html=urlopen(url)
    except HTTPError as es:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError:
        return None
    return title

title = getTitle('https://www.pulzo.com/')
if title == None:
    print('Title could not found')
else:
    print(title)

