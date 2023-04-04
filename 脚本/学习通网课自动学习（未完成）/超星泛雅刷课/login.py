import requests
import execjs  # node操作js执行解码程序


class login():
    def __init__(self) -> None:
        with open('encrypt.js', 'r') as encrypt:
            enc = encrypt.read()
        self.ctx = execjs.compile(enc)
        self.session = requests.Session()

    def enc(self, msg='', vi=''):
        return self.ctx.call('encryptByAES', msg, vi)

    def login(self, uname='', password='',vi='u2oh6Vu^HWe4_AES'):
        url = 'http://passport2.chaoxing.com/fanyalogin'
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
            'X-Requested-With': 'XMLHttpRequest'
        }
        data = {
            'fid': '-1',
            'uname': self.enc(msg=uname,vi=vi),
            'password': self.enc(msg=password,vi=vi),
            'refer': 'http%3A%2F%2Fi.chaoxing.com',
            't': 'true',
            'forbidotherlogin': '0',
            'validate': '',
            'doubleFactorLogin': '0',
            'independentId': '0',
        }
        resp=self.session.post(url=url,headers=head,data=data)
        resp.close()
        return self.session

