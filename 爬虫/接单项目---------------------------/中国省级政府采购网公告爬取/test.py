import requests
import os
import pdfkit
import time
import datetime
from bs4 import BeautifulSoup
# def Data_time(data_time):
#     timestamp = data_time / 1000  # 将毫秒转换为秒
#     dt = datetime.datetime.fromtimestamp(timestamp)
#     date_str = dt.strftime("%Y-%m-%d")
#     return(date_str)
if __name__ == "__main__":
    num = 0
    session = requests.Session()
    head = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Host': 'zfcgmanager.czt.zj.gov.cn',
        'Origin': 'https://zfcg.czt.zj.gov.cn',
        'Referer': 'https://zfcg.czt.zj.gov.cn/',
        'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
    }
    path_wkhtmltopdf = r'wkhtmltopdf\bin\wkhtmltopdf.exe'
    html_=session.get('https://zfcg.czt.zj.gov.cn/purchaseNotice/index.html?_={}'.format(int(time.time())*1000)).text
    soup=BeautifulSoup(html_,'html.parser')
    for i in range(1, 100):
        ID_=''
        aa=soup.find('select',{'class':'hls form_item hide noticeType'}).find_all('option')
        ID_=(aa[12]['value'])
            
        params = {
            'pageSize': '100',
            'pageNo': i,
            'sourceAnnouncementType': ID_,
            'isGov': 'true',
            'keyword': '保险',
            'isExact': '1',
            'pubDate': '2015-01-01 ',
            'endDate': '2021-12-01 ',
            'url': 'notice'
        }
        url = 'https://zfcgmanager.czt.zj.gov.cn/cms/api/cors/remote/results'
        resp = session.get(url=url, headers=head, params=params).json()
        print(resp)
        for j in resp['articles']:
            noticeId=j['id']
            print(noticeId)
            url_='https://zfcgmanager.czt.zj.gov.cn/cms/api/cors/remote/results?noticeId={}&utm&url=noticeDetail'.format(noticeId)
            resp_=session.get(url=url_,headers=head).json()
            # print(resp_['noticeTitle'])
            public_time=resp_['noticePubDate']#发布时间
            if '车' in resp_['noticeTitle'] or '医疗' in resp_['noticeTitle']:
                print('-----------------------错误-----------------------')
                continue
            elif '保险' in resp_['noticeTitle']:
                num+=1
                print(resp_['noticeTitle'])
                noticeTitle=resp_['noticeTitle'].replace('\n','').replace('“','').replace('”','').replace('/','')
                print(noticeTitle)
                with open('HL/{}.html'.format(noticeTitle),'w',encoding='utf-8') as f:
                    f.write('<p style="float: right;border: 2px solid black;">发布时间：&nbsp; &nbsp;{}</p>'.format(public_time)+resp_['noticeContent'])

                config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
                try:
                    pdfkit.from_file('HL/{}.html'.format(noticeTitle), 'HL_pdf/{}.pdf'.format(noticeTitle), configuration=config,options={'encoding': 'utf-8'})
                except:
                    time.sleep(1)
                    pdfkit.from_file('HL/{}.html'.format(noticeTitle), 'HL_pdf/{}.pdf'.format(noticeTitle), configuration=config,options={'encoding': 'utf-8'})
            else:
                print('+++++++++++++++++++++++淘汰+++++++++++++++++++++++')
    print(num)
