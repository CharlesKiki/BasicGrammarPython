#!/usr/bin/env python
# encoding=utf-8
from bs4 import BeautifulSoup
import requests
#目标网页URL
DOWNLOAD_URL = 'http://grs.henu.edu.cn'

#获取HTML文件
def download_page(url):
    headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
}
    #混淆请求头
    data = requests.get(url, headers=headers).content
    return data

def main():
    RawHTML = download_page(DOWNLOAD_URL)
    parse_html(RawHTML)

def parse_html(html):
    soup = BeautifulSoup(html)
    news_ul = soup.find('div', attrs={'class': 'span5 index-up-item '})
    news_list_soup = news_ul.find('ul')
    for news in news_list_soup.find_all('a'):
        print(news.get_text())

if __name__ == '__main__':
    main()
