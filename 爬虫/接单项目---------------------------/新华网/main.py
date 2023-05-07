import requests
import csv
from bs4 import BeautifulSoup as BEA
from urllib.parse import urlparse
import os
import chardet


class RMW():
    def __init__(self, topic='', picture='picture', pagenum=100, csv_name='articles') -> None:
        self.num = 0
        self.head = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Host': 'so.news.cn',
            'Referer': 'http://so.news.cn/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
            'X-Requested-With': 'XMLHttpRequest'
        }
        self.session = requests.Session()
        self.topic = topic
        self.picture = picture
        self.pagenum = pagenum//10
        self.csv_name = csv_name
        print('topic:{}'.format(topic))
        if not os.path.exists(self.picture):
            os.makedirs(self.picture)
        with open('{}.csv'.format(self.csv_name), 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(
                ['id', '事件类别', '来源', '真伪', '文章标题', '文章内容', '图片文件名'])

    def add_csv(self, id_, title, url, imagePATH='', originName=''):
        try:
            resp = requests.get(url=url, headers={
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Host': urlparse(url).netloc,
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
            },timeout=3)
        except:
            print('请求失败')
            return
        resp.encoding = chardet.detect(resp.content)['encoding']
        html = BEA(resp.text, 'html.parser')
        # 分解URL
        if imagePATH:
            url_ = 'http://tpic.home.news.cn/xhCloudNewsPic/'+imagePATH
            try:
                img_resp = self.session.get(url=url_, headers={
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                    'Cache-Control': 'max-age=0',
                    'Connection': 'keep-alive',
                    'Host': 'tpic.home.news.cn',
                    'Upgrade-Insecure-Requests': '1',
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
            'div', {'id': 'detail'})
        if not article:
            return
        article = article.text.replace(',', '，').replace('\n', '').replace('\r','')
        title = title.replace('<font color=red>', '').replace(
            '</font>', '').replace('&nbsp;', ' ')
        if self.topic in title or self.topic in article:
            # 写入CSV文件
            with open('{}.csv'.format(self.csv_name), 'a', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(
                    [id_, self.topic, originName, False, title, article, imagePATH])
                self.num += 1
        else:
            print('{}--淘汰'.format(title))

    def seach_topic(self):
        title_list=list()
        for i in range(1, self.pagenum+1):
            url = 'http://so.news.cn/getNews'
            params = {
                'keyword': '俄乌冲突',
                'curPage': i,
                'sortField': '0',
                'searchFields': '1',
                'lang': 'cn'
            }
            resp = self.session.get(
                url=url, headers=self.head, params=params).json()
            print(resp)
            if resp['content']['results']:
                for j in resp['content']['results']:
                    print(j['title'])
                    if not j['title'] in title_list:
                        title_list.append(j['title'])
                        self.add_csv(id_=j['contentId'], title=j['title'], url=j['url'],
                                    imagePATH=j['imgUrl'], originName=j['sitename'])
        print('共%s' % self.num)


if __name__ == "__main__":

    RMW = RMW('新冠', '图片（新冠）', 1000, '新冠')
    RMW.seach_topic()
