import requests
import login_token
import datetime
import time
import re
# token=login_token.token()#青年大学习网页token
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
    f"https://tuanapi.12355.net/login/adminLogin?userName=xg21rjb&password=xg21rj_b&loginValidCode=&_={int(time.time()*1000)}",
    headers=head1)
# print(resp.headers)
cookie = resp.headers['Set-Cookie']

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
resp5=requests.get(f'https://tuanapi.12355.net/questionnaire/getPcYouthLearningUrl?_={int(time.time()*1000)}',headers=head)
# print(resp5.text)
resp5_json=resp5.json()
youthLearningUrl=resp5_json['youthLearningUrl']
# print(youthLearningUrl)
zhtjToken=re.search(r'zhtjToken=(?P<token>.*)',youthLearningUrl).group('token')
# print(token.group('token'))
head_token={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
'X-Litemall-Admin-Token': 'Nc6T2bF76X2wN6BSqsBnjFEk81FdNMkQDSW6cPmsLyH55DUWlOI3xrUhgews fGAfYXYBnE9SLgBIzNOQ4gnZEexKsEOY8Nxvv8Lzv+2Mm/NfDy70D6nQw4LL vKDcoDfXtwi/y/8WBqyy7zAWtgGKqINQENX80o6qiKHrqBaa1oeYjhAkxte5 CnZ/FIGUedhOV5543S5fHEwaO4XRav5QKFMT59QHXQP0xmmx8Q5BF/s=',
'X-Litemall-IdentiFication': 'young'
}
token_resp=requests.get(f'https://youthstudy.12355.net/apibackend/admin/zhtj/admin/login?zhtjToken={zhtjToken}',headers=head_token).json()
token=token_resp['data']['entity']['token']
MyclassName = {
    '李佳泉': 2106200202,
    '曾勇辉': 2106200204,
    '吴玉萍': 2106200205,
    '叶俊威': 2106200206,
    '陈美静': 2106200207,
    '林育生': 2106200209,
    '胡梦芹': 2106200213,
    '郑腾跃': 2106200214,
    '庄佳胜': 2106200215,
    '李灿植': 2106200216,
    '林炼培': 2106200218,
    '孙湃钒': 2106200219,
    '卢敏如': 2106200222,
    '阮宇航': 2106200223,
    '蔡梓沛': 2106200226,
    '郭卓佳': 2106200231,
    '林曼如': 2106200232,
    '林小荣': 2106200235,
    '方洪宇': 2106200236,
    '郑凯立': 2106200237,
    '钟广源': 2106200238,
    '邓林彬': 2106200239,
    '刘纯娜': 2106200240,
    '李铧斌': 2106200245,
    '李健宏': 2106200246,
    '李硕': 2106200248,
    '林杰鹏': 2106200253,
    }
try:
    
    head3 = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27',
        'X-Litemall-IdentiFication': 'young'
    }
    resp4 = requests.post(f'https://youthstudy.12355.net/apibackend/user/info?token={token}',headers=head3)
                        
    # print(resp4.text)
    resp4_json = resp4.json()

    organizeId = resp4_json['data']['entity']['organizeId']  #organizeId
    head2 = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27',
        'X-Litemall-Admin-Token':
        token,
        'X-Litemall-IdentiFication': 'young'
    }
    for i in range(1,3):
        resp3 = requests.get(
            f'https://youthstudy.12355.net/apibackend/admin/young/organize/userList?organizedId={organizeId}&member=0&pageNo={i}',
            headers=head2)
        List = resp3.json()
        
        for i in List['data']['list']:
            del MyclassName[i['name']]
            
    # print("青年大学习未学习名单：")
    resp4=requests.get(f'https://youthstudy.12355.net/apibackend/admin/young/organize/sort/count?idList={organizeId}',headers=head2)
    learn_numbers=resp4.json()
    tuan_learn_number=learn_numbers['data']['entity']['resultList'][0]['data']['learns']
    qun_learn_number=learn_numbers['data']['entity']['resultList'][0]['data']['thisLearnsMasses']
    a='青年大学习未学习名单：<br/>群众未学：'+str(20-int(qun_learn_number))+'名<br/>团员未学：'+str(27-int(tuan_learn_number))+'名<br/>'
    for i in MyclassName:
        a+=str(i)+'&nbsp;&nbsp;&nbsp;&nbsp;'+str(MyclassName[i])+'<br/>'
        # print(i,MyclassName[i])

    # for i in List['data']['list']:

    #     a+=i['name']+'<br/>'
    #     print(i['name'])
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
        f"https://tuanapi.12355.net/login/adminLogin?userName=xg21rjb&password=xg21rj_b&loginValidCode=&_={int(time.time()*1000)}",
        headers=head1)
    # print(resp.headers)
    cookie = resp.headers['Set-Cookie']
    head1={
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
    resp1=requests.get(f'https://tuanapi.12355.net/login/getSessionAccount?_={int(time.time()*1000)}',headers=head1)
    resp1_json=resp1.json()
    oid=resp1_json['account']['oid']
    # print(resp1_json['account']['oid'])
    study_url='https://wjxt.12355.net/h5/#/?organizeId='+str(oid)+'&time='+str(int(time.time()))
    datetimes=datetime.datetime.now()
    date_yeas=str(datetimes.year)
    date_month=str(datetimes.month)
    if datetimes.month<10:
        date_yeas_month=date_yeas+'0'+date_month
    else:
        date_yeas_month=date_yeas+date_month

    resp2=requests.get(f'https://tuanapi.12355.net/api/v1/admin/group-fee/date/202209?date={date_yeas_month}&sub=0&param={oid}&_={int(time.time()*1000)}',headers=head1)
    resp2_json=resp2.json()
    a+='应缴费人数：'+str(resp2_json['listData'][0]['realTotal'])+'<br/>已缴费人数：'+str(resp2_json['listData'][0]['paidIn'])+'<br/>当月缴纳总额：'+resp2_json['listData'][0]['paidInAmount']+'<br/><br/>青年大学习链接：<br/>'+study_url
except:
    a='token已过期'
print(a)