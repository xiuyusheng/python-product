import json
import requests

a = 'Hello World!'
def send(msg):
    # 获取 access_token
    get_access_token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    values = {
        'corpid': 'ww249f1946b89f668c',
        'corpsecret': 'R_5N3uPB5TyPtZ6fHRBMSu-ZYMaH-DA0VDMe1piJt3E',
    }
    res = requests.post(get_access_token_url, params=values).json()
    access_token = res["access_token"]
    # 推送消息
    send_url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'
    post_data = {
        "touser": '@all',
        "msgtype": "text",
        "agentid": '1000002',
        "text": {
            "content": msg
        },
        "safe": "0"
    }
    q = requests.post(send_url, data=json.dumps(post_data)).json()
    print(q)
send(a)
