import requests
import csv
from bs4 import BeautifulSoup as BEA
from urllib.parse import urlparse
import os
import chardet

class RMW():
    def __init__(self, topic='', picture='picture', pagenum=100,csv_name='articles') -> None:
        self.num = 0
        self.head = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Content-Length': '139',
            'Content-Type': 'application/json',
            'Host': 'search.people.cn',
            'Origin': 'http://search.people.cn',
            'Referer': 'http://search.people.cn/s/?keyword=%E4%BF%84%E4%B9%8C%E5%86%B2%E7%AA%81&st=1&_=1682593618815',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
        }
        self.session = requests.Session()
        self.topic = topic
        self.picture = picture
        self.pagenum=pagenum
        self.csv_name=csv_name
        if not os.path.exists(self.picture):
            os.makedirs(self.picture)
        with open('{}.csv'.format(self.csv_name), 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['id','事件类别','来源','真伪','文章标题','文章内容','图片文件名'])
    def add_csv(self, id_, title, url, imagePATH='', originName=''):

        resp = requests.get(url=url, headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': urlparse(url).netloc,
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
        },timeout=(3,5))
        if resp.status_code!=200:
            return
        resp.encoding = chardet.detect(resp.content)['encoding']
        html = BEA(resp.text, 'html.parser')
        # 分解URL
        if imagePATH:
            try:
                img_resp = self.session.get(url=imagePATH, headers={
                    'Accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                    'Connection': 'keep-alive',
                    'Host': urlparse(imagePATH).netloc,
                    'Referer': url,
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
                },timeout=3)
            except:
                return
            imagePATH = urlparse(imagePATH)
            imagePATH = os.path.split(imagePATH.path)[-1]
            with open('{}/{}'.format(self.picture, imagePATH), 'wb') as f:
                f.write(img_resp.content)
        print(resp.url)
        article = html.find(
            'div', {'class': 'rm_txt_con cf'})
        if not article:
            article = html.find(
                'div', {'class': 'fl text_con_left'})
        if not article:
            article = html.find(
                'div', {'class': 'col col-1 fl'})
        if not article:
            article = html.find(
                'div', {'class': 'artDet'})
        if not article:
            return
        article = article.text.replace(',', '，').replace('\n', '')
        title = title.replace('<em>', '').replace('</em>', '')
        if self.topic in title or self.topic in article:
            # 写入CSV文件
            with open('{}.csv'.format(self.csv_name), 'a', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(
                    [id_,self.topic, originName, False, title, article, imagePATH])
                self.num += 1
        else:
            print('{}--淘汰'.format(title))

    def seach_topic(self):
        url = 'http://search.people.cn/search-platform/front/search'
        json_ = {
            'endTime': 0,
            'hasContent': True,
            'hasTitle': True,
            'isFuzzy': True,
            'key': self.topic,
            'limit': self.pagenum,
            'page': 1,
            'sortType': 2,
            'startTime': 0,
            'type': 1
        }
        resp = self.session.post(url=url, headers=self.head, json=json_).json()
        print(resp)
        for j in resp['data']['records']:
            print(j['title'])
            self.add_csv(id_=j['id'], title=j['title'], url=j['url'],
                         imagePATH=j['imageUrl'], originName=j['originName'])
        print('共%s' % self.num)


if __name__ == "__main__":
    RMW = RMW('俄乌冲突', '图片（俄乌冲突）', 300,'俄乌冲突')
    RMW.seach_topic()
