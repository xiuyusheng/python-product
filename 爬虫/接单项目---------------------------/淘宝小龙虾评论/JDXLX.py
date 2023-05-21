import requests
from bs4 import BeautifulSoup as Bea
import xlwt

class XLX():
    def __init__(self) -> None:
        self.session = requests.Session()
        self.head = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'
        }
        self.work=xlwt.Workbook()
        self.work_sheet=self.work.add_sheet('sheet1')
        self.work_sheet.write(0, 0, '用户名')
        self.work_sheet.write(0, 1, '评价')
        self.work_num = 1

    def add_work(self,username='',usercom=''):

        self.work_sheet.write(self.work_num, 0, username)
        self.work_sheet.write(self.work_num, 1, usercom)
        self.work_num += 1

    def save_work(self):
        self.work.save('小龙虾商品评价表.xls')

    def index_page(self):
        url = 'https://search.jd.com/Search?keyword=%E5%B0%8F%E9%BE%99%E8%99%BE&qrst=1&psort=4&stock=1&psort=4&pvid=dc83449083314c29bbf8eca496a041ca&click=1'
        html = self.session.get(url=url, headers=self.head)
        soup = Bea(html.text, 'html.parser')
        urls = list()
        for i in soup.find_all('li', {'class': 'gl-item'}):
            urls.append(i['data-sku'])
        print(urls)
        return urls[:1]#7个商品

    def comment_page(self):
        url = 'https://api.m.jd.com/'
        for i in self.index_page():
            for pages in range(30):#评论30页
                params = {
                    'appid': 'item-v3',
                    'functionId': 'pc_club_productPageComments',
                    'productId': i,
                    'score': '0',
                    'sortType': '0',
                    'page':pages,
                    'pageSize': '100'
                }
                resp=self.session.get(url=url,headers=self.head,params=params).json()['comments']
                if resp:
                    for com in resp:
                        # print(com['nickname'])
                        self.add_work(username=com['nickname'],usercom=com['content'])
        self.save_work()


if __name__ == "__main__":
    XLX=XLX()
    XLX.comment_page()