# @Author: jerry
# @Date:   2018-03-04T23:04:16+08:00
# @Last modified by:   jerry
# @Last modified time: 2018-03-05T23:09:57+08:00
import random,string,hashlib
import requests
from urllib import request
import urllib

from bs4 import BeautifulSoup


def haslib():
    a = ''.join(random.choice(string.ascii_letters + string.digits)
                for _  in range(10))
    print (a)
    b = hashlib.md5("".join("str_args").encode('utf-8')).hexdigest()
    print(b)


def recursion(n):
    if n <2:
        return n
    else:
        b = recursion(n-1) + recursion(n-2)
        return b

def main():
    pass

def get_pic():
    url = "https://detail.1688.com/offer/560514443414.html"
    html =  request.urlopen(url)
    soup = BeautifulSoup(html,"lxml")
    i = 0
    for link in soup.find_all('img'):
        i += 1
        imgurl = link.get("src")
        if not imgurl.startswith("http"):
            pass
        else:
            print (imgurl)
            request.urlretrieve(imgurl,"log/%02d.jpg" % i)

if __name__ == '__main__':
    main()
    # print (recursion(8))
    get_pic()
