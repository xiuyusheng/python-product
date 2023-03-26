import requests
import re
import os
import execjs
urls={
    'main':'https://www.tiku365.net',
    'index':'https://www.tiku365.net/all/index-{}.html'
}

if __name__=="__main__":
    head={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
    }
    session_=requests.Session()
    for i in range(1,21):
        resp=session_.get(urls['index'].format(i),headers=head)
        print(resp.url,sep='\n')
        links_=re.findall(r'<dd class="imgB"><a href="(.*?)">',resp.text)
        # print(links_)
        for j in links_:
            resp=session_.get(urls['main']+j,headers=head)
            print(resp.url,sep='\n')
            key=re.search(r'<meta property="og:title" content="(?P<fname>.*?)" />',resp.text,re.S)
            # print(key.group('fname'))
            if key:
                fname=key.group('fname')
                key=re.search(r'正文目录</b></dt>(?P<link>.*?)</dl>',resp.text,re.S)
                # print(key.group('link'))
                if key:
                    links__=key.group('link')
                    links=re.findall(r'<dd><a href="(.*?)">',links__)
                    # print(links)
                    folder = os.path.exists(os.path.join('E:\小说',fname))
                    if not folder:
                        os.makedirs(os.path.join('E:\小说',fname))
                    for o,k in enumerate(links):
                        with open(os.path.join('E:\小说',fname,f'第{o+1}章.html').format(fname,o),'w',encoding='utf-8') as f:
                            resp=session_.get(urls['main']+k,headers=head)
                            key=re.search(r'var c2="(?P<c2>.*?)"',resp.text,re.S)
                            if key:
                                
                                c2=key.group('c2')
                                nnx=re.search(r'<script type="text/javascript" src="(?P<c2>.*?)"',resp.text,re.S).group('c2')
                                ajax=session_.get('https://www.tiku365.net{}'.format(nnx),headers=head)
                                # print(ajax.text)
                                js_=re.search(r'(?P<c2>function ajax\(xxyyu\){.*?return temp.toLowerCase\(\)})',ajax.text,re.S).group('c2')
                                ctx = execjs.compile(js_)
                                p=session_.get('https://www.tiku365.net{}'.format(ctx.call('ajax', c2)),headers=head,cookies=session_.cookies)
                                
                            else:
                                print(resp.text,sep='\n')
                                a_num=1
                                key=re.search(r'id="PageSet"(?P<a>.*?)</div>',resp.text)
                            # print(key.group('a'))
                            # if key:
                            #     a_num=key.group('a')
                            #     a_num=len(re.findall(r'href="',a_num))
                            # print(a_num)
        #                     for i in range(a_num):
        #                         while True:
        #                             resp=session_.get(urls['main']+k.replace('.html','-{}.html'.format(i+1)),headers=head)
        #                             print(resp.url,sep='\n')

        #                             key=re.search(r'<div id="content">\s*(?P<content>.*?)\s*</div>',resp.text,re.S)
        #                             if key:
        #                                 text_=key.group('content')
        #                                 f.write(text_)
        #                                 break
        #                             else:
        #                                 key=re.search(r'var c2="(?P<c2>.*?)"',resp.text,re.S)
        #                                 if key:
        #                                     c2=key.group('c2')
        #                                     nnx=re.search(r'<script type="text/javascript" src="(?P<c2>.*?)"',resp.text,re.S).group('c2')
        #                                     ajax=session_.get('https://www.tiku365.net{}'.format(nnx),headers=head)
        #                                     # print(ajax.text)
        #                                     js_=re.search(r'(?P<c2>function ajax\(xxyyu\){.*?return temp.toLowerCase\(\)})',ajax.text,re.S).group('c2')
        #                                     ctx = execjs.compile(js_)
        #                                     p=session_.get('https://www.tiku365.net{}'.format(ctx.call('ajax', c2)),headers=head,cookies=session_.cookies)
        #                                     print('尝试')
        #                                 else:
        #                                     break