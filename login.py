from urllib import request, parse

def execute():
    login_url = 'http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex04/'
    url = 'http://www.heibanke.com/lesson/crawler_ex04/'
    #获取登录页
    cookie = request.urlopen(login_url).getheader('Set-Cookie')
    csrftoken = cookie.split(';')[0].split('=')[1]

    data = {
        'username':'Jiao',
        'password':'123456',
        'csrfmiddlewaretoken':csrftoken
    }
    print(csrftoken)

    hdr = {
        'Origin': 'http://www.heibanke.com',
        'Upgrade-Insecure-Requests': '1',
        'Cookie' : 'csrftoken=' + csrftoken,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }

    #模拟登录
    req = request.Request(login_url, parse.urlencode(data).encode('utf-8'),headers=hdr)
    resp = request.urlopen(req)

    cookie = resp.getheaders('Set-Cookie')
    csrftoken = cookie.split(';')[0].split('=')[1]



execute()