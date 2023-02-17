#独立于刷课程序之外，用于随时执行返回学习情况


import requests
import json
import Parts
import time


def listStudyTask(User):  # 获取课程信息
    login_ = User['data']
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
        # 'limit': '3'#限制放回的专题信息
    }
    listStudyTask_response = requests.post(
        url=listStudyTask_url, headers=listStudyTask_head, data=listStudyTask_data).json()
    return listStudyTask_response


def learning(ID, Password):
    # token存档登录
    try:
        with open('login.json', 'r') as f:
            login = json.load(f)
            listStudyTask_response = listStudyTask(login[ID])
    except:
        login_ = Parts.login_(ID, Password)
        with open('login.json', 'r', encoding="utf-8") as f:
            login = json.load(f)
            if (ID in login):
                login[ID] = login_
            else:
                new_token = {ID: login_}
                login.update(new_token)
        with open('login.json', 'w') as fp:
            json.dump(login, fp)
        listStudyTask_response = listStudyTask(login_)
    ###############################################################################
    result = {'data': []}
    for x in listStudyTask_response['data']:
        result['data'].append({'studyexceedPet': x['exceedPet']/80*100 if not x['exceedPet'] >= 80 else 100, 
        'ExaminationexceedPet': 0 if not x['exceedPet'] == 100 else 100, 'projectName': x['projectName'], 'userProjectId': x['userProjectId']})
    # print(result)
    return json.dumps(result)
learning('2106200248', '2106200248')