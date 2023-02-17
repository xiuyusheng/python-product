import requests
import time
import chaojiying
import re
from datetime import timedelta
url_login_cookie = 'http://passport2.chaoxing.com/login?fid=&newversion=true&refer=http://i.chaoxing.com'
head_login_cookie = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':
    'gzip, deflate',
    'Accept-Language':
    'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control':
    'max-age=0',
    'Connection':
    'keep-alive',
    'Host':
    'passport2.chaoxing.com',
    'Upgrade-Insecure-Requests':
    '1',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
}
response_login_cookie=requests.get(url=url_login_cookie,headers=head_login_cookie)
cookies_=response_login_cookie.headers['Set-Cookie'].split(',')
cookies_1=''
for i in cookies_:
    cookies_1+=i.split(';')[0]+';'
response_login_cookie.close()
head_yzm = {
    'Accept':
    'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Encoding':
    'gzip, deflate',
    'Accept-Language':
    'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection':
    'keep-alive',
    'Cookie':
    'fid=111814;'+cookies_1+' source=""',
    'Host':
    'passport2.chaoxing.com',
    'Referer':
    'http://passport2.chaoxing.com/login?loginType=3&newversion=true&fid=-1&hidecompletephone=0&ebook=0&allowSkip=0&refer=http%3A%2F%2Fi.chaoxing.com&accounttip=&pwdtip=&doubleFactorLogin=0&independentId=0',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
}
resp_yzm = requests.get(
    f'https://passport2.chaoxing.com/num/code?{int(time.time()*1000)}',
    headers=head_yzm)
resp_yzm.close()
yzm = chaojiying.yz(resp_yzm.content)['pic_str']
data_login = {
    'pid': '-1',
    'fid': '111814',
    'uname': '2106200248',
    'numcode': yzm,
    'password': 'cf49ffbb105bc6214cfc33620fedd8d7',
    'refer': 'http%3A%2F%2Fi.chaoxing.com',
    't': 'true',
    'hidecompletephone': '0',
    'doubleFactorLogin': '0',
    'independentId': '0'
}
head_login = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Length': '192',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':
    'fid=111814;'+cookies_1+' source=""',
    'Host': 'passport2.chaoxing.com',
    'Origin': 'http://passport2.chaoxing.com',
    'Referer':
    'https://passport2.chaoxing.com/login?loginType=3&newversion=true&fid=-1&hidecompletephone=0&ebook=0&allowSkip=0&refer=http%3A%2F%2Fi.chaoxing.com&accounttip=&pwdtip=&doubleFactorLogin=0&independentId=0',
    'sec-ch-ua':
    '"Microsoft Edge";v="105", " Not;A Brand";v="99", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',
    'X-Requested-With': 'XMLHttpRequest'
}
resp_login = requests.post('https://passport2.chaoxing.com/unitlogin',
                            headers=head_login,
                            data=data_login)
cookie_ = resp_login.headers['Set-Cookie']
domain = re.search(r'Expires=(?P<domain>.*?),', cookie_)
cookies = re.split(',', cookie_)
a = 0
cookie2 = 'browserLocale=zh_CN; fid=111814; route=52ffa9af7a380e114204ed76732d509c; JSESSIONID=637492354023BBF0789B4C1E82C71486; source="";'
for i in cookies:
    if a % 2 == 0:
        cookie2 += i
    a += 1
cookie__ = cookie2.replace(
    'Domain=.chaoxing.com; Expires=' + domain.group('domain'),
    '') + 'spaceRoleId=""'  
resp_login.close()
head_data = {
    'Cookie': cookie__,
    'Host': 'notice.chaoxing.com',
    'Origin': 'http://notice.chaoxing.com',
    'Referer':
    'http://notice.chaoxing.com/pc/notice/myNotice?s=e4451fe92bf83f32493a27c42c8d7edb',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',
    'X-Requested-With': 'XMLHttpRequest'
}
data_data = {
    'type': '2',
    'notice_type': '',
    'lastValue': '',
    'sort': '',
    'folderUUID': '',
    'kw': '',
    'startTime': '',
    'endTime': '',
    'gKw': '',
    'gName': '',
    'year': '2022'
}
resp_data = requests.post(
    'http://notice.chaoxing.com/pc/notice/getNoticeList',
    headers=head_data,
    data=data_data)
resp_data.close()
datas = resp_data.json()#获取课程表单
num=0
for i in datas['notices']['list']:
    from datetime import datetime
    datetime_object = datetime.strptime(i['sendTime'], '%Y-%m-%d %H:%M:%S')#将获获取到的任务发送时间字符串转换为时间格式
    import datetime
    now = datetime.datetime.now()  #当前日期
    this_week_start = now - timedelta(days=now.weekday())  #本周开始第一天2022-9-12
    this_week_end = now + timedelta(days=6 - now.weekday())  #本周的最后一天2022-9-18
    sult = datetime_object > this_week_start and datetime_object < this_week_end
    print(sult)
    if sult:#对任务发送时间是否是在本周，是则将任务打印出来
        print(str(i['content']).replace('\r', '\n'))
        num+=1
if not num:
    print('本周超星没有作业')
