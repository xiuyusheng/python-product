import requests
from bs4 import BeautifulSoup as bea
import re


class JNJP():
    def __init__(self,keyword='%BD%DA%C4%DC%BC%F5%C5%C5') -> None:
        self.keyword=keyword
        self.urls = r'http://www.china-esi.com/Search.asp?Field=Title&keyword='+self.keyword+r'&button=%CB%D1%CB%F7'
        self.session = requests.Session()
        self.head = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'www.china-esi.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'
        }

    def get_url_list(self):
        resp = self.session.get(url=self.urls, headers=self.head)
        soup = bea(resp.text, 'html.parser')
        pages = int(soup.find('div', {'class': 'show_page'}
                              ).find_all('a')[-1]['href'][-2:])
        text = list()
        for i in range(1, pages+1):
            params = {
                'ModuleName': '',
                'ChannelID': '0',
                'Field': 'Title',
                'ClassID': '0',
                'SpecialID': '0',
                'page': i
            }
            resp = requests.get(
                url='http://www.china-esi.com/Search.asp?Keyword={}'.format(self.keyword), headers=self.head, params=params)
            soup = bea(resp.text, 'html.parser')
            resp.encoding = 'gb2312'
            for j in soup.find('table', {'class': 'new_showtb'}).find_all('a',{'class':'LinkSearchResult'})[1::2]:
                print(j['href'])
                try:
                    resp = self.session.get(j['href'], headers=self.head)
                    resp.encoding = 'gb2312'
                    text_ = bea(resp.text, 'html.parser').find(
                        'table', {'class': 'new_showtb'})
                    if text_:
                        text.append(text_.text)
                    resp.close()
                except:
                    pass
        return text


def main():
    from chinaesi import JNJP
    for i in ['%BD%DA%C4%DC%BC%F5%C5%C5','%CA%AF%BB%AF%B9%A4%D2%B5']:
        JNJP = JNJP(i)
        return JNJP.get_url_list()


if __name__ == "__main__":
    main()
