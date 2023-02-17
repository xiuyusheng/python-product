import requests
import random
import time
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "test.db")
import sqlite3
conn = sqlite3.connect(db_path)

Library = '11yuequestions'  # 数据库名称

listPlan_url = 'https://weiban.mycourse.cn/pharos/exam/listPlan.do?timestamp='  # 获取专题考试编号
prepare_url = 'https://weiban.mycourse.cn/pharos/exam/preparePaper.do?timestamp='  # 准备考试
startPaper_url = 'https://weiban.mycourse.cn/pharos/exam/startPaper.do?timestamp='  # 开始考试，获取题目
recordQuestion_url = 'https://weiban.mycourse.cn/pharos/exam/recordQuestion.do?timestamp='  # 后台题目备案
submitPaper_url='https://weiban.mycourse.cn/pharos/exam/submitPaper.do?timestamp='#结束考试，获取考试结果

def listPlan(userProjectId, userId, prepare_startpaper_head):

    listPlan_data = {
        'userProjectId': userProjectId,  # 专题编号
        'tenantCode': '4144013930',
        'userId': userId
    }
    listPlan_resp = requests.post(url=listPlan_url+str(int(time.time())),
                                  data=listPlan_data, headers=prepare_startpaper_head).json()
    # print(listPlan_resp.text)
    if(listPlan_resp['data']==[]):
        return []
    return listPlan_resp['data'][0]


def prepare_startpaper(userId, listPlan_, prepare_startpaper_head):
    result = []
    prepare_startpaper_data = {
        'userExamPlanId': listPlan_['id'],  # 考试编号
        'tenantCode': '4144013930',
        'userId': userId
    }
    # print(prepare_startpaper_data)
    prepare_resp = requests.post(url=prepare_url+str(int(time.time())),
                                 data=prepare_startpaper_data, headers=prepare_startpaper_head).json()
    result.append(prepare_resp)
    # print(prepare_resp)
    startPaper_resp = requests.post(url=startPaper_url+str(int(time.time())),
                                    data=prepare_startpaper_data, headers=prepare_startpaper_head).json()
    result.append(startPaper_resp)
    return result


def getRandomtime():
    delayTime = random.randint(1, 3)
    return delayTime


def getRandomlist(lens):
    randonnumber = random.randint(0, lens-1)
    return randonnumber


def Search(questionId, question):
    cursor = conn.execute(
        f"SELECT questionId,Answer  from '{Library}'")  # sql查询语句
    for i in cursor:
        if (questionId == i[0]):
            return i[1]
    return question['optionList'][int(getRandomlist(len(question['optionList'])))]['id']


def recordQuestion(userId, listPlan_, prepare_startpaper_head):
    questionLists= prepare_startpaper(userId, listPlan_, prepare_startpaper_head)
    # print(questionLists[1])
    questionList = questionLists[1]['data']['questionList']
    print(questionLists[0]['data']['realName']+'\n'+questionLists[0]['data']['userIDLabel']+'\n'+'开始考试！')
    for question in questionList:

        sleep_time = getRandomtime()
        # print(f'等待{sleep_time}秒')
        time.sleep(sleep_time)
        recordQuestion_data = {
            'userExamPlanId': listPlan_['id'],
            'questionId': question['id'],  # 题目编号
            'useTime': sleep_time,  # 等待时间（秒）
            'answerIds': Search(question['id'], question),  # 答案编号
            'tenantCode': '4144013930',
            'userId': userId,
            'examPlanId': listPlan_['examPlanId']  # 考试编号
        }
        while (True):
            recordQuestion_resp = requests.post(url=recordQuestion_url+str(int(
                time.time())), data=recordQuestion_data, headers=prepare_startpaper_head,timeout=10).json()#答案备案
            
            # print(recordQuestion_resp['code'])
            if (recordQuestion_resp['code'] == '0'):
                # print(question['id']+'已提交')
                # time.sleep(1)
                break

    submitPaper_data = {
        'userExamPlanId': listPlan_['id'],
        'tenantCode': '4144013930',
        'userId': userId
    }
    result = requests.post(url=submitPaper_url+str(int(
        time.time())), data=submitPaper_data, headers=prepare_startpaper_head).json()#结束开始，获取考试结果
    # print(result)
    if (result['code'] == '0'):
        score = result['data']['score']
        return score


def getTask(token, userId, header, num):  # 获取专题号
    param = {
        'userId': userId,
        'tenantCode': '4144013930',
        "token": token
    }
    url = 'https://weiban.mycourse.cn/pharos/index/listStudyTask.do?timestamp=' + \
        str(int(time.time()))

    re = requests.post(url=url + f"?timestamp={int(time.time())}",
                       data=param,
                       headers=header)
    response = re.json()
    if response['code'] == '0':
        preUserProjectId = response['data'][num]['userProjectId']
        return preUserProjectId


def start(login__ ,num):
    login_ = login__['data']
    userId = login_['userId']
    token = login_['token']

    prepare_startpaper_head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35',
        'x-token': token
    }
    userProjectId = getTask(token, userId, prepare_startpaper_head, num)
    listPlan_ = listPlan(userProjectId, userId, prepare_startpaper_head)
    if(listPlan_['examOddNum']==0):
        return '考试次数用尽'
    elif(listPlan_==[]):
        return []
    return recordQuestion(userId, listPlan_, prepare_startpaper_head)

