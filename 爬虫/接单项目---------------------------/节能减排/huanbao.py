import requests
from bs4 import BeautifulSoup as bea
class JNJP():
    def __init__(self) -> None:
        self.urls='https://huanbao.bjx.com.cn/topics/huagongjieneng/'
        self.session=requests.Session()
        self.head={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'
        }
    def get_url_list(self):
            resp=self.session.get(url=self.urls,headers=self.head)
            soup=bea(resp.text,'html.parser')
            nums=soup.find_all('div',{'class':'top'})
            text=list()

            for i in nums:
                print(i.find('a')['href'])
                try:
                    resp=self.session.get(url=i.find('a')['href'],headers=self.head)
                    resp.encoding='utf-8'
                    text_=bea(resp.text,'html.parser').find('div',{'id':'article_cont'})
                    if text_:
                        text.append(text_.text)
                    resp.close()
                except:
                    pass
            with open('2.html','w',encoding='utf-8') as f:
                f.write(str(text))
            return text

def main():
    from huanbao import JNJP
    JNJP=JNJP()
    return JNJP.get_url_list()

if __name__=="__main__":
    print(main())