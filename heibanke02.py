#coding=utf-8
from urllib import request,parse
import re

def getData(password):
    data = {
        "csrfmiddlewaretoken":"u6wGrbEnmcfKCaHCsO2wkszyMQnQOMS1",
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
    hdr = {
        "Cookie":"sessionid=gl86prhdtovhwd4xddk3x6d5eelzeaz3; csrftoken=u6wGrbEnmcfKCaHCsO2wkszyMQnQOMS1; Hm_lvt_74e694103cf02b31b28db0a346da0b6b=1466992468,1467076208; Hm_lpvt_74e694103cf02b31b28db0a346da0b6b=1467077707",
    }
    for i in range(0,30):
        data  = getData(i)
        post_data = parse.urlencode(data).encode("utf-8")
        req = request.Request(url,post_data,headers=hdr)
        response = request.urlopen(req)
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