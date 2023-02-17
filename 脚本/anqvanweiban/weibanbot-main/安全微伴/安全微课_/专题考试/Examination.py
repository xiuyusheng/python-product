import requests
import random
import time
import sqlite3
import login
conn = sqlite3.connect('test.db')

Library = 'ruxuehou'  # 数据库名称
num = 1  # 专题序列

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
    return listPlan_resp['data'][0]


def prepare_startpaper(userId, listPlan_, prepare_startpaper_head):
    result = []
    prepare_startpaper_data = {
        'userExamPlanId': listPlan_['id'],  # 考试编号
        'tenantCode': '4144013930',
        'userId': userId
    }
    prepare_resp = requests.post(url=prepare_url+str(int(time.time())),
                                 data=prepare_startpaper_data, headers=prepare_startpaper_head).json()
    result.append(prepare_resp)
    startPaper_resp = requests.post(url=startPaper_url+str(int(time.time())),
                                    data=prepare_startpaper_data, headers=prepare_startpaper_head).json()
    result.append(startPaper_resp)
    return result


def getRandomtime():
    delayTime = random.randint(2, 5)
    return delayTime


def getRandomlist(lens):
    randonnumber = random.randint(0, lens-1)
    return randonnumber


def Search(questionId, question):
    cursor = conn.execute(
        f"SELECT questionId,Answer  from {Library}")  # sql查询语句
    for i in cursor:
        if (questionId == i[0]):
            return i[1]
    print
    return question['optionList'][int(getRandomlist(len(question['optionList'])))]


def recordQuestion(userId, listPlan_, prepare_startpaper_head):
    questionList = prepare_startpaper(userId, listPlan_, prepare_startpaper_head)[
        1]['data']['questionList']
    print()
    for question in questionList:

        sleep_time = getRandomtime()
        print(f'等待{sleep_time}秒')
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
                time.time())), data=recordQuestion_data, headers=prepare_startpaper_head).json()#答案备案
            
            # print(recordQuestion_resp['code'])
            if (recordQuestion_resp['code'] == '0'):
                print(question['id']+'已提交')
                time.sleep(1)
                break

    submitPaper_data = {
        'userExamPlanId': listPlan_['id'],
        'tenantCode': '4144013930',
        'userId': userId
    }
    result = requests.post(url=submitPaper_url+str(int(
        time.time())), data=submitPaper_data, headers=prepare_startpaper_head).json()#结束开始，获取考试结果
    if (result['code'] == '0'):
        score = result['data']['score']
        print(f'考试成功，成绩{score}')


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


def start():
    # 登录
    login__ = login.stat()
    while (not login__['code'] == '0'):
        if not login__['code'] == '0':
            print(login__['msg'])
            login__ = login.stat()
    login_ = login__['data']
    userId = login_['userId']
    token = login_['token']

    prepare_startpaper_head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35',
        'x-token': token
    }
    userProjectId = getTask(token, userId, prepare_startpaper_head, num)
    listPlan_ = listPlan(userProjectId, userId, prepare_startpaper_head)
    recordQuestion(userId, listPlan_, prepare_startpaper_head)

try:
    start()
except:
    print('出错了！')
