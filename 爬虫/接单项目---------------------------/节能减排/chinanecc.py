import requests
from bs4 import BeautifulSoup as bea
import re
class JNJP():
    def __init__(self) -> None:
        self.urls='https://www.chinanecc.cn/website/News.shtml?mod_index=1004'
        self.session=requests.Session()
        self.head={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'
        }
    def get_url_list(self):
            resp=self.session.get(url=self.urls,headers=self.head)
            soup=bea(resp.text,'html.parser')
            nums=re.search(r'document\.bottomPageForm,\s*(\d*),\s*(\d*),',resp.text).groups()
            pages=int(nums[0])//int(nums[1])+1
            text=list()
            for i in range(1,pages+1):
                data={
                    'pager.requestPage': i,
                    'mod_index': 1004
                }
                resp=self.session.post(url='https://www.chinanecc.cn/website/News.shtml',headers=self.head,data=data)
                soup=bea(resp.text,'html.parser')
                for j in soup.find('ul',{'class':'list_line'}).find_all('a'):
                    print(j['href'])
                    try:
                        resp=self.session.get('https://www.chinanecc.cn/website/{}'.format(j['href']),headers=self.head)
                        resp.encoding='gb2312'
                        text_=bea(resp.text,'html.parser').find('div',{'id':'newsContent'})
                        if text_:
                            text.append(text_.text)
                        resp.close()
                    except:
                        pass
            with open('2.html','w',encoding='utf-8') as f:
                f.write(str(text))
            return text

def main():
    from chinanecc import JNJP
    JNJP=JNJP()
    return JNJP.get_url_list()

if __name__=="__main__":
    print(main())