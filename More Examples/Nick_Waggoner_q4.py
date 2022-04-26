import os
import bs4

# Reads from the HTML file (web-scraping) using beautifulsoup and prints out the objects matching the item type/id

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, features="html.parser")
span = exampleSoup.select('span[id]')
print(len(span))
print(span[1].getText())
