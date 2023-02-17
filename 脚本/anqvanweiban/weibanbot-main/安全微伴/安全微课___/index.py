import WeibanAPI
import time
from rich.console import Console
import requests
import login
import Examination
import set_bank
import os
console = Console()

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
    return score

def set_bank_(login__,num):
    set_bank.start(login__,num)



# if __name__ == '__main__':
#     try:
#         userId=input('学号:')
#         login__=login_(userId,userId)
#         login_=login__['data']
#         userId = login_['userId']
#         token = login_['token']
#         tenantCode = login_['tenantCode']

#         listStudyTask_url = f'https://weiban.mycourse.cn/pharos/index/listStudyTask.do?timestamp={int(time.time())}'
#         listStudyTask_head = {
#             "user-agent":
#             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35",
#             "x-token": token
#         }
#         listStudyTask_data = {
#             'userId': userId,
#             'tenantCode': tenantCode,
#             'limit': '3'
#         }
#         listStudyTask_response=requests.post(url=listStudyTask_url,headers=listStudyTask_head,data=listStudyTask_data).json()
#         key_=True
#         print('开始学习！')
#         while(key_):
#             key_=False
#             for num in range(len(listStudyTask_response['data'])):
#                 bb=Study(login__,num)
#                 if(bb):
#                      key_=True
#         print('学习完成！')

#         for num in range(len(listStudyTask_response['data'])):
#             print('开始考试！')
#             while(True):
#                 score=Examination_(login__,num)
#                 set_bank_(login__,num)
#                 if(score>=90):
#                     print(f'考试合格，成绩{score}')
#                     break
#                 elif(score==0):
#                     print('考试次数已用尽 ')
#                     break

#     except Exception as e:
#         print('error: '+str(e))
#     os.system("pause")
