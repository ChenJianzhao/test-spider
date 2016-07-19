# coding=utf-8
import re, tool;
import pytesseract
from urllib import request, parse
from PIL import Image

from tool import time_decorato

CAPTCHA_0 = 'captcha_0'
CAPTCHA_1 = 'captcha_1'
CSRFMIDDLEWARETOKEN = 'csrfmiddlewaretoken'
IMAGE_URL = 'image_url'
MSG = 'msg'
PASSWORD = 'password'

def test():
    pass


def parse_response(resp):

    result = {}
    html = resp.read().decode('utf-8')

    #构建正则表达式
    token_str = '<input id="id_captcha_0" name="captcha_0" type="hidden" value="(.*?)" />'
    image_str = '<img src="(.*?)" alt="captcha" class="captcha" />'
    msg_str = '<h3>(.*?)</h3>'

    token_pattern = re.compile(token_str)
    image_pattern = re.compile(image_str)
    msg_pattern = re.compile(msg_str)

    #获取页面上的数据
    msg = re.findall(msg_pattern, html)[0]
    result[MSG] = msg
    if msg == '恭喜! 用户JIAN成功闯关, 后续关卡敬请期待':
       return result
    captcha_0 = re.findall(token_pattern,html)[0]
    cookie = resp.getheader('Set-Cookie')
    csrfmiddlewaretoken = cookie.split(';')[0].split('=')[1]
    image_url = re.findall(image_pattern,html)[0]

    result[CAPTCHA_0] = captcha_0
    result[CSRFMIDDLEWARETOKEN] = csrfmiddlewaretoken
    result[IMAGE_URL] = 'http://www.heibanke.com' + image_url
    # result[IMAGE_URL] = image_url

    return result


def build_post_data(result):
    data = {
        'csrfmiddlewaretoken' : result[CSRFMIDDLEWARETOKEN],
        'username' : 'JIAN',
        'password' : result[PASSWORD],
        'captcha_0': result[CAPTCHA_0],
        'captcha_1' : result[CAPTCHA_1]
    }
    return parse.urlencode(data).encode('utf-8')


def parse_image(image_url):
    code_str = '[A-Z]{4}'
    code_pattren = re.compile(code_str)
    while(True):
        request.urlretrieve(image_url,'%s.png' % 1)
        image = Image.open(r'1.png')
        vcode = pytesseract.image_to_string(image,lang='eng')

        if re.findall(code_pattren,vcode).__len__() > 0:
            break
    return vcode


def ex_04():
   msg, password = execute()
   print( '%s,，密码为%s' % (msg, password))

@time_decorato
def execute():
     #访问登录页面
    url = 'http://www.heibanke.com/lesson/crawler_ex04/'
    hdr = {
        'Cookie' : 'sessionid=2g3x9k93advx27hrnqpm5kmypzidgi3f; csrftoken=ZURvSZ074OL0M6fjmRltTsQ1ch428Yty; Hm_lvt_74e694103cf02b31b28db0a346da0b6b=1467723505,1468398255; Hm_lpvt_74e694103cf02b31b28db0a346da0b6b=1468406006'
    }
    req = request.Request(url,headers=hdr)
    resp = request.urlopen(req)
    i = 0

    while(True):

        result = parse_response(resp)
        msg = result[MSG]
        #密码错误
        if msg == '您输入的密码错误, 请重新输入':
            i += 1
            result[PASSWORD] = str(i)

        #验证码错误
        elif msg =='加了验证码' or msg == '验证码输入错误':

            captcha_1 = parse_image(result[IMAGE_URL])
            result[CAPTCHA_1] = captcha_1
            result[PASSWORD] = str(i)

            post_data = build_post_data(result)
            req = request.Request(url, post_data, headers=hdr)
            resp = request.urlopen(req)

        #正确
        else:
            return (msg, i)

ex_04()