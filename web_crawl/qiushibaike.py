#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author: yzw
@CreateTime: 2017-06-22, 20:49:28 CST+0800
@File: zhihu_spider.py
"""

from bs4 import BeautifulSoup
import requests

URL = 'https://www.qiushibaike.com/8hr/page/'

def get_url(url):
    for num in xrange(1,5):

        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        r = requests.get(url+str(num),headers=headers)

        content = r.content
        soup = BeautifulSoup(content, 'lxml')



        divs = soup.find_all(class_ = 'article block untagged mb15')

        for div in divs:
            if div.find_all(class_ = 'thumb'):
                continue
            joke = div.span.get_text()
            print joke



if __name__ == '__main__':
    get_url(URL)
