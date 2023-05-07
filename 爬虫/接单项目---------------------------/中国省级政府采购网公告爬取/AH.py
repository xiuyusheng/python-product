import requests
import os
import pdfkit
import time
import datetime
from selenium import webdriver
import json
import re
def Data_time(data_time):
    timestamp = data_time / 1000  # 将毫秒转换为秒
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt
if __name__ == "__main__":
    session = requests.Session()
    head = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '174',
        'Content-Type': 'application/json;charset=UTF-8',
        'Host': 'www.ccgp-anhui.gov.cn',
        'Origin': 'http://www.ccgp-anhui.gov.cn',
        'Referer': 'http://www.ccgp-anhui.gov.cn/luban/category?parentId=541080&childrenCode=ZcyAnnouncement4&utm=luban.luban-PC-4718.564-pc-websitegroup-nav-front.10.3dbe28a0e2af11ed800bb9caecfd2489',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
        'X-Requested-With': 'XMLHttpRequest'
    }
    path_wkhtmltopdf = r'wkhtmltopdf\bin\wkhtmltopdf.exe'
    for i in range(1, 100):
        url = 'http://www.ccgp-anhui.gov.cn/portal/category'
        data = {
            'categoryCode': "ZcyAnnouncement4",
            'districtCode': None,
            'leaf': None,
            'pageNo': i,
            'pageSize': 100,
            'publishDateBegin': "2015-01-01",
            'publishDateEnd': "2021-12-31",
            '_t': int(time.time())*1000
        }
        resp = session.post(url=url, headers=head, json=data).json()

        for j in resp['result']['data']['data']:
            noticeId = j['articleId']
            print(noticeId)
            head1 = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Host': 'www.ccgp-anhui.gov.cn',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
            }
            params = {
                'articleId': noticeId,
                'timestamp': int(time.time())
            }
            url_ = 'http://www.ccgp-anhui.gov.cn/portal/detail'
            resp_ = session.get(url=url_, headers=head1,params=params).json()['result']['data']
            if '车' in resp_['title'] or '医疗' in resp_['title']:
                print('-----------------------错误-----------------------')
                continue
            elif '保险' in resp_['title']:
                noticeTitle=resp_['title'].replace('\n','').replace('“','').replace('”','').replace('/','').replace('[','(').replace(']',')')
                print(noticeTitle)
                with open('HL2/{}.html'.format(noticeTitle),'w',encoding='utf-8') as f:
                    f.write('<p style="float: right;border: 2px solid black;">发布时间：&nbsp; &nbsp;{}</p>'.format(Data_time(resp_['publishDate']))+re.sub(re.compile(r'face=".*?"'), 'face="宋体"',resp_['content']).replace('仿宋','宋体').replace('黑体','宋体'))
                config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
                try:
                    pdfkit.from_file('HL2/{}.html'.format(noticeTitle), 'HL2_pdf/{}.pdf'.format(noticeTitle), configuration=config,options={'encoding': 'utf-8'})
                except:
                    time.sleep(3)
                    pdfkit.from_file('HL2/{}.html'.format(noticeTitle), 'HL2_pdf/{}.pdf'.format(noticeTitle), configuration=config,options={'encoding': 'utf-8'})
            else:
                print('+++++++++++++++++++++++淘汰+++++++++++++++++++++++')