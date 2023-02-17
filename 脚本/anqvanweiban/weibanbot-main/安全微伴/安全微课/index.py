import WeibanAPI
import time
import requests
import login
import Examination
import set_bank
import os

def login_(UserId,UserPassword):
    login__=login.stat(UserId,UserPassword)
    while(not login__['code']=='0'):
        if not login__['code']=='0':
            print(login__['msg'])
            login__=login.stat(UserId,UserPassword)
    return login__

def Study(login__,num):
    login_=login__['data']
    userId = login_['userId']
    token = login_['token']
    tenantCode = login_['tenantCode']
    wb = WeibanAPI.WeibanAPI(token=token, userId=userId, tenantCode=tenantCode)

    wb.getTask(num)
    wb.getProgress()
    wb.getCourse()
    bb=wb.finshiall()
    return bb

def Examination_(login__,num):
    score=Examination.start(login__,num)

    if(type(score)==str):
        return 0
    elif(type(score)==list):
        return []
    return score

def set_bank_(login__,num):
    set_bank.start(login__,num)



if __name__ == '__main__':
    try:
        login__=login_()
        login_=login__['data']
        userId = login_['userId']
        token = login_['token']
        tenantCode = login_['tenantCode']

        listStudyTask_url = f'https://weiban.mycourse.cn/pharos/index/listStudyTask.do?timestamp={int(time.time())}'
        listStudyTask_head = {
            "user-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35",
            "x-token": token
        }
        listStudyTask_data = {
            'userId': userId,
            'tenantCode': tenantCode
        }
        listStudyTask_response=requests.post(url=listStudyTask_url,headers=listStudyTask_head,data=listStudyTask_data).json()
        key_=True
        print('开始学习！')
        while(key_):
            key_=False
            for num in range(len(listStudyTask_response['data'])):
                if(not listStudyTask_response['data'][num]['progressPet']>=80):
                    bb=Study(login__,num)
                    if(bb):
                        key_=True
                
        print('学习完成！')

        for num in range(len(listStudyTask_response['data'])):
            score=0
            if(not listStudyTask_response['data'][num]['progressPet']==100):
                print('开始考试！')
                score=Examination_(login__,num)
                if(score>=90):
                    print(f'考试合格，成绩{score}')
                elif(score==0):
                    print('考试次数已用尽 ')
                print(f'成绩：{score}')
            if(not score==[]):

                set_bank_(login__,num)

    except Exception as e:
        print('error: '+str(e))
    os.system("pause")
