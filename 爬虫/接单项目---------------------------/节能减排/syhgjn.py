import requests
from bs4 import BeautifulSoup as bea
import re


class JNJP():
    def __init__(self) -> None:
        self.urls = 'http://www.syhgjn.cn/news.more2.php'
        self.session = requests.Session()
        self.head = {
            'Host': 'www.syhgjn.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'
        }

    def get_url_list(self):
        params = {
                'search': '节能减排',
                'page': 0
            }
        text=list()
        while True:
            params['page']+=1
            resp = self.session.get(url=self.urls, headers=self.head,params=params)
            soup = bea(resp.text, 'html.parser')
            if 'norecord' in resp.text:
                with open('7.html', 'w', encoding='utf-8') as f:
                    f.write(str(text))
                return text
            
            for j in soup.find_all('li', {'class': 'clear'}):
                url=j.find('a')['href']
                print(url)
                try:
                    resp = self.session.get(
                        'http://www.syhgjn.cn/{}'.format(url), headers=self.head)
                    text_ = bea(resp.text, 'html.parser').find(
                        'div', {'class': 'content'})
                    if text_:
                        text.append(text_.text)
                    resp.close()
                except:
                    pass

def main():
    from syhgjn import JNJP
    JNJP = JNJP()
    return JNJP.get_url_list()


if __name__ == "__main__":
    print(main())
