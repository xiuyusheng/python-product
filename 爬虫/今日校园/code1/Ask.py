import requests
import re
import login
cookie=login.login()
data={
  "pageNumber": 1,
  "pageSize": 20,
  "startDate": "",
  "endDate": "",
  "moduleCode": "3",
  "creatorWid": "",
  "signType": "",
  "sortColumn": "",
  "content": ""
}
headers={
 'Accept': 'application/json, text/plain, */*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
'Connection': 'keep-alive',
'Cookie': cookie,
'Referer': 'https://gpc.campusphere.net/wec-counselor-apps/counselor/mobile-v2/index.html',
'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (4479773184) cpdaily/9.2.1 wisedu/9.2.1',
'X-Requested-With': 'XMLHttpRequest'
}
url='https://gpc.campusphere.net/wec-counselor-apps/counselor/homepage/getFollowsInProgress'
resp1=requests.post(url=url,headers=headers,json=data)
#print(resp1.text)
one_resp=resp1.json()
for i in one_resp['datas']['rows']:
 #print(i['mobileUrl'])
 id=re.search(r'id=(?P<id>.*)',i['mobileUrl']).group('id')
 #print(id)
 url=f'https://gpc.campusphere.net/wec-counselor-leave-apps/leaveadmin/tch/detail/{id}/1'
 ly=requests.get(url=url,headers=headers)
 xq=ly.json()
 userid=xq['datas']['main']['userId']
 print('姓名:'+xq['datas']['main']['userName']+'\n'+f'学号:{userid}')
 print('理由:'+xq['datas']['main']['leaveReason'])
