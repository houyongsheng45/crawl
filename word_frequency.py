import jieba
import requests
from bs4 import BeautifulSoup

def extract_text(url):
    """Extract html content."""
    page_source = requests.get(url).content
    bs_source = BeautifulSoup(page_source)
    report_text = bs_source.find_all('p')

    text = ''

    for p in report_text:
        text += p.get_text()
        text += '\n'

    return text

def word_frequency(text):
    from collections import Counter

    words = [word for word in jieba.cut(text, cut_all=True) if len(word) >= 2]
    c = Counter(words)

    for word_freq in c.most_common(10):
        word, freq = word_freq
        print(word, freq)

url = 'http://codingpy.com/article/most-frequent-words-in-2016-china-governments-report-using-python/'
content = extract_text(url)
word_frequency(content)
