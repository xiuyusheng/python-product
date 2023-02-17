import requests
import time
import re
import json
import password_RSA

def cookie(head):
    url = 'https://gitee.com/login'
    res = requests.get(url=url, headers=head)
    authenticity_token = re.search(
        r'<meta name="csrf-token" content="(?P<token>.*?)"', res.text).group('token')
    cookie = res.cookies.get_dict()
    # cookie['slide_id'] = '9'
    # cookie['tz'] = 'Asia%2FShanghai'
    # # cookie['Hm_lvt_24f17767262929947cc3631f99bfd274'] = str(int(time.time()))
    # cookie['close_wechat_tour'] = 'true'
    # cookie['sensorsdata2015jssdkcross'] = '%7B%22distinct_id%22%3A%221857b9894c2a03-0aa9aa74ba4229-26021151-921600-1857b9894c31371%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%22185777378709a5-02eea703b8ec8ba-26021151-1024000-18577737871bdd%22%7D'
    pulic_key = re.search(r'"password_key":"(?P<pu_key>.*?)"',
                          res.text).group('pu_key').replace('\\n','\n')
    print(cookie)
    return (cookie, authenticity_token, pulic_key)


def check_user_login(cookie, head, token):
    url = 'https://gitee.com/check_user_login'
    head['Content-Security-Policy'] = 'frame-ancestors \'self\' https://*.gitee.com'
    head['Content-Type'] = 'application/x-www-form-urlencoded'
    head['Referer'] = 'https://gitee.com/login'
    head['X-CSRF-Token'] = token
    head['X-Requested-With']='XMLHttpRequest'
    data = {
        'user_login': '17676520416'
    }
    res = requests.post(url=url, headers=head, cookies=cookie, data=data)
    print(res.text)
    print(res.cookies.get_dict())
    return res.cookies.get_dict()

# def login(cookie):
#     url = 'https://gitee.com/login'
#     head = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'zh-CN,zh;q=0.9',
#         'Cache-Control': 'max-age=0',
#         'Connection': 'keep-alive',
#         'Content-Length': '448',
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'Cookie': cookie,
#         'Host': 'gitee.com',
#         'Origin': 'https://gitee.com',
#         'Referer': 'https://gitee.com/login',
#         'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': "Windows",
#         'Sec-Fetch-Dest': 'document',
#         'Sec-Fetch-Mode': 'navigate',
#         'Sec-Fetch-Site': 'same-origin',
#         'Sec-Fetch-User': '?1',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
#     }


def head_(cookie, token, public_key):
    url='https://gitee.com/login'
    head = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '444',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'gitee.com',
        'Origin': 'https://gitee.com',
        'Referer': 'https://gitee.com/login',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    param = {
        'encrypt_key': 'password',
        'utf8': '%E2%9C%93',
        'authenticity_token': token,
        'redirect_to_url': '',
        'user[login]': '17676520416',
        'encrypt_data[user[password]]': password_RSA.encrpt(f'{token[-8:]}$gitee$20030216abc', public_key),
        'user[remember_me]': '0'
    }
    res = requests.post(url=url, headers=head, data=param, cookies=cookie)
    print(res.status_code)


if __name__ == "__main__":
    head = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'gitee.com',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
    }
    cookie1, token, public_key = (cookie(head))
    cookie2 = check_user_login(cookie=cookie1, token=token, head=head)
    head_(cookie=cookie2, token=token, public_key=public_key)
