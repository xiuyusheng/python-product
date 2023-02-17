# -*- coding:utf-8 -*-
import requests
import math
import json
import login
def handler (event, context):
    cookie=login.login()
    DailyUrl = 'https://gpc.campusphere.net/wec-counselor-collector-apps/collector/teacher/queryDailyDetail'
    TargetUrl = 'https://gpc.campusphere.net/wec-counselor-collector-apps/collector/notice/queryAllTarget'
    headers = {
        'Cookie': cookie,
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://gpc.campusphere.net',
        'Connection': 'keep-alive',
        'Host': 'gpc.campusphere.net',
        'User-Agent':
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (4530414080) cpdaily/9.0.20 wisedu/9.0.20',
        'Referer':
        'https://gpc.campusphere.net/wec-counselor-collector-apps/collector/mobile/index.html?collectorInfoPage=true&collectorWid=29559',
        'X-Requested-With': 'XMLHttpRequest'
    }
    payload = {
        'taskWid': '29559',
        'pageNumber': 1,
        'pageSize': 9999999,
        'isSelectMngt': 'false'
    }
    response = requests.request("POST", DailyUrl, headers=headers,
                                json=payload).json()
    key_=False
    try:
        instanceWid = response['datas']['rows'][0]['instanceWid']#总未打卡人数
        Rate = response['datas']['rows'][0]['stuSubmitRate'].split("（")[0].split("/")#打卡人数数组
        total = int(Rate[1]) - int(Rate[0])
        pages = math.ceil(total / 10)  #页数
        if pages == 0:
            print("今日打卡已完成！")
        class_= {}
        a=""
        for page in range(1, pages + 1):#页数循环
            body = {
                "isRead": "-1",
                "sortColumn": "",
                "isHandled": "0",
                "isSelectMngt": "false",
                "wid": "29559",
                "instanceWid": instanceWid,
                "content": "",
                "pageNumber": page,
                "pageSize": 10
            }
            resp = requests.request("POST", TargetUrl, headers=headers,
                                    json=body).json()
            rows = resp['datas']['rows']#未打卡学生情况
            for row in rows:
                # print(row)
                if row['propertyClass'] not in class_:
                    class_[row['propertyClass']] = 1
                else:
                    class_[row['propertyClass']] += 1
                if row['propertyClass'] == '21级软件技术B班': #筛选软件B班学生
                    a+=(row['name'] +"\t"+ row['userId'] +"\t" + row['mobile'] +"\n")
                    print(row['name'], row['userId'], row['mobile'],sep="\t")
        if total:
            print("未打卡人数：", str(total) + "人\n\n")
            print("今日打卡统计:")
            a += "未打卡人数：" + str(total) + "人\n今日打卡统计:\n"
            for i in class_:
                a += (i + str(class_[i]) + "人\n")
                print(i, str(class_[i]) + "人")
            
        else:
            a="今日打卡已完成！"
    except:
        a="Cookie---失效"
    def send(msg):
        # 获取 access_token
        get_access_token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        values = {
            'corpid': 'ww249f1946b89f668c',
            'corpsecret': 'R_5N3uPB5TyPtZ6fHRBMSu-ZYMaH-DA0VDMe1piJt3E',
        }
        res = requests.post(get_access_token_url, params=values).json()
        access_token = res["access_token"]
        # 推送消息
        send_url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'
        post_data = {
            "touser": '@all',
            "msgtype": "text",
            "agentid": '1000002',
            "text": {
                "content": msg
            },
            "safe": "0"
        }
        q = requests.post(send_url, data=json.dumps(post_data)).json()
        print(q)


    send(a)
    return {
        "statusCode": 200,
        "isBase64Encoded": False,
        "body": class_,
        "headers": {
            "Content-Type": "application/json"
        }
    }