import WeibanAPI
import time
from rich.console import Console
import requests
import login
import os 

console = Console()



def run():

    console.print('{:=^45}'.format('安全微课逃课助手'))
    console.print("程序仅供学习，完全免费，不包含考试哦")
    console.print('多学一些安全知识也不是没有用\n')
   
    login__=login.stat()
    while(not login__['code']=='0'):
        if not login__['code']=='0':
            print(login__['msg'])
            login__=login.stat()
    login_=login__['data']
    userId = login_['userId']
    token = login_['token']
    tenantCode = login_['tenantCode']

    wb = WeibanAPI.WeibanAPI(token=token, userId=userId, tenantCode=tenantCode)

    key_=True
    listStudyTask_url = f'https://weiban.mycourse.cn/pharos/index/listStudyTask.do?timestamp={int(time.time())}'
    listStudyTask_head = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35",
        "x-token": token
    }
    listStudyTask_data = {
        'userId': userId,
        'tenantCode': tenantCode,
        'limit': '3'
    }
    listStudyTask_response=requests.post(url=listStudyTask_url,headers=listStudyTask_head,data=listStudyTask_data).json()
    while(key_):
        key_=False
        for num in range(len(listStudyTask_response['data'])):
            wb.getTask(num)
            wb.getProgress()
            print('获取课程列表')
            wb.getCourse()
            bb=wb.finshiall()
            if(bb):
                key_=True
        

    print("全部刷完了")

    # print('开始考试')
    # Examination.start()


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        print("再见~~")
        time.sleep(5)
    os.system("pause")
