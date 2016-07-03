import requests
from bs4 import BeautifulSoup
import csv

headers = {'User-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'
           }

def get_attractions(url,date=None):
    page = requests.get(url,headers = headers)
    soup = BeautifulSoup(page.text,'lxml')
    zhnames = soup.select('#cube-info > div > div.cube-title.sp-color > div.name')
    symbols = soup.select('#cube-info > div > div.cube-title.sp-color > div.symbol')
    dates = soup.select('#cube-info > div > div.cube-color.sp-color > div.cube-createdate > span.date')
    tags = soup.select('#cube-info > div > div.cube-color.sp-color > div.cube-style')
    periods = soup.select('#cube-info > div.cube-blockmain > div > div.cube-profits.fn-clear > div > div.per')
    years = soup.select('#cube-info > div > div.cube-color.sp-color > div.cube-profit-year.fn-clear > span.per')
    ranks = soup.select('#cube-info > div > div.cube-ranks.fn-clear > div.cube-rank.rank > p > span')
    yuebaos = soup.select('#cube-info > div > div.cube-ranks.fn-clear > div.cube-baobao.rank > p > span')

    for zhname in zhnames:
        print (zhname.get_text())

    for symbol in symbols:
        print (symbol.get_text())

    for date in dates:
        print (date.get_text())

    for tag in tags:
        print (tag.get_text())

    for period in periods:
        print (period.get_text())

    for year in years:
        print (year.get_text())

    for rank in ranks:
        print (rank.get_text())

    for yuebao in yuebaos:
        print (yuebao.get_text())


    with open('xueqiu_a.csv','a') as csvfile:
        fieldnames = ['组合名称','代码',"时间","标签","净值","年收益","月收益排名","对比余额宝"]
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
#        writer.writeheader()
        writer.writerow({'组合名称':zhname.get_text(),'代码':symbol.get_text(),'时间':date.get_text(),'标签':tag.get_text(),'净值':period.get_text(),'年收益':year.get_text() + "%",'月收益排名':"跑赢" + rank.get_text() + "组合",'对比余额宝':yuebao.get_text()})

urls_a = ['https://xueqiu.com/p/ZH000' + str(i) for i in range(101,999,1)]
urls_b = ['https://xueqiu.com/p/ZH00' + str(i) for i in range(1000,9999,1)]
urls_c = ['https://xueqiu.com/p/ZH0' + str(i) for i in range(10000,99999,1)]
urls_d = ['https://xueqiu.com/p/ZH' + str(i) for i in range(100000,901882,1)]

for i in (urls_b):
    get_attractions(i)
