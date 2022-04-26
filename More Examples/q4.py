import os
import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, features="html.parser")
span = exampleSoup.select('span[id]')
print(len(span))
print(span[1].getText())