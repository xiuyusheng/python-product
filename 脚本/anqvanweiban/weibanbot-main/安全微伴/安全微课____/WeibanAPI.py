# import os
import requests
import time
import random
import re

getQRCodeURL = 'https://weiban.mycourse.cn/pharos/login/genBarCodeImageAndCacheUuid.do'  # 获取登录二维码
loginStatusURL = 'https://weiban.mycourse.cn/pharos/login/barCodeWebAutoLogin.do'  # 刷新登录状态
getuserInfo = 'https://weiban.mycourse.cn/pharos/my/getInfo.do'  # 获取用户信息
getTask = 'https://weiban.mycourse.cn/pharos/index/getStudyTask.do'  # 获取任务列表
getzt = 'https://weiban.mycourse.cn/pharos/index/listStudyTask.do?'  #获取专题id
getProgressURL = 'https://weiban.mycourse.cn/pharos/project/showProgress.do'  # 获取进程
getCourseURL = 'https://weiban.mycourse.cn/pharos/usercourse/listCategory.do'  # 获取课程URL
getCourselisURL = 'https://weiban.mycourse.cn/pharos/usercourse/listCourse.do'  # 获取课程详细信息
doStudyURL = 'https://weiban.mycourse.cn/pharos/usercourse/study.do'  # 发送开始练习
finishURL = 'https://weiban.mycourse.cn/pharos/usercourse/finish.do'  # 发送完成请求
getCourseUrls = 'https://weiban.mycourse.cn/pharos/usercourse/getCourseUrl.do'





class WeibanAPI():

    def __init__(self, token, userId, tenantCode):
        self.header = {
            "user-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35",
            "x-token": token
        }
        self.userId = userId
        self.tenantCode = tenantCode,
        self.token = token

    def getRandomtime(self):#随机提交时间
        delayTime = random.randint(10,20)
        return delayTime




    def getTask(self,studyID):#返回专题课程
        param = {
            'userId': self.userId,
            'tenantCode': self.tenantCode,
            "token": self.token
        }
        url = getzt + str(int(time.time()))

        re = requests.post(url=url + f"?timestamp={int(time.time())}",
                           data=param,
                           headers=self.header)
        response = re.json()
        if response['code'] == '0':
            self.preUserProjectId = studyID
            self.projectID = self.preUserProjectId
            return studyID

    def getCourse(self):#获取课程
        param = {
            'userProjectId': self.projectID,
            "userId": self.userId,
            'chooseType': 3,
            'tenantCode': self.tenantCode,
            "token": self.token
        }
        self.course = requests.post(getCourseURL +
                                    f"?timestamp={int(time.time())}",
                                    data=param,
                                    headers=self.header)
    def finshiall(self):#向后台发送学习
        number=0
        for i in self.course.json()['data']:
                key_=True#程序关卡
                while(key_):
                    key_=False
                    param = {
                        'userProjectId': self.projectID,
                        'chooseType': 3,
                        'categoryCode': i['categoryCode'],
                        'name': '',
                        'userId': self.userId,
                        'tenantCode': self.tenantCode,
                        'token': self.token
                    }
                    req = requests.post(url=getCourselisURL +
                                        f"?timestamp={int(time.time())}",
                                        data=param,
                                        headers=self.header)
                    for j in req.json()['data']:
                        if (j['finished'] == 1):
                            pass
                            
                        else:#是否已学习，未学习则开始学习
                            key_=True
                            param = {
                                'userProjectId': self.projectID,
                                'courseId': j['resourceId'],
                                'tenantCode': self.tenantCode,
                                'userId': self.userId
                            }
                            temp = time.time()#生成请求时间
                            res = requests.post(
                                url=
                                f'https://weiban.mycourse.cn/pharos/usercourse/study.do?timestamp={int(time.time())}',
                                data=param,
                                headers=self.header)
                                
                            data = {
                                'courseId': j['resourceId'],
                                'userProjectId': self.projectID,
                                'tenantCode': self.tenantCode,
                                'userId': self.userId,
                            }
                            res = requests.post(url=getCourseUrls +
                                                f"?timestamp={int(temp)}",
                                                data=data,
                                headers=self.header).json()
                            methodToken=re.search(r'&methodToken=(?P<methodToken>.*?)&',res['data']).group('methodToken')
                            if('open.mycourse.cn' in res['data']):
                                finishURL='https://weiban.mycourse.cn/pharos/usercourse/finish.do'
                            else: 
                                finishURL=f'https://weiban.mycourse.cn/pharos/usercourse/v1/{methodToken}.do'
                            wait_time = self.getRandomtime()#生成随机等待时间
                            print('等待{}秒'.format(wait_time))
                            time.sleep(wait_time)#等待提交
                            params = {
                                'callback':'jQuery34105397279727918969_1667836335117',
                                'userCourseId': j['userCourseId'],
                                'tenantCode': self.tenantCode[0],
                                '_':temp
                            }
                            r = requests.get(url=finishURL,params=params,timeout=5000)
                            if str(r.content):#后台已阅览则content值不为空，已阅读不代表已存在记录
                                if 'jQuery34105397279727918969_1667836335117' in str(r.content):
                                    print('完成')
                                    pass
                                else:
                                    print('失败')
