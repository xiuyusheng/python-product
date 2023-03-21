import requests
import time
head = {
    'Cookie': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'
}
data = {
    'func': 'addvideotime',
    'articlesid': 'cb39ecd1-7f37-4715-8468-c6c321a28d4d',
    'secnum': '60'
}


def login(user, login):
    url = 'http://www.xhredcross.com/publiclist.aspx'
    data = {
        'func': 'login',
        'phone': user,
        'password': login
    }
    resp2=requests.post(url=url,headers=head,params=data)
    return resp2.headers['Set-Cookie']
n = 0   
data1 = {
    'r': '0.7243555668130681',
    'func': 'getvideolist'
}
head['Cookie']='UserLevel=1;'+login(input('账号'),input('密码'))
print(head['Cookie'])

resp1 = requests.get(r'http://www.xhredcross.com/publiclist.aspx',
                     params=data1, headers=head).json()
print(resp1)
for i in resp1:
    print(i['title'])
    for _ in range(100):
        data['articlesid'] = i['id']
        
        resp = requests.post(
            'http://www.xhredcross.com/publiclist.aspx', headers=head, params=data)
        # time.sleep(0.01)
        print(resp.text)
print('刷完了')
