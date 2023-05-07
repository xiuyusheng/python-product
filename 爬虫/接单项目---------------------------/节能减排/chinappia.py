import requests
from bs4 import BeautifulSoup as bea
import re
from time import sleep as sp

class JNJP():
    def __init__(self) -> None:
        self.urls = 'http://www.chinappia.com/page.html'
        self.session = requests.Session()
        self.params = {
            'bb': '',
            'typeid1': '1',
            'typeid2': '76',
            'typeid3': '',
            'page': 0
        }
        self.head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'
        }


    def get_url_list(self):
        text=list()
        urls_=list()
        while True:
            self.params['page']+=1
            resp = self.session.get(url=self.urls, headers=self.head,params=self.params)
            urls=re.findall(r'<a href="(pinfo\.html\?newsid=\d+)"',resp.text)
            if set(urls) & set(urls_):
                print(set(urls) & set(urls_))
                with open('4.html','w',encoding='utf-8') as f:
                    f.write(str(text))
                return text
            urls_=urls
            for i in urls:
                url='http://www.chinappia.com/{}'.format(i)
                print(url)
                try:
                    resp=requests.get(url=url,headers=self.head,params=self.params)
                    resp.encoding='gb2312'
                    text_=bea(resp.text,'html.parser').find('td',style='LINE-HEIGHT: 180%;FONT-SIZE: 14px;FONT-FAMILY: 宋体;')
                    if text_:
                        text.append(text_.text)
                    resp.close()
                except:
                    pass
                


def main():
    from chinappia import JNJP
    JNJP = JNJP()
    return JNJP.get_url_list()


if __name__ == "__main__":
    print(main())
