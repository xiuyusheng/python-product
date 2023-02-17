import sqlite3
import requests
import time
import login

conn = sqlite3.connect('test.db')

Library = 'ruxuehou'  # 数据库名称
num = 1  # 专题序列

login__ = login.stat()
while (not login__['code'] == '0'):
    if not login__['code'] == '0':
        print(login__['msg'])
        login__ = login.stat()
login_ = login__['data']
userId = login_['userId']
token = login_['token']
tenantCode = login_['tenantCode']


prepare_startpaper_head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35',
    'x-token': token
}


def listPlan(userProjectId):
    listPlan_url = 'https://weiban.mycourse.cn/pharos/exam/listPlan.do?timestamp='  # 获取专题考试编号

    listPlan_data = {
        'userProjectId': userProjectId,  # 专题编号
        'tenantCode': '4144013930',
        'userId': userId
    }
    listPlan_resp = requests.post(url=listPlan_url+str(int(time.time())),
                                  data=listPlan_data, headers=prepare_startpaper_head).json()
    return listPlan_resp['data'][0]


def getlisthistory(listPlan):
    listhistory_url = 'https://weiban.mycourse.cn/pharos/exam/listHistory.do?timestamp='
    listhistory_data = {
        'examPlanId': listPlan['examPlanId'],
        'isRetake': listPlan['examFinishNum'],
        'userId': userId,
        'tenantCode': '4144013930'
    }
    listhistory_resp = requests.post(
        url=listhistory_url, data=listhistory_data, headers=prepare_startpaper_head).json()
    # print(listhistory_resp)
    return listhistory_resp['data']


def reviewPaper(listhistory):
    reviewPaper_url = 'https://weiban.mycourse.cn/pharos/exam/reviewPaper.do?timestamp='
    reviewPaper_data = {
        'userExamId': listhistory['id'],
        'isRetake': listhistory['isRetake'],
        'tenantCode': '4144013930',
        'userId': userId
    }
    reviewPaper_resp = requests.post(url=reviewPaper_url+str(
        int(time.time())), data=reviewPaper_data, headers=prepare_startpaper_head)
    reviewPaper_resp.encoding='utf-8'
    return reviewPaper_resp.json()

def pdxd(id):
    cursor = conn.execute(f"SELECT questionId  from {Library}")#sql查询语句
    for i in list(cursor):
        # print(i[0]==id)
        if(i[0]==id):
            return False
    return True

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

getlisthistory_=getlisthistory(listPlan(getTask(token, userId, prepare_startpaper_head, num)))
for i in range(len(getlisthistory_)):
    print(getlisthistory_[i])
    result = reviewPaper(getlisthistory_[i])['data']['questions']
    print(result)
    for question in result:
        cursor = conn.execute(f"SELECT questionId  from {Library}")#sql查询语句
        # print(list(cursor))
        
        if(pdxd(question['id'])):
            # print(question['id'])
            Answers=''
            for Answer in question['optionList']:
                if(Answer['isCorrect']==1):
                    Answers+=Answer['id']+','
            Answers=Answers[:-1]
            conn.execute(f"INSERT INTO {Library}(questionId,Answer) values('{question['id']}','{Answers}')")
cursor = conn.execute(f"SELECT questionId,Answer  from {Library}")#sql查询语句
for cur in cursor:
    print('问题：'+cur[0],'答案：'+cur[1])
conn.commit()
cursor.close()
# print(result)
