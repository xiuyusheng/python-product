import json
import login_sign
import os
import PUSH
def start(USER,PASSWORD,PUSH):
        yiban=login_sign.Login(USER=USER,PASSWORD=PASSWORD)
        yiban.login_get()#获取密钥
        if yiban.login():#登录
            yiban.comments()
            yiban.sign()#签到
            yiban.praise(PUSH)#点赞
if __name__=="__main__":
    list_get=[]
    cpu_num=1
    if 'cookie.json' in os.listdir():
        with open('./cookie.json','r') as f:
            list_ = json.load(f)
            for i in list_['list'][::-1]:
                list_get.append([i['userid'],i['password']])
    push=PUSH.Push_plus('962e5cfffa8e4d0a9a6036f5fbabebce')
    for i in list_get:
        start(i[0],i[1],push)
    

