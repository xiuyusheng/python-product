from email import header
from posixpath import split
from tokenize import maybe
from typing import List
import requests
import time
import re
def token(class_):
    head1 = {
        'Accept':
        'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':
        'gzip, deflate, br',
        'Accept-Language':
        'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection':
        'keep-alive',
        'Host':
        'tuanapi.12355.net',
        'Origin':
        'https://tuan.12355.net',
        'Referer':
        'https://tuan.12355.net/',
        'sec-ch-ua':
        '"Microsoft Edge";v="105", " Not;A Brand";v="99", "Chromium";v="105"',
        'sec-ch-ua-mobile':
        '?0',
        'sec-ch-ua-platform':
        '"Windows"',
        'Sec-Fetch-Dest':
        'empty',
        'Sec-Fetch-Mode':
        'cors',
        'Sec-Fetch-Site':
        'same-site',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'
    }
    # print(int(time.time()))
    resp = requests.get(
        f"https://tuanapi.12355.net/login/adminLogin?userName={class_[0]}&password={class_[1]}&loginValidCode=&_={int(time.time()*1000)}",
        headers=head1)
    # print(resp.headers)
    cookie = resp.headers['Set-Cookie']#登录广东智慧团建获得Cookie
    return cookie