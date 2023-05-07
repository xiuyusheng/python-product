import requests
from time import sleep
import re
from datetime import datetime
def requ(url,head):
    html = requests.get(url=url,headers=head)
    num=re.search(r'<p>实时游客人数：<span>(?P<num>\d+)</span>人</p>',html.text).group('num')
    return num
if __name__ == "__main__":
    url = 'http://www.xuanwuhu.net/'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'
    }
    while True:
        n=0
        while True:
            try:
                num=requ(url=url,head=head)
                break
            except: 
                n+=1
                print(f'第{n}次失败尝试')
                pass
        with open('人数.txt','a',encoding='utf-8') as f:
            f.write("人数："+num+'\t\t获取时间：'+str(datetime.today())+'\n')
        sleep(3600)