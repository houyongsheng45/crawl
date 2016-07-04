from bs4 import BeautifulSoup
import requests
import csv

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
    infos = soup.select('body > div.job-detail.page.clear > div.job-detail-l > div.job_intro.jpadding.mt15 > div.job_intro_wrap > div')

    title = titles[0].get_text()
    money = moneys[0].get_text()
    company = companys[0].get_text()
    industry = industrys[0].get_text()
    scale = scales[0].get_text()
    ctype = ctypes[0].get_text()
    exp = exps[0].get_text()
    degree = degrees[0].get_text()
    jobtime = jobtimes[0].get_text()
    location = locations[0].get_text()
    info = infos[0].get_text()

    with open('chinahr.csv','a') as csvfile:
        fieldnames = ['职位','月薪','公司','行业','规模','性质','年限要求','学历要求','工作时间','工作地点','工作内容']
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writerow({'职位':title,'月薪':money,'公司':company,'行业':industry,'规模':scale,'性质':ctype,'年限要求':exp,'学历要求':degree,'工作时间':jobtime,'工作地点':location,'工作内容':info})

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
        for k in detail_page:
            get_attractions(k['href'])
