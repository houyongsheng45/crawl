#-*— coding:utf8 -*-
from bs4 import BeautifulSoup
import requests,time,sys

url = 'http://www.tripadvisor.cn/Attractions-g293916-Activities-Bangkok.html#ATTRACTION_LIST'
urls = ['http://www.tripadvisor.cn/Attractions-g293916-Activities-oa{}-Bangkok.html#ATTRACTION_LIST'.format(str(i)) for i in range(0,480,30)]

def get_attractions(url,date=None):
    html = requests.get(url)
    soup = BeautifulSoup(html.text,"lxml")
    titles = soup.select('div.property_title > a[target="_blank"]')
    cates = soup.select('div.p13n_reasoning_v2 > a > span')
    for title,cate in zip(titles,cates):
        data = {
            'title':title.get_text(),
            'cate':cate.get_text(),
        }
        print(data)

for single_url in urls:
    get_attractions(single_url)
    sys.stdout = open("tripadvisor.txt", "a")