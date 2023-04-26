import Parts  # 自定义程序包
import requests
import time
import json
from multiprocessing import Pool
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
        # 'limit': '3'
    }
    listStudyTask_response = requests.post(
        url=listStudyTask_url, headers=listStudyTask_head, data=listStudyTask_data).json()
    return listStudyTask_response


def userName(User):
    login_ = User['data']
    userId = login_['userId']
    token = login_['token']
    tenantCode = login_['tenantCode']
    index_url = f'https://weiban.mycourse.cn/pharos/my/index.do?timestamp={int(time.time())}'
    index_head = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35",
        "x-token": token
    }
    index_data = {
        'userId': userId,
        'tenantCode': tenantCode,
    }
    listStudyTask_response = requests.post(
        url=index_url, headers=index_head, data=index_data).json()

    return listStudyTask_response


class All():
    def __init__(self, userId, Password, studyName) -> None:
        # print(userId)
        # token存档登录
        try:  # 验证一边token是否有效
            with open('login.json', 'r') as f:
                login = json.load(f)[userId]
                listStudyTask_response = listStudyTask(login)  # 有课程数据则为有效
        except:  # token无效则重新账号密码获取
            login_ = Parts.login_(userId, Password)  # 执行账号密码登录
            # 获取login.json中已存在该账号的token数据，如没有则新建
            with open('login.json', 'r', encoding="utf-8") as f:
                login = json.load(f)  # 将json转换为dic
                if (userId in login):
                    login[userId] = login_  # 存在，将其值修改为新获取到的token数据
                else:
                    new_token = {userId: login_}  # 不存在新建dic数据
                    login.update(new_token)  # 合并两个dic合并
            with open('login.json', 'w') as fp:  # 重新更替新数据
                json.dump(login, fp)  # 将dic转换为json

            listStudyTask_response = listStudyTask(login_)  # 获取课程课程信息
            login = login_
        ################################################################################
        self.login = login
        self.userName = userName(self.login)['data']
        self.listStudyTask_response = listStudyTask_response
        self.studyID = ''
        for i in self.listStudyTask_response['data']:
            if (i['projectName'] == studyName and i['progressPet'] < 100):
                self.studyID = i['userProjectId']
                return
            else:
                self.studyID = ''

    def study(self):  # 学习
        login__ = self.login
        print('开始学习！')
        # 执行学习模块# # # # # # # # # # # # # # # # # # # # # # # #
        Parts.Study(login__, self.studyID)
        print('学习完成！')

    def examination(self):  # 考试
        score = 0
        print('开始考试！')
        # 执行考试模块，成功执行返回成绩# # # # # # # # # # # # # # # # # # # # # # # #
        score = Parts.Examination_(self.login, self.studyID)

        print(f'成绩合格：{score}' if score > 90 else f'成绩：{score}')  # 输出成绩
        if (not score == []):
            # 执行刷新题库模块# # # # # # # # # # # # # # # # # # # # # # # #
            Parts.set_bank_(self.login, self.studyID)


def start(userId, password, studyName):
    start = All(userId, password, studyName)
    userName=start.userName['realName']
    if (not start.studyID == ''):  # 判断是否存在该课程
        # print(start.studyID)
        print('考生：'+userName,
              userName, f'课程：{studyName}', sep='\n')
        start.study()
        start.examination()
    else:
        print(f'课程：{studyName}')
        print('已通过')
    
if __name__=="__main__":
    studyName = [
        # ['2106200232', '2106200232', ['2022年11月禁毒专题', '2022年11月专题', '2022年12月专题', '2021级入学后安全教育']],
    # ['2106200248', '2106200248', ['2023年春季专题']],
    # ['2106200253', '2106200253', ['2023年春季专题']],
    ['2107240132', '2107240132', '2023年春季专题'],
    ['2106030134', '2106030134', '2023年春季专题'],
    ['2107240332', '2107240332', '2023年春季专题'],
    ['2107260103', '2107260103', '2023年春季专题'],
    ['2107260120', '2107260120', '2023年春季专题'],
    ['2106280416', '2106280416', '2023年春季专题'],
    ['2106200108', '2106200108', '2023年春季专题'],
    ['2106200347', '2106200347', '2023年春季专题'],
    ['2106200301', '2106200301', '2023年春季专题'],
    ['2107240308', '2107240308', '2023年春季专题'],
    # ['2106280112', '2106280112', ['2023年春季专题']],
    # ['2106200111', '2106200111', ['2023年春季专题']],
    # ['2107270234', '2107270234', ['2023年春季专题']],
    # ['2106200110', '2106200110', ['2023年春季专题']],
    # ['2106200150', '2106200150', ['2023年春季专题']],
    # ['2106200149', '2106200149', ['2023年春季专题']],
    # ['2106200132', '2106200132', ['2023年春季专题']],
    # ['2106200116', '2106200116', ['2023年春季专题']],
    # ['2106200103', '2106200103', ['2023年春季专题']],
    # ['1906200208', '1906200208', ['2023年春季专题']],
    # ['2106200132', '2106200132', ['2023年春季专题']],
    # ['2106200116', '2106200116', ['2023年春季专题']],
    # ['2106200107', '2106200107', ['2023年春季专题']],
    # ['2106200224', '2106200224', ['2023年春季专题']],
    # ['2106200207', '2106200207', ['2023年春季专题']],
    # ['2106200222', '2106200222', ['2023年春季专题']],
    # ['2106200224', '2106200224', ['2023年春季专题']],
    # ['2106200232', '2106200232', ['2023年春季专题']],
    # ['2106200245', '2106200245', ['2023年春季专题']],
    # ['2106200254', '2106200254', ['2023年春季专题']],
    # ['2106200216', '2106200216', ['2023年春季专题']],
    # ['2106200241', '2106200241', ['2023年春季专题']],
    # ['2106200153', '2106200153', ['2023年春季专题']],
    # ['2106200136', '2106200136', ['2023年春季专题']],
    # ['2107270238', '2107270238', ['2023年春季专题']],
    # ['2106200217', '2106200217', ['2023年春季专题']],
    # ['2106200243', '2106200243', ['2023年春季专题']],
        ]
    pool = Pool(10)
    pool.starmap(start, studyName)
    # for i in studyName:
    #     for j in i[2]:
    #         # 1.学号2.密码3.课程ID，先通过Learningsituation.py下的learning((ID,Password))返回给前端用户选择专题并返回专题号
    #         start(i[0], i[1], j)
    
