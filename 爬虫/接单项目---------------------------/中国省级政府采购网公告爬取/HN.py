import requests
import os
import pdfkit
import time
from datetime import date,timedelta,datetime
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
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '137',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'ccgp-hunan.gov.cn',
        'Origin': 'http://ccgp-hunan.gov.cn',
        'Referer': 'http://ccgp-hunan.gov.cn/page/notice/moreCityCounty.jsp?prcmMode=01',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
        'X-Requested-With': 'XMLHttpRequest'
    }
    path_wkhtmltopdf = r'wkhtmltopdf\bin\wkhtmltopdf.exe'
    startDate='2019-01-01'
    endDate='2019-12-31'
    for i in range(1, 3):
        
        url = 'http://ccgp-hunan.gov.cn/mvc/getNoticeList4Web.do'

        data = {
            'nType': 'dealNotices',
            'pType': '',
            'prcmPrjName': '',
            'prcmItemCode': '',
            'prcmOrgName': '',
            'startDate': str(startDate),
            'endDate': str(endDate),
            'city': '',
            'county': '',
        }
        resp = session.post(
            url='http://ccgp-hunan.gov.cn/mvc/getNoticeListOfCityCountyCount.do', headers=head, data=data).json()
        # print(resp)
        # break
        data.pop('city')
        data.pop('county')
        for p in range(1,round(resp['count']/18)+1):
            
            data.update({'prcmPlanNo':'','page': p, 'pageSize': '18'})
            resp = session.post(url=url, headers=head,
                                data=data, timeout=30).json()
            # print(resp.json(),resp.url,data)
            # break
            for j in resp['rows']:
                if j['NOTICE_TITLE'] and (not '车' in j['NOTICE_TITLE'] and not '医疗' in j['NOTICE_TITLE']) and '保险' in j['NOTICE_TITLE']:
                    print(j['NOTICE_ID'])
                    if j['NOTICE_ID']:
                        Id = j['NOTICE_ID']

                        head1 = {
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                            'Accept-Encoding': 'gzip, deflate',
                            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                            'Connection': 'keep-alive',
                            'Host': 'ccgp-hunan.gov.cn',
                            'Referer': 'http://ccgp-hunan.gov.cn/page/notice/notice.jsp?noticeId=1000832839&area_id=1',
                            'Upgrade-Insecure-Requests': '1',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
                        }
                        params = {
                            'noticeId': Id,
                            'area_id': ''
                        }
                        url_ = 'http://ccgp-hunan.gov.cn/mvc/viewNoticeContent.do'
                        resp_ = session.get(url=url_, headers=head1, params=params,timeout=30)
                        noticeTitle = j['NOTICE_TITLE']
                        with open('HL3/{}.html'.format(noticeTitle), 'w', encoding='utf-8') as f:
                            f.write(resp_.text)
                        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
                        try:
                            pdfkit.from_file('HL3/{}.html'.format(noticeTitle), 'HL3_pdf/{}.pdf'.format(
                                noticeTitle), configuration=config, options={'encoding': 'utf-8'})
                        except:
                            time.sleep(1)
                            try:
                                pdfkit.from_file('HL3/{}.html'.format(noticeTitle), 'HL3_pdf/{}.pdf'.format(
                                    noticeTitle), configuration=config, options={'encoding': 'utf-8'})
                            except:
                                pass
                else:
                    print('+++++++++++++++++++++++淘汰+++++++++++++++++++++++')
        startDate=date(*(int(i) for i in str(startDate).split('-')))
        startDate+=timedelta(days=365)
        endDate=date(*(int(i) for i in str(endDate).split('-')))
        endDate+=timedelta(days=365)
