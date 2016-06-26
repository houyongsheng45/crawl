# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests,sys

def get_sex(class_name):
    if class_name == ["member_ico1"]:
        return '女'
    else:
        return '男'

def get_pages(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text,'lxml')
    pages = soup.select('#page_list > ul > li > a')
    for page in pages:
        href = page.get('href')
        get_detail(href)

def get_detail(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text,'lxml')
    titles = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
    addresses = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span.pr5')
    costs = soup.select('#pricePart > div.day_l > span')
    photoes = soup.select('#curBigImage')
    owners = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    credits = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > p > span.zm_ico.zm_credit')
    rates = soup.select('#comment_box > div.comment_box.clearfix > div > span > em')
    sexes = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
    for title,address,cost,photo,owner,sex,name,credit,rate in zip (titles,addresses,costs,photoes,owners,sexes,names,credits,rates):
        data = {
            'title':title.get_text(),
            'address':address.get("em"),
            'cost':cost.get_text(),
            'photo':photo.get("src"),
            'owner':owner.get("src"),
            'sex':get_sex(sex.get("class")),
            'name':name.get_text(),
            'credit':credit.get_text(),
            'rate':rate.get_text()
        }
        print(data)


urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(1,13)]

for single_url in urls:
    get_pages(single_url)
    print()
#sys.stdout = open('xiaozu.txt','a')