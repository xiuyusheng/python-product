import index
import requests
import os
import time
import multiprocessing as mp 
def start(UserId,UserPassword,time_):
    time.sleep(time_)
    try:
        login__=index.login_(UserId,UserPassword)
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
            'tenantCode': tenantCode,
            'limit': '3'
        }
        listStudyTask_response=requests.post(url=listStudyTask_url,headers=listStudyTask_head,data=listStudyTask_data).json()
        key_=True
        print('开始学习！')
        while(key_):
            key_=False
            for num in range(len(listStudyTask_response['data'])):
                if(not listStudyTask_response['data'][num]['progressPet']>=80):
                    bb=index.Study(login__,num)
                    if(bb):
                        key_=True
                
        print('学习完成！')

        for num in range(len(listStudyTask_response['data'])):
            score=0
            if(not listStudyTask_response['data'][num]['progressPet']==100):
                print('开始考试！')
                score=index.Examination_(login__,num)
                if(score>=90):
                    print(f'考试合格，成绩{score}')
                elif(score==0):
                    print('考试次数已用尽 ')
                else:
                    print(f'成绩：{score}')
            if(not score==[]):
                index.set_bank_(login__,num)
    except Exception as e:
        print('error: '+str(e))
        os.system("pause")
        
def main(user):
    for i in range(len(user)):
        list_[i].append(i)
    pool=mp.Pool(mp.cpu_count())
    result=pool.starmap(start,user)#同步并行
    # result=pool.starmap_async(start,user)#异步并行，需要get()启动
    # result.get()
    # print(user)
if __name__ == '__main__':
    list_=[
    ['2107240308','2107240308'],
    ['2106030127','2106030127'],
    ['2107240132','2107240132'],
    ['2106030107','2106030107'],
    ['2106030110','2106030110'],
    ['2106030125','2106030125'],
    ['2106030126','2106030126'],
    ['2106030127','2106030127'],
    ['2107260238','2107260238'],
    ['2107260210','2107260210'],
    ['2107260225','2107260225'],
    ]
    
    main(list_) 
    