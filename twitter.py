from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import re

html = urlopen('https://twitter.com/i/streams/category/686639666771046402')
soup = BeautifulSoup(html,'html.parser')
divs = soup.findAll('div', attrs={'class':'TweetWithPivotModule'})
for div in divs:
        #print (div)

        p = '<div class="TweetWithPivotModule" data-scribe-context=\'{"id":"(.*)","name":"(.*)","type":"(.*)"}\'>'
        res = re.findall(p, str(div))
        if res:
            print (res[0][1])

        '''if div.find('data-scribe-context', {'name': True}):
            print (name.text)'''