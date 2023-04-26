import requests
import re
import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64
import time


class Login():
    def __init__(self, USER, PASSWORD) -> None:
        self.key = True
        self.USER = USER
        self.PASSWORD = PASSWORD
        self.session = requests.Session()
        self.head = {
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62'
        }

    def aa(self, PUBLIC, PASSWORD):
        key = RSA.importKey(PUBLIC)
        cipher = PKCS1_v1_5.new(key)
        encrypted_password = cipher.encrypt(PASSWORD.encode('utf-8'))
        return base64.b64encode(encrypted_password).decode('utf-8')

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
            'password': self.aa(self.PUBLIC, self.PASSWORD),
            'captcha': '',
            'keysTime': self.KEYTIME,
        }
        resp = self.session.post(url=url, data=data, headers=self.head)
        print(resp.text)
        if resp.json()['code'] == 200:
            return True

    def sign(self):  # 签到
        url1 = 'https://www.yiban.cn/ajax/checkin/checkin'
        resp = self.session.post(url=url1, headers=self.head)
        print(resp.json()['code'], resp.text)
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

    def comment(self, j):  # 评论
        comment = 'https://s.yiban.cn/api/post/comment'
        comments = self.session.get(
            'https://s.yiban.cn/api/forum/primaryComment?postId={}&offset=0&count=20'.format(j['id'])).json()
        for r in comments['data']['list']:
            if r['user']['id'] == '52645580':
                print('评论过了')
                return
        time.sleep(10)
        token_ = self.session.post(
            url='https://s.yiban.cn/api/security/getToken', headers=self.head).json()
        data1 = {
            'comment': "赞,说的很棒！",
            'csrfToken':
            token_['data']['csrfToken'],
            'postId':
            "",
            'userId':
            ""
        }
        data1['postId'] = j['id']
        data1['userId'] = j['user']['id']
        resp_1 = self.session.post(
            url=comment, headers=self.head, data=data1).json()
        if resp_1['code'] == 200:
            print('{}<{}>'.format(resp_1['message'], resp_1))
            return
        else:
            self.key = False

    def praise(self, PUSH):  # 点赞
        school_web = 'https://www.yiban.cn/ajax/bbs/getBoardList?orgId=2004278'
        resp = self.session.get(url=school_web, headers=self.head).json()
        thumb = 'https://s.yiban.cn/api/post/thumb'
        data = {
            'action': "up",
            'postId': '',
            'userId': ''
        }

        num = 0
        if resp['code'] == 200:
            for i in resp['data']:
                for n in range(0, 100, 10):
                    resp_ = self.session.get(
                        'http://www.yiban.cn/ajax/bbs/getListByBoard?offset={}&count={}&boardId={}&orgId=2004278'.format(n, 10, i['id']), headers=self.head).json()
                    if resp_['code'] == 200 and resp_['data']:
                        for j in resp_['data']['list']:

                            if num < 30:
                                try:
                                    if not j['upNum']:
                                        if self.key:
                                            self.comment(j=j)
                                        time.sleep(3)
                                        data['postId'] = j['id']
                                        data['userId'] = j['user']['id']
                                        resp_1 = self.session.post(
                                            url=thumb, headers=self.head, data=data).json()
                                        num += 1
                                        print(j['user']['name']+'已点赞', resp_1)
                                    else:
                                        print('已经点过赞了')
                                except Exception as e:
                                    print(e)
                                    PUSH.Push(title="易班签到打卡(异常)",
                                              content=f"异常\n{e}")
                                    return
                            else:
                                PUSH.Push(title="易班签到打卡",
                                          content=f"{self.USER}点赞已完成")
                                return
                    elif not resp_['data']:
                        break

    def comments(self):

        def getToken():
            url = 'https://s.yiban.cn/api/security/getToken'
            resp = self.session.post(url=url, headers=self.head)
            self.csrfToken = resp.json()['data']['csrfToken']
            # print(resp.text)

        def send_web():
            url = 'https://s.yiban.cn/api/post/web'
            data = {
                "title": "七日不见，如隔一周",
                "summary": "不生活在别人的影子里",
                "content": "<p>不生活在别人的影子里</p>",
                "attach": [],
                "thumbType": 1,
                "channel": [
                    {
                        "orgId": "693168",
                        "boardId": "zQGUdzbEdKzBRBd"
                    }
                ],
                "hasVLink": 0,
                "isWeb": 1,
                "csrfToken": self.csrfToken
            }
            head = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Length': '377',
                'Content-Type': 'application/json',
                'Host': 's.yiban.cn',
                'Origin': 'https://s.yiban.cn',
                'platform': 'yiban_web',
                'Pragma': 'no-cache',
                'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'}
            resp = self.session.post(url=url, json=data, headers=head)
            print(resp.text,self.session.cookies.get_dict(),self.csrfToken)
        getToken()
        send_web()
