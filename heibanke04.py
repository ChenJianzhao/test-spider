# coding=utf-8
from urllib import request, parse
import re

def test():
    pass


def parse_login_page(self, captcha_0, csrfmiddlewaretoken):
    url = 'http://www.heibanke.com/lesson/crawler_ex04/'
    resp = request.urlopen(url)
    html = resp.read().decode('utf-8')
    reStr = '<input id="id_captcha_0" name="captcha_0" type="hidden" value="(.*)" />'
    pattern = re.compile(reStr)
    captcha_0 = re.findall(pattern)[0]
    cookie = resp.getheader().get('Set-Cookie')
    csrfmiddlewaretoken = cookie.split(';')[0].split('=')[1]

