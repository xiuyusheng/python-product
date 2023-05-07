import requests
from bs4 import BeautifulSoup as bea
import re
import xlwt
import json
class WB():
    def __init__(self,key_word) -> None:
        self.session = requests.Session()
        self.head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'}
        self.key_word=key_word
        self.save_ids=list()#记录一查找过的对象

        self.new_data = xlwt.Workbook()#表格实例
        self.work_sheet = self.new_data.add_sheet('sheet1')#添加页面
        self.work_sheet.write(0, 0, 'text')
        self.work_sheet.write(0, 1, '转发数')
        self.work_sheet.write(0, 2, '评论数')
        self.work_sheet.write(0, 3, '点赞数')
        self.work_num = 1

    def add_work(self, text='', reposts_count='',comments_count='', attitudes_count='',time_=''):
        self.work_sheet.write(self.work_num, 0, text)
        self.work_sheet.write(self.work_num, 1, reposts_count)
        self.work_sheet.write(self.work_num, 2, comments_count)
        self.work_sheet.write(self.work_num, 3, attitudes_count)
        self.work_sheet.write(self.work_num, 4, time_)
        self.work_num += 1

    def save_work(self):
        self.new_data.save('微博.xls')

    def write_excel(self,k):
        k=k['mblog']
        if (not k['id'] in self.save_ids) and (2008<int(k['created_at'][-4:]) and int(k['created_at'][-4:])<2022):
            text=bea(k['text'],'html.parser').text
            text_=re.search(r'.{,5}'+self.key+r'.{,5}',text)
            if text_:
                text_=text_.group()
                self.add_work(text=text_,
                            reposts_count=k['reposts_count'],
                            comments_count=k['comments_count'],
                            attitudes_count=k['attitudes_count'],
                            time_=k['created_at'][-4:])
                            
                self.save_ids.append(k['id'])
                print(k['id'],self.work_num)

    def seach(self):
        for key in self.key_word:
            self.add_work(text=key)
            self.key=key
            url = 'https://m.weibo.cn/api/container/getIndex'
            for year in range(1900,2022):
                print(year)
                for type_ in (1,2):
                    params = {
                        'containerid': '100103type={}&q={}'.format(type_,key+str(year)),
                        'page_type': 'searchall'
                    }
                    try:
                        resp=self.session.get(url=url,headers=self.head,params=params,timeout=5).json()
                    except:
                        continue
                    # print(resp)
                    if resp['ok']:
                        self.key_=False
                        for n in range(1,1000):
                            params['page']=n
                            resp_=self.session.get(url=url,headers=self.head,params=params)
                            try:
                                resp_=resp_.json()
                                if resp['ok'] and resp_['data']['cards']:
                                        for k in resp_['data']['cards']:
                                            if k['card_type']==9:
                                                self.write_excel(k=k)
                                            elif  k['card_type']==11:
                                                for i in k['card_group']:
                                                    if i['card_type']==9:
                                                        self.write_excel(i)
                                                    else:
                                                        print('淘汰',i['card_type'])
                                            else:
                                                print('错误')
                                else:
                                    break
                            except:
                                pass
        self.save_work()
if __name__ == "__main__":
    WB=WB(['低碳','双碳','排放碳','双减','减碳','减碳排','节能减排'])
    WB.seach()