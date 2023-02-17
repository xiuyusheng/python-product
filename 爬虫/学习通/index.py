import requests
from datetime import datetime
from datetime import timedelta
import login

cookie=login.start()

def date(sendTime):#时间比对
    import datetime
    now = datetime.datetime.now()  #当前日期
    this_week_start = now - timedelta(days=now.weekday())  #本周开始第一天2022-9-12
    this_week_end = now + timedelta(days=6 - now.weekday())  #本周的最后一天2022-9-18
    sult = sendTime > this_week_start and sendTime < this_week_end
    print(sult)
    return sult

def data(cookie):  #获取表单
    head_data = {
        'Cookie': cookie,
        'Host': 'notice.chaoxing.com',
        'Origin': 'http://notice.chaoxing.com',
        'Referer':
        'http://notice.chaoxing.com/pc/notice/myNotice?s=e4451fe92bf83f32493a27c42c8d7edb',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data_data = {
        'type': '2',
        'notice_type': '',
        'lastValue': '',
        'sort': '',
        'folderUUID': '',
        'kw': '',
        'startTime': '',
        'endTime': '',
        'gKw': '',
        'gName': '',
        'year': '2022'
    }
    resp_data = requests.post(
        'http://notice.chaoxing.com/pc/notice/getNoticeList',
        headers=head_data,
        data=data_data)
    resp_data.close()
    return resp_data.json()

def analysis():
    datas = data(cookie)#获取课程表单
    num=0
    for i in datas['notices']['list']:
        datetime_object = datetime.strptime(i['sendTime'], '%Y-%m-%d %H:%M:%S')#将获获取到的任务发送时间字符串转换为时间格式
        if date(datetime_object):#对任务发送时间是否是在本周，是则将任务打印出来
            print(str(i['content']).replace('\r', '\n'))
            num+=1
    if not num:
        print('本周超星没有作业')
analysis()