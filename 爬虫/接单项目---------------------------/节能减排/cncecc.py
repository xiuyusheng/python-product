import requests
from bs4 import BeautifulSoup as bea

class JNJP():
    def __init__(self) -> None:
        self.urls='https://www.cncecc.org.cn/xwzx/'
        self.session=requests.Session()
        self.head={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'
        }
    def get_url_list(self):
        page=0
        text=list()
        while True:
            page+=1
            url=self.urls+f'index_{page}.shtml'
            if page==1:
                url='https://www.cncecc.org.cn/xwzx/'
                resp=self.session.get(url=url,headers=self.head)
                print(resp.status_code,resp.url)
                if resp.status_code!=200:
                    with open('6.html','w',encoding='utf-8') as f:
                        f.write(str(text))
                    return text
                soup=bea(resp.text,'html.parser')
                for j in soup.find_all('div',{'class':'info d-grow'}):
                    url=j.find('a')['href']
                    print(url)
                    resp=self.session.get('https://www.cncecc.org.cn{}'.format(url),headers=self.head)
                    text_=bea(resp.text,'html.parser').find('div',{'class':'article'})
                    if text_:
                        text.append(text_.text)
            else:
                resp=self.session.get(url=url,headers=self.head)
                print(resp.status_code,resp.url)
                if resp.status_code!=200:
                    with open('6.html','w',encoding='utf-8') as f:
                        f.write(str(text))
                    return text
                soup=bea(resp.text,'html.parser')
                for j in soup.find_all('div',{'class':'info d-grow'}):
                    url=j.find('a')['href']
                    print(url)
                    try:
                        resp=self.session.get('https://www.cncecc.org.cn{}'.format(url),headers=self.head)
                        text_=bea(resp.text,'html.parser').find('section',{'class':'135brush'})
                        if text_:
                            text.append(text_.text)
                        resp.close()
                    except:
                        pass
def main():
    from cncecc import JNJP
    JNJP=JNJP()
    return JNJP.get_url_list()

if __name__=="__main__":
    print(main())