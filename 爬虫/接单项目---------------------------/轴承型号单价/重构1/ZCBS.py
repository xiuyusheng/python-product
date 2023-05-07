import requests
import re
import time
from bs4 import BeautifulSoup as BEA
import xlwt


class ZCBS():
    def __init__(self, userid, password) -> None:
        self.session = requests.Session()
        self.userid = userid
        self.password = password
        self.head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
        }
        self.new_data = xlwt.Workbook()
        self.work_sheet = self.new_data.add_sheet('sheet1')
        self.work_sheet.write(0, 0, '品牌')
        self.work_sheet.write(0, 1, '型号')
        self.work_sheet.write(0, 2, '单价')
        self.work_sheet.write(0, 3, '直通惠价')
        self.work_num = 1

    def login(self):
        url = 'https://www.bearingbus.com/index.php?app=member&act=login'
        data = {
            'username': self.userid,
            'password': self.password,
            'captcha': 'undefined',
            'back_act': '/index.php?app=buyer_order',
            'remember': 'true'
        }
        self.session.post(url=url, headers=self.head, data=data)

    def index_url(self):
        url = 'https://www.bearingbus.com/index.php'
        resp = self.session.get(url=url, headers=self.head)
        url_s = re.findall(
            r'<div class="channels">\s*<a href="(.*?)"', resp.text, re.S)
        classname = re.findall(
            r'<div class="channels">\s*<a href=".*?" target="_blank" title="(.*?)">', resp.text, re.S)
        return url_s, classname

    def add_work(self,PP='', XH='', DJ='',ZTHJ=''):
        self.work_sheet.write(self.work_num, 0, PP)
        self.work_sheet.write(self.work_num, 1, XH)
        self.work_sheet.write(self.work_num, 2, DJ)
        self.work_sheet.write(self.work_num, 3, ZTHJ)
        self.work_num += 1

    def save_work(self):
        self.new_data.save('轴承(巴士).xls')

    def class_save(self, PATH_):
        url = 'https://www.bearingbus.com/{}'.format(PATH_)
        resp = self.session.get(url=url, headers=self.head)
        url_s = (re.findall(r'<a class="num" href="', resp.text))
        for brand in ['FAG', 'INA']:
            for i in range(1, len(url_s)+2):
                params = {
                    'app': 'search',
                    'brand': brand,
                    'keyword': '',
                    'display': '',
                    'page':i
                }
                url = 'https://www.bearingbus.com/{}'.format(PATH_)
                resp = self.session.get(url=url, headers=self.head,params=params)
                XH = re.findall(
                    r'backUlbackColor\(this\)(?P<YS>.*?)</ul>', resp.text, re.DOTALL)
                for i in XH:
                    XX = re.findall(r'px;">(?P<XH>.*?)</b>', i, re.DOTALL)
                    XH = XX[0].strip()

                    if 'FAG' in XH or 'INA' in XH:
                        PP='FAG' if 'FAG' in XH else 'INA'
                        ZTHJ=''
                        if len(XX)>4:
                            ZTHJ=XX[3]+XX[4]
                        self.add_work(PP=PP,XH=XH, DJ=XX[1]+XX[2],ZTHJ=ZTHJ)
                        
                        print('型号:{},单价:{},直通汇价：{}'.format(XX[0], XX[1]+XX[2],ZTHJ))
                    else:
                        print('不符合')


# 851245259@qq.com
if __name__ == "__main__":
    ZCBS = ZCBS('19818951743', 'yxraiyy666')
    ZCBS.login()
    urls, classname = ZCBS.index_url()
    for i, j in enumerate(urls):
        print(i, j)
        ZCBS.add_work(XH=classname[i])
        ZCBS.class_save(j)
    ZCBS.save_work()
