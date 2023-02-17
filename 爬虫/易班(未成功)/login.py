from email import header
from http.client import responses
import json
from tokenize import group
import requests
import time
import password_RSA
import re


def public():
    url_public = 'https://www.yiban.cn/login?go=https://www.yiban.cn'
    header_public = {
        'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':
        'gzip, deflate, br',
        'Accept-Language':
        'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control':
        'max-age=0',
        'Host':
        'www.yiban.cn',
        'sec-ch-ua':
        '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile':
        '?0',
        'sec-ch-ua-platform':
        "Windows",
        'Sec-Fetch-Dest':
        'document',
        'Sec-Fetch-Mode':
        'navigate',
        'Sec-Fetch-Site':
        'none',
        'Sec-Fetch-User':
        '?1',
        'Upgrade-Insecure-Requests':
        '1',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34'
    }
    response_public = requests.get(url=url_public, headers=header_public)
    # print(response_public.headers)
    result = []
    public_ = re.search(
        r'<ul class="login-pr clearfix" id="login-pr" data-keys=\'(?P<public>.*?)\' data-keys-time=\'(?P<keytime>.*?)\'',
        response_public.text, re.S)
    result.append(public_.group('keytime'))
    result.append(public_.group('public'))
    print(response_public.headers)
    first_cookie = response_public.headers['Set-Cookie']
    first_cookie = 'YB_SSID=' + first_cookie.split('YB_SSID=')[1].split(';')[0]
    result.append(first_cookie)
    # print(first_cookie)
    # print('public',result[1],sep=':')
    # print(round(time.time(),2))
    return result


def login(public):
    password = password_RSA.stay('20030216abc', public[1])
    # print(password)
    url_login = 'https://www.yiban.cn/login/doLoginAjax'
    data_login = {
        'account': '17676520416',
        'password': password,
        'captcha': '',
        'keysTime': public[0]
    }
    header_login = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '246',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': public[2],
        'Host': 'www.yiban.cn',
        'Origin': 'https://www.yiban.cn',
        'Referer':
        'https://www.yiban.cn/login?go=https%3A%2F%2Fwww.yiban.cn%2F',
        'sec-ch-ua':
        '"Microsoft Edge";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34',
        'X-Requested-With': 'XMLHttpRequest'
    }
    # header_login = {
    #     'Accept': 'application/json, text/javascript, */*; q=0.01',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    #     'Connection': 'keep-alive',
    #     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    #     'Host': 'www.yiban.cn',
    #     'Origin': 'https://www.yiban.cn',
    #     'Referer':
    #     'https://www.yiban.cn/login?go=https%3A%2F%2Fwww.yiban.cn%2F',
    #     'sec-ch-ua-mobile': '?0',
    #     'sec-ch-ua-platform': "Windows",
    #     'Sec-Fetch-Dest': 'empty',
    #     'Sec-Fetch-Mode': 'cors',
    #     'Sec-Fetch-Site': 'same-origin',
    #     'User-Agent':
    #     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34',
    #     'X-Requested-With': 'XMLHttpRequest'
    # }
    response_login = requests.post(url=url_login,
                                   headers=header_login,
                                   data=json.dumps(data_login))
    # print(json.dumps(header_login))
    print(response_login.json())
    print(response_login.headers)


# get_first_cookie()
# public()
# for i in range(5):
public_ = public()
public=['''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC94bo2nd9Uk+pP2zH0pEoChFQy
QiWNe+UPS3IDnNp/t9582dl1wnPdTJ0ve75PKvXVkJn+e76/qHcy+XMVs0/QYsyC
dHlpduY3vSrPJxbUVGxrY9LZtvm1MpVBWu9Es1iDBcmp2HIgWn2NUDV29nPZRb//
+EMVBOOtKBKcPC0iEwIDAQAB
-----END PUBLIC KEY-----''','1665723142.19','https_waf_cookie=2bc76c8d-38fb-483967c8296e3a1894819ce790d3a066401c; YB_SSID=264df06a88a9acf26b5ac15be432127f']
print(public_)
login(public_)
