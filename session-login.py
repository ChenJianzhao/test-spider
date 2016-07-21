from urllib import request, parse
import requests


def execute():
    login_url = 'http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex04/'
    url = 'http://www.heibanke.com/lesson/crawler_ex04/'
    # 获取登录页
    s = requests.session()
    csrftoken = s.get(login_url).cookies['csrftoken']

    # print(csrftoken)

    data = {
        'username': 'Jiao',
        'password': '123456',
        'csrfmiddlewaretoken': csrftoken
    }
    hdr = {
        'Cookie': 'csrftoken=' + csrftoken,
    }

    # 模拟登录
    csrftoken = s.post(login_url,data).cookies['csrftoken']
    print(csrftoken)



execute()