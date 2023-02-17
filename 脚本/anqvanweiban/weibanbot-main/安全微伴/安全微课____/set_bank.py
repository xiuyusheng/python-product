import sqlite3
import requests
import time
import os
import sys

###################程序打包路径纠错##########################
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)
########################################################

db_path = os.path.join(application_path, "test.db")#路径连接

conn = sqlite3.connect(db_path)#连接题库

Library = '11yuequestions'  # 数据库名称

def listPlan(userId,prepare_startpaper_head,userProjectId):
    listPlan_url = 'https://weiban.mycourse.cn/pharos/exam/listPlan.do?timestamp='  # 获取专题考试编号

    listPlan_data = {
        'userProjectId': userProjectId,  # 专题编号
        'tenantCode': '4144013930',
        'userId': userId
    }
    listPlan_resp = requests.post(url=listPlan_url+str(int(time.time())),
                                  data=listPlan_data, headers=prepare_startpaper_head).json()
    if(listPlan_resp['data']==[]):#没有考试项目则返回空
        return []
    return listPlan_resp['data'][0]


def getlisthistory(userId,prepare_startpaper_head,listPlan):#获取考试记录
    listhistory_url = 'https://weiban.mycourse.cn/pharos/exam/listHistory.do?timestamp='
    listhistory_data = {
        'examPlanId': listPlan['examPlanId'],
        'isRetake': 2,
        'userId': userId,
        'tenantCode': '4144013930'
    }
    listhistory_resp = requests.post(
        url=listhistory_url, data=listhistory_data, headers=prepare_startpaper_head).json()
    if(not listhistory_resp['code']=='0'):#没有记录则返回空
        return []
    return listhistory_resp['data']


def reviewPaper(userId,prepare_startpaper_head,listhistory):#获取考试结果即正确答案反馈
    reviewPaper_url = 'https://weiban.mycourse.cn/pharos/exam/reviewPaper.do?timestamp='
    reviewPaper_data = {
        'userExamId': listhistory['id'],
        'isRetake': listhistory['isRetake'],
        'tenantCode': '4144013930',
        'userId': userId
    }
    reviewPaper_resp = requests.post(url=reviewPaper_url+str(
        int(time.time())), data=reviewPaper_data, headers=prepare_startpaper_head)
    reviewPaper_resp.encoding='utf-8'#防止中文乱码
    return reviewPaper_resp.json()

def pdxd(id):
    cursor = conn.execute(f"SELECT questionId  from '{Library}'")#sql查询语句
    for i in list(cursor):
        # print(i[0]==id)
        if(i[0]==id):
            return False
    return True


def Storage(token, userId, prepare_startpaper_head,studyID):
    listPlan_= listPlan(userId, prepare_startpaper_head,studyID)#获取考试的信息（目的在获取考试ID）
    if(not listPlan_==[]):
        getlisthistory_=getlisthistory(userId, prepare_startpaper_head,listPlan_)#获取历史考试记录
        for i in range(len(getlisthistory_)):#存在记录开始刷新题库
            result = reviewPaper(userId, prepare_startpaper_head,getlisthistory_[i])['data']['questions']#获取题目和答案列表
            for question in result:
                if(pdxd(question['id'])):#判断题库中是否存在该题目ID，不存在则为true，题目ID在所有专题唯一
                    Answers=''
                    for Answer in question['optionList']:#获取选项，不是答案
                        if(Answer['isCorrect']==1):#isCorrect等于1则为则为正确答案
                            Answers+=Answer['id']+','#连接答案字符串
                    Answers=Answers[:-1]#用切片将字符串最后一位“,”删掉
                    conn.execute(f"INSERT INTO '{Library}'(questionId,Answer) values('{question['id']}','{Answers}')")#插入考题ID
        conn.commit()#关闭数据库连接
        print('题库刷新')
    else:
        print('无考试')

def start(login__,studyID):
    login_ = login__['data']
    userId = login_['userId']
    token = login_['token']
    prepare_startpaper_head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35',
    'x-token': token
    }
    Storage(token, userId, prepare_startpaper_head,studyID)#执行主程序，无返回值
