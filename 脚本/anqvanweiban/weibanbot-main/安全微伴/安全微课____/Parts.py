import WeibanAPI
import login
import Examination
import set_bank

def login_(UserId,UserPassword):#登录
    login__=login.stat(UserId,UserPassword)
    while(not login__['code']=='0'):#验证码识别错误则重新登录
        if not login__['code']=='0':
            login__=login.stat(UserId,UserPassword)
        if('msg' in login__):
            print(login__['msg'])
    return login__

def Study(login__,studyID):#学习
    login_=login__['data']
    userId = login_['userId']
    token = login_['token']
    tenantCode = login_['tenantCode']
    wb = WeibanAPI.WeibanAPI(token=token, userId=userId, tenantCode=tenantCode)#创建学习实例
    wb.getTask(studyID)#获取专题，获取课程，为他传参因为有其他程序需要获取该类下的该程序返回的专题信息
    wb.getCourse()#获取而课程
    wb.finshiall()#开始学习提交


def Examination_(login__,studyID):#考试
    score=Examination.start(login__,studyID)
    if(type(score)==list):#该专题没有考试，列表为空
        return []
    return score#正常返回成绩

def set_bank_(login__,studyID):#刷新题库
    set_bank.start(login__,studyID)

