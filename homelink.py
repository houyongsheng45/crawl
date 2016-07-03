from bs4 import BeautifulSoup
import requests
import csv

headers = {'User-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'
           }

url = "http://m.lianjia.com/bj/zufang/pg1"
urls = ['http://m.lianjia.com/bj/zufang/pg' + str(i) for i in range(1,56420,1)]

def get_attractions(url):
    response = requests.get(url,headers = headers)
    soup = BeautifulSoup(response.text,'lxml')
    titles = soup.select('#main_start > section.page.page_zufang > div > div.mod_box.house_lists > div.mod_cont > ul > li > div > div.item_list > div.item_main.text_cut')
    locations = soup.select('#main_start > section.page.page_zufang > div > div.mod_box.house_lists > div.mod_cont > ul > li > div > div.item_list > div.item_other > a')
    infos = soup.select('#main_start > section.page.page_zufang > div > div.mod_box.house_lists > div.mod_cont > ul > li > div > div.item_list > div.item_minor > div.info')
    prices = soup.select('#main_start > section.page.page_zufang > div > div.mod_box.house_lists > div.mod_cont > ul > li > div > div.item_list > div.item_minor > div.price_total')
    tags = soup.select('#main_start > section.page.page_zufang > div > div.mod_box.house_lists > div.mod_cont > ul > li > div > div.item_list > div.tag_box')

    for title in titles:
        print(title.get_text())
    for location in locations:
        print(location.get_text())
    for info in infos:
        print(info.get_text())
    for price in prices:
        print(price.get_text())
    for tag in tags:
        print(tag.get_text())

    with open('homelink.csv','a') as csvfile:
        fieldnames = ['标题','地点',"详情","价格","标签"]
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
#       writer.writeheader()
        writer.writerow({'标题':title.get_text(),'地点':location.get_text(),'详情':info.get_text(),'价格':price.get_text(),'标签':tag.get_text()})

for i in urls:
    get_attractions(i)


