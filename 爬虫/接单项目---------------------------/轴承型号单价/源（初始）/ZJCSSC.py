import requests
import jwt
import base64
import json
from bs4 import BeautifulSoup
import re
import xlwt
class ZJCSSC():
    def __init__(self,userid,password) -> None:
        self.userid=userid
        self.password=password
        self.session=requests.Session()
        self.head={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
        }
        self.new_data= xlwt.Workbook()
        self.work_sheet = self.new_data.add_sheet('sheet1')
        self.work_sheet.write(0,0,'型号')
        self.work_sheet.write(0,1,'单价(普通)')
        self.work_sheet.write(0,2,'单价(VIP)')
        self.work_num=1
    def get_cookie(self,name):
        # 获取cookie字符串
        token_str = name  # 这里需要替换成实际的cookie值
        if token_str:
            # 解析JWT令牌
            s1 = token_str.split('.')[1]
            s2 = base64.urlsafe_b64decode(s1 + '=' * (4 - len(s1) % 4))
            s3 = json.loads(s2.decode('utf-8'))
            s4 = base64.urlsafe_b64decode(s3['sub'] + '=' * (4 - len(s3['sub']) % 4))
            return json.loads(s4.decode('utf-8'))

    def login(self):
        url='https://www.zjshop.com.cn/'
        self.session.get(url=url,headers=self.head)#获取token
        self.token=self.session.cookies['scptoken']
        self.enc=self.get_cookie(self.token)#获取其他参数

        #登录
        login_url='https://www.zjshop.com.cn/firefly-user/user/login'
        data={
            'token':self.token,
            'mobile':self.userid,
            'password':self.password,
            'xpj':self.enc['xpj']
        }
        self.token=self.session.post(url=login_url,headers=self.head,data=data).json()['result']['token']
        self.session.cookies['scptoken']=self.token

    def add_work(self,XH,DJ='',DJ_V=''):
        self.work_sheet.write(self.work_num,0,XH)
        self.work_sheet.write(self.work_num,1,DJ)
        self.work_sheet.write(self.work_num,2,DJ_V)
        self.work_num+=1
    def save_work(self):
        self.new_data.save('轴承(中机昌盛).xls')
        
    def get_spidstr(self):
        url='https://www.zjshop.com.cn/products'
        resp=self.session.get(url=url,headers=self.head)
        #创建BeautifulSoup对象
        soup=BeautifulSoup(resp.text,'html.parser')
        type_list=list()
        
        #获取类型id
        INA_element=re.search(r',(?P<spidstr>.*?),',soup.find('a',{'title':'INA轴承'})['href']).group('spidstr').strip()
        FAG_element=re.search(r',(?P<spidstr>.*?),',soup.find('a',{'title':'FAG轴承'})['href']).group('spidstr').strip()
        type_list.append(INA_element)
        type_list.append(FAG_element)

        for j,i in enumerate(type_list):
            url='https://www.zjshop.com.cn/products?spidstr={}'.format(i)
            resp=self.session.get(url=url,headers=self.head)
            #创建BeautifulSoup对象
            soup=BeautifulSoup(resp.text,'html.parser')
            ul=soup.find('ul',{'class','pagination'}).find_all('a')[-1]['href']
            pageSize=re.search(r'page=(?P<num>\d+)',ul).group('num')
            self.add_work(XH=['INA轴承','FAG轴承'][j])
            for j in range(1,int(pageSize)+1):
                url='https://www.zjshop.com.cn/products?spidstr={}'.format(i)+'&page={}'.format(j)
                resp=self.session.get(url=url,headers=self.head)
                print(resp.url)
                #创建BeautifulSoup对象
                soup=BeautifulSoup(resp.text,'html.parser')
                Tr=soup.find('tbody').find_all('tr')
                # print(Tr)
                for p in Tr:
                    # print(p)
                    # print('-----------------------------------------------------------')
                    # return
                    XH=p.find('div',{'id':'wnum'}).text
                    price=p.find_all('td',{'class':'cpmoney'})
                    not_vip=price[0].text.replace('\n','').strip()
                    is_vip=price[1].text.replace('\n','').strip()
                    self.add_work(XH,not_vip,is_vip)
                    print('型号：{}，单价（普通）：{}，单价（vip）：{}'.format(XH,not_vip,is_vip))
        self.save_work()

if __name__=="__main__":
    ZJCSSC=ZJCSSC('13810040506','111111')
    ZJCSSC.login()
    ZJCSSC.get_spidstr()