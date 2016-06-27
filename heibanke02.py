#coding=utf-8
from urllib import request,parse
import re

def getData(password):
    data = {
        "username":"Jiao",
        "password":password
    }
    return data

def getResult(response):
    html = response.read().decode('utf-8')
    reg = r'您输入的密码错误, 请重新输入'
    msgre = re.compile(reg)
    msglist = re.findall(msgre,html)
    return msglist.__len__() == 0

def getPassword():
    url="http://www.heibanke.com/lesson/crawler_ex02/"
    for i in range(0,30):
        data  = getData(i)
        post_data = parse.urlencode(data).encode("utf-8")
        response = request.urlopen(url,post_data)
        result = getResult(response)
        if result:
            return i
    return None



def test():
    password = getPassword()
    if password:
        print("password is %s" % password)
    else:
        print("can not find password")

test()