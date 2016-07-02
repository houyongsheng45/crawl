# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys


headers = {'User-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'
           }

def get_attractions(url,date=None):
    page = requests.get(url,headers = headers)
    soup = BeautifulSoup(page.text,'lxml')

    names = soup.select('#cube-info > div > div.cube-title.sp-color > div.name')
    symbols = soup.select('#cube-info > div > div.cube-title.sp-color > div.symbol')
    fans = soup.select('#cube-info > div > div.cube-color.sp-color > div.cube-createdate > span')
    tags = soup.select('#cube-info > div > div.cube-color.sp-color > div.cube-style')
    dailys = soup.select('#cube-info > div > div.cube-color.sp-color > div.cube-profits.fn-clear > div > div.per')
    years = soup.select('#cube-info > div > div.cube-color.sp-color > div.cube-profit-year.fn-clear > span.per')
    ranks = soup.select('#cube-info > div > div.cube-ranks.fn-clear > div.cube-rank.rank > p > span')
    yuebaos = soup.select('#cube-info > div > div.cube-ranks.fn-clear > div.cube-baobao.rank > p > span')

    for name in names:
        print name.get_text().encode('ascii','ignore').decode('ascii')

    for symbol in symbols:
        print symbol.get_text().encode('ascii', 'ignore').decode('ascii')

    for fan in fans:
        print fan.get_text().encode('ascii', 'ignore').decode('ascii')

    for tag in tags:
        print tag.get_text().encode('ascii', 'ignore').decode('ascii')

    for daily in dailys:
        print daily.get_text().encode('ascii', 'ignore').decode('ascii')

    for year in years:
        print year.get_text().encode('ascii', 'ignore').decode('ascii')

    for rank in ranks:
        print rank.get_text().encode('ascii', 'ignore').decode('ascii')

    for yuebao in yuebaos:
        print yuebao.get_text().encode('ascii', 'ignore').decode('ascii')

urls_a = ['https://xueqiu.com/p/ZH000' + str(i) for i in range(101,999,1)]
urls_b = ['https://xueqiu.com/p/ZH00' + str(i) for i in range(1000,9999,1)]
urls_c = ['https://xueqiu.com/p/ZH0' + str(i) for i in range(10000,99999,1)]
urls_d = ['https://xueqiu.com/p/ZH' + str(i) for i in range(100000,901882,1)]

for i in (urls_a):
    get_attractions(i)
    sys.stdout = open("xueqiu.txt", "a")