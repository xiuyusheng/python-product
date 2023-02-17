from asyncio.windows_events import NULL
from http.client import responses
import numbers
from turtle import width
import requests
import login__zhtj
import re
import os
class_={
    #软件技术
    'rja':'rj_a',
    'rjb':'rj_b',
    'rjc':'rj_c',
    'rjd':'rj_d',
    'rje':'rj_e',
    'rjf':'rj_f',
    #计算机应用技术
    'jya':'jy_a',
    'jyb':'jy_b',
    'jyc':'jy_c',
    'jyd':'jy_d',
    'jye':'jy_e',
    #计算机网络技术
    'jwa':'jw_a',
    'jwb':'jw_b',
    'jwc':'jw_c',
    'jwd':'jw_d',
    'jwe':'jw_e',
    #数字媒体技术
    'sma':'sm_a',
    'smb':'sm_b',
    'smc':'sm_c',
    'smd':'sm_d',
    'txa':'tx_a',
    'txb':'tx_b',
    'txc':'tx_c',
    #现代通信技术
    'txa':'tx_a',
    'txa':'tx_a',
    'txa':'tx_a',
    'txa':'tx_a',
    'txa':'tx_a',
    'txa':'tx_a',
}
Grade=['xg20','xg21','xg22']
max_=[0,'']#设定最大值
def send(page,cla):
    head = {
        'Accept':
        'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':
        'gzip, deflate, br',
        'Accept-Language':
        'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'authorize_name':
        '15749857',
        'Connection':
        'keep-alive',
        'Content-Length':
        '24',
        'Content-Type':
        'application/json',
        'Cookie':
        login__zhtj.token(cla),
        'Host':
        'tuanapi.12355.net',
        'Origin':
        'https://tuan.12355.net',
        'Referer':
        'https://tuan.12355.net/',
        'sec-ch-ua':
        '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile':
        '?0',
        'sec-ch-ua-platform':
        "Windows",
        'Sec-Fetch-Dest':
        'empty',
        'Sec-Fetch-Mode':
        'cors',
        'Sec-Fetch-Site':
        'same-site',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26'
    }
    url = 'https://tuanapi.12355.net/api/v1/admin/members/page'
    data = {'page': page, 'pageSize': '20'}
    responses=requests.post(url=url,headers=head,json=data).json()
    aabb=0
    try:#防止班级不存在
        for i in responses['listData']:
            num=int(i['volunteerServiceHours'])
            # global max_
            if(num>max_[0]):
                max_[0]=num
                max_[1]=i['name']
            if(int((num-num%60)/60)>=100):
                aabb+=1
            num=str(int(num/60))+'小时'+str(num%60)+'分钟'
            
            print(i['name'],str(num),sep='\t\t\t')
    except:
        print('无'+cla[0]+'班级')
        pass
    return aabb
for k in Grade:#年级切换
    for j in class_:#班级切换
        print(k+j)
        num=0
        for i in [1,2,3]: #翻页访问
            num+=send(i,[k+j,k+class_[j]])
        print('超过100时长有:'+str(num)+'人')
print(f'-----时长最长为：{max_[1]}————>{str(int(max_[0]/60))}小时{str(max_[0]%60)}分钟-----')
os.system("pause")

