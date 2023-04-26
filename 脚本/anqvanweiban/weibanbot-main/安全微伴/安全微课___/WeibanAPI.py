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

    def getRandomtime(self):
        delayTime = random.randint(5,10)
        return delayTime




    def getTask(self,num):
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
            self.preUserProjectId = response['data'][num]['userProjectId']
            self.projectID = self.preUserProjectId
            return response['data'][num]['userProjectId']
            # print(self.preUserProjectId)

    def getProgress(self):
            param = {
                'userProjectId': self.preUserProjectId,
                'tenantCode': self.tenantCode,
                "token": self.token,
                "userId": self.userId
            }
            re = requests.post(url=getProgressURL +
                            f"?timestamp={int(time.time())}",
                            data=param,
                            headers=self.header)
            progress = re.json()['data']
            print('{:*^15}'.format('学习进度'))
            print('课程总数：' + str(progress['requiredNum']))
            print('完成课程：' + str(progress['requiredFinishedNum']))
            print('结束时间：' + str(progress['endTime']))
            print('剩余天数：' + str(progress['lastDays']))

    def getCourse(self):
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
        # print(self.course)
    def finshiall(self):
        key_=False
        for i in self.course.json()['data']:
            print('\n----章节码：' + i['categoryCode'] + '章节内容：' +
                  i['categoryName'])
            print('获取课程详细信息')
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

                print('课程内容：' + j['resourceName'])
                if (j['finished'] == 1):
                    print('已完成')
                    pass
                    
                else:
                    key_=True
                    param = {
                        'userProjectId': self.projectID,
                        'courseId': j['resourceId'],
                        'tenantCode': self.tenantCode,
                        'userId': self.userId
                    }
                    temp = time.time()
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
                    wait_time = self.getRandomtime()
                    print('等待{}秒'.format(wait_time))
                    time.sleep(wait_time)
                    params = {
                        'callback':'jQuery34105397279727918969_1667836335117',
                        'userCourseId': j['userCourseId'],
                        'tenantCode': self.tenantCode[0],
                        '_':temp
                    }
                    r = requests.get(url=finishURL,params=params,timeout=5000)
                    if str(r.content):
                        if 'jQuery34105397279727918969_1667836335117' in str(r.content):
                            print('完成')
                            # print(r.headers)
                            pass
                        else:
                            print('失败')
        return key_
