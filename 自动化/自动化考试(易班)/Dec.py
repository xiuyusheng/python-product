import json
import base64
from Crypto.Cipher import AES
import hashlib
import re
import requests


class crypto():  # AES加解密
    def __init__(self, iv_, yibanid) -> None:
        self.iv_ = iv_
        self.MD5(yibanid)

    def MD5(self, yibanid):
        # 要加密的字符串
        self.yibanid = yibanid

        s = 'yooc@admin{}'.format(self.yibanid)

        # 创建MD5对象
        m = hashlib.md5()

        # 更新MD5对象的哈希值
        m.update(s.encode('utf-8'))

        # 获取哈希值的十六进制表示
        self.result = m.hexdigest()

    def decrypto(self, text_):
        # 密文
        encrypted_text = text_

        # Base64 解码
        encrypted_data = base64.b64decode(encrypted_text)

        # AES 解密
        key = self.result[8:24]
        iv = self.iv_
        cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, iv.encode('utf8'))
        decrypted_data = cipher.decrypt(encrypted_data).decode('utf-8')
        # 输出结果
        return decrypted_data

    def encrypto(self, data):
        # 明文
        plain_text = data

        # 密钥和初始向量
        key = self.result[8:24]
        iv = self.iv_

        # 将明文填充为 16 的倍数
        pad = 16 - len(plain_text) % 16
        plain_text += chr(pad) * pad

        # AES 加密
        cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, iv.encode('utf8'))
        encrypted_data = cipher.encrypt(plain_text.encode('utf8'))

        # Base64 编码
        encrypted_text = base64.b64encode(encrypted_data).decode('utf-8')

        # 输出结果
        return (encrypted_text)

def Their_papers(token, yibanid, answer, score, examuserid):
        head = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarydgnVVbY55Heefiow',
            'Host': 'exambackend.yooc.me',
            'Origin': 'https://exam.yooc.me',
            'Pragma': 'no-cache',
            'Referer': 'https://exam.yooc.me/',
            'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'
        }
        params={
            'token':token,
            'yibanId':yibanid
        }
        data={
            'answer':answer,
            'score':'Z/zKKhd3RHoGWeZ+hN9BbA==',
            'examuserId':examuserid
        }
        resp=requests.post('https://exambackend.yooc.me/api/exam/submit/action',headers=head,params=params,data=data)
        return resp

