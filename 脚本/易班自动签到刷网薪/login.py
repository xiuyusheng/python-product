import json
import login_sign
from multiprocessing import Pool,cpu_count
import os

def start(USER,PASSWORD):
    yiban=login_sign.Login(USER=USER,PASSWORD=PASSWORD)
    yiban.login_get()#获取密钥
    if yiban.login():#登录
        yiban.sign()#签到
        yiban.praise()#点赞

if __name__=="__main__":
    list_get=[]
    cpu_num=1
    if 'cookie.json' in os.listdir():
        with open('./cookie.json','r') as f:
            list_ = json.load(f)
            for i in list_['list']:
                list_get.append([i['userid'],i['password']])
            if len(list_)<=cpu_count():
                cpu_num=len(list_)
    pool=Pool(cpu_num)
    print(list_get)
    pool.starmap(start,list_get)
    

