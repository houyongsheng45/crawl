from bs4 import BeautifulSoup
import requests
import lxml
import csv

# 获取职能分类列表cates
cate = 'http://www.chinahr.com/beijing/jobs/'
reponse_cate = requests.get(cate)
soup_cate = BeautifulSoup(reponse_cate.text, 'lxml')
cates = soup_cate.select('body > div.main > div.all-job > div > div.con-all > div.item-con.cur > div > div > a')
# 获取每个分类的职位列表job_urls
for cate_url in cates:
    i = cate_url['href']
    job_urls = [i + str(j) for j in range(1, 500, 1)]
    # 获取每个职位的详情页地址detail_page
    for job_url in job_urls:
        response_job_url = requests.get(job_url)
        soup_job_url = BeautifulSoup(response_job_url.text, 'lxml')
        detail_page = soup_job_url.select('#searchList > div.resultList > div > ul > li.l1 > span.e1 > a')
        # 获取每个职位详情页的职位介绍job_info
        for detail_url in detail_page:
            m = detail_url['href']
            response_m = requests.get(m)
            soup_m = BeautifulSoup(response_m.text, 'lxml')
            job_info = soup_m.select(
                'body > div.job-detail.page.clear > div.job-detail-l > div.job_intro.jpadding.mt15 > div.job_intro_wrap > div')


def get_attractions(k):
    response = requests.get(k)
    soup = BeautifulSoup(response.text,"lxml")


    titles = soup.select('body > div.job-detail.page.clear > div.job-detail-l > div.job_profile.jpadding > div.base_info > div > h1 > span.job_name')
    moneys = soup.select('body > div.job-detail.page.clear > div.job-detail-l > div.job_profile.jpadding > div.base_info > div.job_require > span.job_price')
    companys = soup.select('body > div.job-detail.page.clear > div.job-detail-r > div > h4 > a')
    industrys = soup.select('body > div.job-detail.page.clear > div.job-detail-r > div > table > tbody > tr > td > a')
    scales = soup.select('body > div.job-detail.page.clear > div.job-detail-r > div > table > tbody > tr > td')
    ctypes = soup.select('body > div.job-detail.page.clear > div.job-detail-r > div > table > tbody > tr > td')
    exps = soup.select('body > div.job-detail.page.clear > div.job-detail-l > div.job_profile.jpadding > div.base_info > div.job_require > span.job_exp')
    degrees = soup.select('body > div.job-detail.page.clear > div.job-detail-l > div.job_profile.jpadding > div.base_info > div.job_require > span')
    jobtimes = soup.select('body > div.job-detail.page.clear > div.job-detail-l > div.job_profile.jpadding > div.base_info > div.job_require > span')
    locations = soup.select('body > div.job-detail.page.clear > div.job-detail-l > div.job_profile.jpadding > div.base_info > div.job_require > span.job_loc')


    for title in titles:
        print(title.get_text())
    for money in moneys:
        print(money.get_text())
    for company in companys:
        print(company.get_text())
    for industry in industrys:
        print(industry.get_text())
    for scale in scales:
        print(scale.get_text())
    for ctype in ctypes:
        print(ctype.get_text())
    for exp in exps:
        print(exp.get_text())
    for degree in degrees:
        print(degree.get_text())
    for jobtime in jobtimes:
        print(jobtime.get_text())
    for location in locations:
        print(location.get_text())

    with open('chinahr.csv','a') as csvfile:
        fieldnames = ['职位','月薪','公司','行业','规模','性质','年限要求','学历要求','工作时间','地点']
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writerow({'职位':title.get_text(),'月薪':money.get_text(),'公司':company.get_text(),'行业':industry.get_text(),'规模':scale.get_text(),'性质':ctype.get_text(),'年限要求':exp.get_text(),'学历要求':degree.get_text(),'工作时间':jobtime.get_text(),'工作地点':location.get_text(),'工作内容':job_info.get_text()})


for k in job_urls:
    get_attractions(k)
