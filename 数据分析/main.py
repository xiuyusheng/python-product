import requests
import re
def download(url,name):
    resp=requests.get(url=url)
    with open(f'大国工匠/{name}.mp4','wb') as f:
        f.write(resp.content)

def list_():
    url='https://article.xuexi.cn/data/app/17947697773664604777.js?callback=callback'
    resp=requests.get(url=url).text
    link=re.findall(r'"normal":"(?P<link>.*?)"',resp)
    name=re.findall(r'{"title":"(?P<link>.*?)"',resp)
    for i in range(len(link)):
        download(url=link[i],name=name[i])

if __name__=="__main__":
    list_()