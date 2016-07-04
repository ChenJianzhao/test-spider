#coding=utf-8
from urllib import request,parse
import re

def parseData(response,itemmap):
    html = response.read().decode('utf-8')
    posstr = r'title="password_pos">(.+?)</td>'
    valstr = r'title="password_val">(.+?)</td>'
    posre = re.compile(posstr)
    valre = re.compile(valstr)
    posList = re.findall(posre,html)
    valList = re.findall(valre,html)
    # for k,v in posList,valList:
    #     itemmap[k]=v
    #for i in range(0, 7):
    while( posList.__len__() > 0):
        pos = posList.pop(0)
        val = valList.pop(0)
        itemmap[pos] = val
        print(itemmap.items())

def requestdata():
    baseurl = "http://www.heibanke.com/lesson/crawler_ex03/pw_list/?page="
    hdr = {
        "cookie":"sessionid=yfuhkb4ehdosm33uo3oxtr1hw1ai7r3m; csrftoken=AmehYubARHFXRa2BkfZTMPM4zzG2uEZu; Hm_lvt_74e694103cf02b31b28db0a346da0b6b=1467634317; Hm_lpvt_74e694103cf02b31b28db0a346da0b6b=1467635302"
    }
    postdata = getpostdata("AmehYubARHFXRa2BkfZTMPM4zzG2uEZu")
    itemmap = {}
    while(itemmap.__len__()<100):
        for i in range(1,13):
            url = baseurl + str(i)
            req = request.Request(url, postdata, headers=hdr)
            response = request.urlopen(req)
            parseData(response,itemmap)
    password = ''
    for i in range(0,99):
        password += itemmap[str(i)]
    print(password)

#----------------------------------------------------------------------------------------------------
def login():
    '''
    模拟登录
    :return: None
    '''
    loginurl = 'http://www.heibanke.com/accounts/login'
    cookie = loginpage()
    hdr = getheader(cookie)
    postdata = getpostdata(cookie)
    req = request.Request(loginurl, postdata, headers=hdr)
    loginresp = request.urlopen(req)
    print(loginresp.read().decode('utf-8'))

def getpostdata(cookie):
    '''
    组装post参数
    :param cookie: 登录页面返回的cookie值
    :return: 编码后的postdata
    '''
    data = {
        "username":"Jiao",
        "password":"123456",
        "csrfmiddlewaretoken":cookie
    }
    return parse.urlencode(data).encode('utf-8')

def loginpage():
    '''
    请求登录页面
    :return: response中cookie的value
    '''
    loginurl = 'http://www.heibanke.com/accounts/login'
    loginresp = request.urlopen(loginurl)
    print(loginresp.read().decode('utf-8'))
    cookie = loginresp.getheader('Set-Cookie')
    return cookie.split(';')[0].split('=')[1]

def getheader(cookie):
    hdr = {
        "Cookie":"csrftoken="+cookie
    }
    return hdr

def test():
   login()


def test2():
    requestdata()

def test3():
    password =''
    dict_items={"25":"6","4":"0","99":"3","65":"3","7":"2","68":"5","11":"1","13":"9","83":"2","30":"1","40":"5","56":"3","52":"3","28":"8","17":"3","45":"2","77":"9","22":"7","78":"5","90":"6","8":"6","37":"3","9":"5","54":"1","66":"5","62":"4","38":"8","53":"8","74":"5","95":"7","24":"5","61":"4","100":"9","35":"8","89":"4","32":"3","80":"4","10":"3","27":"2","20":"8","46":"6","94":"4","87":"8","14":"0","72":"8","6":"3","85":"5","75":"0","86":"4","51":"3","88":"9","98":"0","97":"9","55":"8","92":"3","41":"3","42":"6","18":"6","64":"1","3":"3","39":"2","79":"2","21":"7","76":"6","23":"4","44":"5","84":"9","16":"6","47":"4","49":"7","31":"7","34":"1","71":"4","48":"9","19":"6","26":"6","5":"3","93":"6","81":"4","91":"1","69":"7","36":"5","60":"7","59":"6","96":"9","70":"7","33":"6","43":"7","82":"3","73":"9","58":"8","29":"8","67":"3","50":"2","1":"7","12":"4","2":"9","63":"5","15":"1","57":"0"}
    for i in range(1,100):
        password+=dict_items[str(i)]
    print(password)


#test()
#test2()
test3()