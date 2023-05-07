import requests
import random
import time
import os
#读取db文件相对地址会出错，获取文件的绝对地址
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "test.db")

#连接题库
import sqlite3
conn = sqlite3.connect(db_path)
Library = '11yuequestions'  # 表名

listPlan_url = 'https://weiban.mycourse.cn/pharos/exam/listPlan.do?timestamp='  # 获取专题考试编号
prepare_url = 'https://weiban.mycourse.cn/pharos/exam/preparePaper.do?timestamp='  # 准备考试
startPaper_url = 'https://weiban.mycourse.cn/pharos/exam/startPaper.do?timestamp='  # 开始考试，获取题目
recordQuestion_url = 'https://weiban.mycourse.cn/pharos/exam/recordQuestion.do?timestamp='  # 后台题目备案
submitPaper_url='https://weiban.mycourse.cn/pharos/exam/submitPaper.do?timestamp='#结束考试，获取考试结果
listStudyTask_url='https://weiban.mycourse.cn/pharos/index/listStudyTask.do??timestamp='

def listPlan(userProjectId, userId, prepare_startpaper_head):#获取考试ID

    listPlan_data = {
        'userProjectId': userProjectId,  # 专题编号
        'tenantCode': '4144013930',
        'userId': userId
    }
    listPlan_resp = requests.post(url=listPlan_url+str(int(time.time())),
                                  data=listPlan_data, headers=prepare_startpaper_head).json()
    # print(listPlan_resp)
    if(listPlan_resp['data']==[]):
        return []
    return listPlan_resp['data']


def prepare_startpaper(userId, listPlan_, prepare_startpaper_head):#
    result = []
    prepare_startpaper_data = {
        'userExamPlanId': listPlan_['id'],  # 考试编号
        'tenantCode': '4144013930',
        'userId': userId
    }
    # print(prepare_startpaper_data)
    prepare_resp = requests.post(url=prepare_url+str(int(time.time())),
                                 data=prepare_startpaper_data, headers=prepare_startpaper_head).json()#准备考试
    result.append(prepare_resp)
    # print(prepare_resp)
    startPaper_resp = requests.post(url=startPaper_url+str(int(time.time())),
                                    data=prepare_startpaper_data, headers=prepare_startpaper_head).json()#开始考试
    # print(startPaper_resp)
    result.append(startPaper_resp)
    return result


def getRandomtime():#生成随机时间
    delayTime = random.randint(1, 3)
    return delayTime


def getRandomlist(lens):#根据题目数量获取随机选项
    randonnumber = random.randint(0, lens-1)
    return randonnumber


def Search(questionId, question):
    cursor = conn.execute(
        f"SELECT questionId,Answer  from '{Library}'")  # sql查询语句
    for i in cursor:
        if (questionId == i[0]):#判断是否存在题目，有则获取，没有则采用随机
            return i[1]
    return question['optionList'][int(getRandomlist(len(question['optionList'])))]['id']


def recordQuestion(userId, listPlan_, prepare_startpaper_head):#考试主程序
    questionLists= prepare_startpaper(userId, listPlan_, prepare_startpaper_head)#预备加开始考试
    # print(questionLists[1])
    questionList = questionLists[1]['data']['questionList']#提取考试题目
    print(questionLists[0]['data']['realName']+'\n'+questionLists[0]['data']['userIDLabel']+'\n'+'开始考试！')
###################################################开始考试######################################################################
    for question in questionList:
        sleep_time = getRandomtime()#生成等待时间
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
        while (True):#提交成功则退出
            recordQuestion_resp = requests.post(url=recordQuestion_url+str(int(
                time.time())), data=recordQuestion_data, headers=prepare_startpaper_head,timeout=10).json()#答案备案
            
            # print(recordQuestion_resp['code'])
            if (recordQuestion_resp['code'] == '0'):
                break

    submitPaper_data = {
        'userExamPlanId': listPlan_['id'],
        'tenantCode': '4144013930',
        'userId': userId
    }
###################################################结束考试######################################################################

    result = requests.post(url=submitPaper_url+str(int(
        time.time())), data=submitPaper_data, headers=prepare_startpaper_head).json()#结束开始，获取考试结果


    # print(result)
    if (result['code'] == '0'):#正常则返回考试情况
        score = result['data']['score']
        return score




def start(login__ ,studyID):
    ##存储用户信息变量##
    login_ = login__['data']
    userId = login_['userId']
    token = login_['token']
    ####################

    prepare_startpaper_head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35',
        'x-token': token
    }
    userProjectId = studyID#学习ID
    listPlan_ = listPlan(userProjectId, userId, prepare_startpaper_head)
    if(listPlan_==[]):#该专题没有考试项目，返回空列表
        return []
    # print(listPlan_)
    return recordQuestion(userId, listPlan_[0], prepare_startpaper_head)#执行考试后返回成绩

