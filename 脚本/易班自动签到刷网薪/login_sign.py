import requests
import execjs
import re
import time
import json

class Login():
    def __init__(self, USER, PASSWORD) -> None:
        self.ctx = execjs.compile('''const JSEncrypt=require('node-jsencrypt')
var aa=function(PUBLIC,PASSWORD){
var encrypt = new JSEncrypt();
encrypt.setPublicKey(PUBLIC);
return (encrypt.encrypt(PASSWORD));
}
''')
        self.USER = USER
        self.PASSWORD = PASSWORD
        self.session = requests.Session()
        self.head = {
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62'
        }

    def login_get(self):  # 获取密钥
        url = 'https://www.yiban.cn/login?go=https%3A%2F%2Fwww.yiban.cn%2F'
        resp = self.session.get(url=url, headers=self.head)
        self.PUBLIC = re.search(
            r'id="login-pr" data-keys=\'(?P<public>.*?)\'', resp.text, re.S).group('public')
        self.KEYTIME = float(re.search(
            r'data-keys-time=\'(?P<keytime>.*?)\'', resp.text, re.S).group('keytime'))

    def login(self):  # 登录
        url = 'https://www.yiban.cn/login/doLoginAjax'
        data = {
            'account': self.USER,
            'password': self.ctx.call('aa', self.PUBLIC, self.PASSWORD),
            'captcha': '',
            'keysTime': self.KEYTIME,
        }
        # print(dict(self.session.cookies), data)
        resp = self.session.post(url=url, data=data, headers=self.head)
        if resp.json()['code']==200:
            return True

    def sign(self):  # 签到
        url1 = 'https://www.yiban.cn/ajax/checkin/checkin'
        resp = self.session.post(url=url1, headers=self.head)
        print(resp.json()['code'],resp.text)
        if resp.json()['code'] == 200:
            print(f"签到问题<{resp.json()['message']}>")
            optionid = re.search(
                r'class=\\\"survey-option\\\" data-value=\\\"(?P<id>.*?)\\\"', resp.text, re.S).group('id')
            url2 = 'https://www.yiban.cn/ajax/checkin/answer'
            data = {
                'optionid[]': optionid,
                'input': ''
            }
            resp = self.session.post(url=url2, headers=self.head, data=data)
            if resp.json()['code'] == 200:
                print(f"签到<{resp.json()['message']}>")
        else:
            print('已经签到过了')

    def praise(self):  # 点赞
            school_web = 'https://www.yiban.cn/ajax/bbs/getBoardList?orgId=2004278'
            resp = self.session.get(url=school_web, headers=self.head).json()
            thumb = 'https://s.yiban.cn/api/post/thumb'
            data = {
                'action': "up",
                'postId': '',
                'userId': ''
            }
            with open('./cookie.json','r') as f:
                cook=json.load(f)
                for i in cook['list']:
                    cook['num'][i['userid']]=cook['num'].get(i['userid'],0)
            
            if resp['code'] == 200:
                for i in resp['data']:
                    for n in range(0,1000,10):
                        resp_ = self.session.get(
                            'http://www.yiban.cn/ajax/bbs/getListByBoard?offset={}&count={}&boardId={}&orgId=2004278'.format(n,10,i['id']), headers=self.head).json()
                        if resp_['code'] == 200 and resp_['data']:
                            for j in resp_['data']['list']:
                                    if cook['num'][self.USER]<30:
                                        if not j['upNum']:
                                            time.sleep(3)
                                            data['postId']=j['id']
                                            data['userId']=j['user']['id']
                                            resp_1=self.session.post(url=thumb,headers=self.head,data=data).json()
                                            cook['num'][self.USER]+=1
                                            with open('./cookie.json','w') as f:
                                                json.dump(cook,f)
                                            print(j['user']['name']+'已点赞',resp_1)
                                        else:
                                            print('已经点过赞了')
                                    else:
                                        return
                        elif not resp_['data']:
                            break