import requests
import time
import re
import ddddocr
ocr = ddddocr.DdddOcr()
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
def ValidCode():
    url="https://tuanapi.12355.net/login/loginValidCode?t=1698160315047"
    resp=requests.get(url,headers=head1)
    validcode=ocr.classification(resp.content)
    return validcode
def token():
    
    # print(int(time.time()))
    resp = requests.get(
        f"https://tuanapi.12355.net/login/adminLogin?userName=xg21rja&password=a4e3e4d7c0ff35e90e529a2287259785&loginValidCode={ValidCode()}&_={int(time.time()*1000)}",
        headers=head1)
    # print(resp.headers)
    cookie = resp.headers['Set-Cookie']#登录广东智慧团建获得Cookie
    # print(resp.text)
    # print(cookie)
    head = {
        'Accept':
        'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':
        'gzip, deflate, br',
        'Accept-Language':
        'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection':
        'timeout=20',
        'Cookie':
        cookie,
        'Host':
        'tuanapi.12355.net',
        'Origin':
        'https://tuan.12355.net',
        'Referer':
        'https://tuan.12355.net/',
        'sec-ch-ua':
        'Microsoft Edge;v=105, Not;A Brand;v=99, Chromium;v=105',
        'sec-ch-ua-mobile':
        '?0',
        'sec-ch-ua-platform':
        'Windows',
        'Sec-Fetch-Dest':
        'empty',
        'Sec-Fetch-Mode':
        'cors',
        'Sec-Fetch-Site':
        'same-site',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'
    }
    resp5=requests.get(f'https://tuanapi.12355.net/questionnaire/getPcYouthLearningUrl?_={int(time.time()*1000)}',headers=head)#请求青年大学习网页链接
    print(resp5.text)
    resp5_json=resp5.json()
    youthLearningUrl=resp5_json['youthLearningUrl']
    zhtjToken=re.search(r'zhtjToken=(?P<token>.*)',youthLearningUrl).group('token')#提取访问首页面链接所用的token
    # print(token.group('token'))
    head_token={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'X-Litemall-Admin-Token': 'Nc6T2bF76X2wN6BSqsBnjFEk81FdNMkQDSW6cPmsLyH55DUWlOI3xrUhgews fGAfYXYBnE9SLgBIzNOQ4gnZEexKsEOY8Nxvv8Lzv+2Mm/NfDy70D6nQw4LL vKDcoDfXtwi/y/8WBqyy7zAWtgGKqINQENX80o6qiKHrqBaa1oeYjhAkxte5 CnZ/FIGUedhOV5543S5fHEwaO4XRav5QKFMT59QHXQP0xmmx8Q5BF/s=',
    'X-Litemall-IdentiFication': 'young'
    }
    token_resp=requests.get(f'https://youthstudy.12355.net/apibackend/admin/zhtj/admin/login?zhtjToken={zhtjToken}',headers=head_token).json()#请求青年大学习后所用的真正token
    token=token_resp['data']['entity']['token']
    return token
