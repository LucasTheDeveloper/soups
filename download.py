import requests
from bs4 import BeautifulSoup

exampleFile = open('example.html')
exampleSoup = BeautifulSoup(exampleFile.read(), 'html.parser')  # Specify the parser you want to use
elems = exampleSoup.select('#author')
type(elems)
len(elems)
type(elems[0])
print(elems[0].getText())
str(elems[0])
elems[0].attrs

