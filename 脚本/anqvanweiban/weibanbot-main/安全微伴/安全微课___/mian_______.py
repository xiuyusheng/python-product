import index
import requests
import os
import time
from multiprocessing import Pool


def start(UserId, UserPassword):
    try:
        login__ = index.login_(UserId, UserPassword)
        login_ = login__['data']
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
        }
        listStudyTask_response = requests.post(
            url=listStudyTask_url, headers=listStudyTask_head, data=listStudyTask_data).json()
        key_ = True
        print('开始学习！')
        while (key_):
            key_ = False
            for num in range(len(listStudyTask_response['data'])):
                bb = index.Study(login__, num)
                if (bb):
                    key_ = True
        print('学习完成！')

        for num in range(len(listStudyTask_response['data'])):
            print('开始考试！')
            while (True):
                score = index.Examination_(login__, num)
                index.set_bank_(login__, num)
                if (score >= 90):
                    print(f'考试合格，成绩{score}')
                    break
                elif (score == 0):
                    print('考试次数已用尽 ')
                    break
    except Exception as e:
        print('error: '+str(e))
        os.system("pause")


if __name__ == '__main__':
    user = [
        ['2106200150', '2106200150'],
        ['2106200149', '2106200149'],
        ['2106200132', '2106200132'],
        ['2106200116', '2106200116'],
    ]
    pool = Pool(5)
    pool.starmap(start, user)
