#coding=utf-8
from urllib import request
import re

def geNewUrl(url):
    baseurl = "http://www.heibanke.com/lesson/crawler_ex00/"
    if url:
        reg = r'下一个你需要输入的数字是(.....)'
    else:
        reg = r'你需要在网址后输入数字(.....)'

    url = baseurl if url is None else url

    page = request.urlopen(url)
    html = page.read().decode('utf-8')

    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    exturl = imglist[0] if  imglist.__len__() != 0 else ''
    return baseurl+exturl

def test():
    x=0
    L = []
    baseurl = "http://www.heibanke.com/lesson/crawler_ex00/"
    newurl = None
    while( x<100 and baseurl != newurl):
        newurl =  geNewUrl(newurl)
        if newurl == baseurl:
            break
        print(newurl)
        L.append(newurl)


test()
