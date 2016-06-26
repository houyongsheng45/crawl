from bs4 import BeautifulSoup
from urllib.request import urlopen
import os

html = urlopen('http://www.newsnow.co.uk/h/World+News/North+America/Canada')
soup = BeautifulSoup(html,'html.parser')
divs = soup.findAll('div', attrs={'class':'hl'})
for div in divs:
    if div.find('span', {'c': True}):
        print ("%s|%s" % (div.find('span',{'c':True}).get('c'), div.find('span',{'data-pub':True}).text))