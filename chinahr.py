from bs4 import BeautifulSoup
import requests
import lxml
import csv

cate = 'http://www.chinahr.com/beijing/jobs/'
reponse_cate = requests.get(cate)
soup_cate = BeautifulSoup(reponse_cate.text, 'lxml')
cates = soup_cate.select('body > div.main > div.all-job > div > div.con-all > div.item-con.cur > div > div > a')
for url in cates:
    i = url['href']
    urls = [i + str(j) for j in range(1, 500, 1)]

def get_attractions(k):

    response = requests.get(k)
    soup = BeautifulSoup(response.text,"lxml")
    titles = soup.select('#searchList > div.resultList > div > ul > li.l1 > span.e1')
    moneys = soup.select('#searchList > div.resultList > div > ul > li.l2 > span.e2')
    companys = soup.select('#searchList > div.resultList > div > ul > li.l1 > span.e3.cutWord > a')
    industrys = soup.select('#searchList > div.resultList > div > ul > li.l2 > span.e3 > em')

    for title in titles:
        print(title.get_text())
    for money in moneys:
        print(money.get_text())
    for company in companys:
        print(company.get_text())
    for industry in industrys:
        print(industry.get_text())

    with open('chinahr.csv','a') as csvfile:
        fieldnames = ['职位','月薪','公司','行业']
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writerow({'职位':title.get_text(),'月薪':money.get_text(),'公司':company.get_text(),'行业':industry.get_text()})


for k in urls:
    get_attractions(k)