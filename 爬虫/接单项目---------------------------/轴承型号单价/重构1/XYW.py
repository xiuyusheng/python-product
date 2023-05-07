import requests
from bs4 import BeautifulSoup
import re
import xlwt

class XYW():
    def __init__(self) -> None:
        self.session=requests.Session()
        self.head={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58.X-Requested-With: XMLHttpRequest'
        }
        self.new_data= xlwt.Workbook()
        self.work_sheet = self.new_data.add_sheet('sheet1')
        self.work_sheet.write(0,0,'品牌')
        self.work_sheet.write(0,1,'型号')
        self.work_sheet.write(0,2,'单价')
        self.work_num=1
    def add_work(self,PP,XH,DJ=''):
        self.work_sheet.write(self.work_num,0,PP)
        self.work_sheet.write(self.work_num,1,XH)
        self.work_sheet.write(self.work_num,2,DJ)
        self.work_num+=1

    def save_work(self):
        self.new_data.save('轴承(西域).xls')

    def DJ_get(self):
        url='https://www.ehsy.com/bearings'
        resp=self.session.get(url=url,headers=self.head)
        #创建BeautifulSoup对象
        soup=BeautifulSoup(resp.text,'html.parser')

        #查找nodeImg类的div
        url_list=list(i.find('a')['href'] for i in soup.find_all('div',{'class':'nodeImg'}))
        # return url_list
        for i in url_list:
            resp_=self.session.get(url=i,headers=self.head)

            soup=BeautifulSoup(resp_.text,'html.parser')
            total=soup.find('li',{'class':'pg-num-total'})
            if total:
                num=re.search(r'(?P<num>\d+)',total.text)
                if num:
                    num=int(num.group("num"))+1
                    # print(num)
                    for n in range(1,num):
                        # 使用CSS选择器查找带有data-text属性的元素
                        resp_=self.session.get(url=i+'?p={}'.format(n),headers=self.head)
                        # print(resp_.url)
                        soup=BeautifulSoup(resp_.text,'html.parser')
                        elements = soup.select('[data-text]')
                        for j in elements:
                            ul=j.find('ul')
                            childs=ul.find_all()
                            ZM=re.search(r'(?P<ZM>\w+)',childs[0].text)
                            if ZM:
                                # print(ZM)
                                ZM=ZM.group('ZM')
                                if 'FAG' in ZM or 'INA' in ZM :
                                    self.add_work(ZM,childs[1].text.replace('\n',''),ul.find('span','yen').text.replace('\n',''))
                                    print('品牌：{}，型号：{}，单价：{}'.format(ZM,childs[1].text,ul.find('span','yen').text).replace('\n',''))
                                else:
                                    print('淘汰')
        self.save_work()
if __name__=="__main__":
    XYW=XYW()
    XYW.DJ_get()