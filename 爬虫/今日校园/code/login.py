import re
import random
import base64
import requests
from Crypto.Cipher import AES
from urllib.parse import unquote

def rds(lenght):
        chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678'
        return ''.join(random.choice(chars) for _ in range(lenght))
"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDIrn+WB2Yi4ABAL5Tq6E09tumY\nqVTFdpU01kCDUmClczJOCGZriLNMrshmN9NJxazpqizPthwS1OIK3HwRLEP9D3GL\n7gCnvN6lpIpoVwppWd65f/rK2ewv6dstN0fCmtVj4WsLUchWlgNuVTfWljiBK/Dc\nYkfslRZzCq5Fl3ooowIDAQAB\n-----END PUBLIC KEY-----\n"
def encrypt(data, key, iv):
        BLOCK_SIZE = 16
        def pad(s): return s + (BLOCK_SIZE - len(s.encode()) %
                                BLOCK_SIZE) * chr(BLOCK_SIZE - len(s.encode()) % BLOCK_SIZE)
        data = pad(data)
        cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, iv.encode('utf8'))
        encrypting = cipher.encrypt(data.encode('utf8'))
        base = base64.b64encode(encrypting)
        context = base.decode('utf8')
        return context

def login():
    session = requests.Session()
    response = session.get('https://gpc.campusphere.net/iap/login?service=https://gpc.campusphere.net/wec-counselor-apps/counselor/mobile-v2/index.html')
    url = 'http://authserver.gpc.net.cn/authserver/login?service=https://gpc.campusphere.net/iap/loginSuccess?sessionToken=' + \
        unquote(response.url)[-32:]
    html = response.text
    pattern = re.compile(r'name="lt" value="(.*?)"')
    lt = pattern.findall(html)[0]
    pattern = re.compile(r'var pwdDefaultEncryptSalt = "(.*?)"')
    salt = pattern.findall(html)[0]

    username = '2106200248'
    pwd = '20030216...'

    password = encrypt(rds(64) + pwd, salt, rds(16))

    body = {
        'username': username,
        'password': password, 
        'lt': lt, 
        'dllt': 'userNamePasswordLogin', 
        'execution': 'e1s1', 
        '_eventId': 'submit', 
        'rmShown': '1'
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'authserver.gpc.net.cn',
        'Origin': 'http://authserver.gpc.net.cn',
        'Proxy-Connection': 'keep-alive',
        'Referer': url,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

    response = session.post(url, data=body, headers=headers, allow_redirects=False)
    location = response.headers['Location']
    headers['Host'] = 'gpc.campusphere.net'
    headers['Referer'] = 'http://authserver.gpc.net.cn/'
    response = session.get(location, headers=headers, allow_redirects=False)
    location = response.headers['Location']
    response = session.get(location, headers=headers, allow_redirects=False)
    cookies = requests.utils.dict_from_cookiejar(response.cookies)
    cookie = "; ".join([str(x) + "=" + str(y) for x, y in cookies.items()])
    print(cookie)
    return cookie
login()
    
