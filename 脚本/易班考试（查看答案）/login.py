import requests
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64
import re
class Login():
    def __init__(self, USER, PASSWORD) -> None:
        self.key=True
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
        if resp.json()['code'] == 200:
            return True
