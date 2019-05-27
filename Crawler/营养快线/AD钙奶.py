#!/usr/bin/env python
# encoding=utf-8
from bs4 import BeautifulSoup
import requests
import urllib3
#目标网页URL
DOWNLOAD_URL = 'http://xh2.1024xp2.xyz/pw/html_data/14/1905/4093290.html'

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
    #parse_html(RawHTML)

    get_onepage_url_To_file(download_page("http://xh2.1024xp2.xyz/pw/thread.php?fid=14&page=1"))

#获得所有的页面
def get_all_page(firstpage):
    return

#获取一页的的全帖子URL地址
def get_onepage_url_To_file(first_pag):
    soup = BeautifulSoup(first_pag)
    all_invitation = soup.find('tbody', attrs={'style': 'table-layout:fixed;'})
    href_text = all_invitation.find_all('a', attrs={'title': '打开新窗口'})

    for src in href_text:
        src = "http://xh2.1024xp2.xyz/pw/" + src.get("href")
        get_picture_src_To_file(download_page(src))    

#对URL文件统一转化到图片SRC
def drive_URL_To_SRC():
    return

#对一个URL进行图片的转存
def get_picture_src_To_file(html):
    soup = BeautifulSoup(html)
    picture_class = soup.find('div', attrs={'id': 'read_tpc'})
    picture_list_soup = picture_class.find_all('img')
    #print(picture_list_soup)
    #给文件名命名
    number = 1 
    for picture in picture_list_soup:
        #追加到文件后
        #print(picture.get('src'))
        download_from_URL(number,picture.get('src'))
        number = number + 1

def download_from_URL(filename,URL):
    r = urllib3.PoolManager().request('GET', URL)
    data = r.data
    f = open("D:\TestFolderforCrawler\\" + str(filename) + ".jpg", 'wb+')
    f.write(data)
    f.close()


def parse_html(HTML):
    #读取所有的URL到文件
    #读取所有的SRC
    #get_picture_src_To_file()
    #下载所有的SRC
    return         
if __name__ == '__main__':
    main()
