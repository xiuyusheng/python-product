import requests
import time
import datetime
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
print(resp1_json)
oid=resp1_json['account']['oid']
print(resp1_json['account']['oid'])
datetimes=datetime.datetime.now()
date_yeas=str(datetimes.year)
date_month=str(datetimes.month)
if datetimes.month<10:
    date_yeas_month=date_yeas+'0'+date_month
else:
    date_yeas_month=date_yeas+date_month

resp2=requests.get(f'https://tuanapi.12355.net/api/v1/admin/group-fee/date/202209?date={date_yeas_month}&sub=0&param={oid}&_={int(time.time()*1000)}',headers=head1)
resp2_json=resp2.json()
print('应缴费人数：'+str(resp2_json['listData'][0]['realTotal'])+'\n已缴费人数：'+str(resp2_json['listData'][0]['paidIn'])+'\n当月缴纳总额：'+resp2_json['listData'][0]['paidInAmount'])
