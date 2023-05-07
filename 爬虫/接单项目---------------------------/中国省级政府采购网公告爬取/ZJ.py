import requests
import os
import pdfkit
import time
import datetime
# def Data_time(data_time):
#     timestamp = data_time / 1000  # 将毫秒转换为秒
#     dt = datetime.datetime.fromtimestamp(timestamp)
#     date_str = dt.strftime("%Y-%m-%d")
#     return(date_str)
if __name__=="__main__":
    session=requests.Session()
    head={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
    }
    path_wkhtmltopdf = r'wkhtmltopdf\bin\wkhtmltopdf.exe'
    for i in range(1,100):
        url='https://zfcgmanager.czt.zj.gov.cn/cms/api/cors/remote/results?pageSize=100&pageNo={}&sourceAnnouncementType=3004,4005,4006,4009,8043&isGov=true&pubDate=2015-01-01+&endDate=2021-12-31+&isExact=1&url=notice'.format(i)
        resp=session.get(url=url,headers=head).json()
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
        # print(resp.text)