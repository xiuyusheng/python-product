from http.cookiejar import Cookie
import requests
import math
import json

def start(resp):
    
    
    # print(resp.json()+"12")
    DailyUrl = 'https://gpc.campusphere.net/wec-counselor-collector-apps/collector/teacher/queryDailyDetail'
    TargetUrl = 'https://gpc.campusphere.net/wec-counselor-collector-apps/collector/notice/queryAllTarget'
    headers = {
        'Cookie':resp,
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
        'taskWid': '30145',
        'pageNumber': 1,
        'pageSize': 9999999,
        'isSelectMngt': 'false'
    }
    response = requests.request("POST", DailyUrl, headers=headers,
                                json=payload).json()
    key_=False
    class_= {}
    a=""
    c=''
    RJBlistNum=0
#############################################################################################################
    instanceWid = response['datas']['rows'][0]['instanceWid']#总未打卡人数
    Rate = response['datas']['rows'][0]['stuSubmitRate'].split("（")[0].split("/")#打卡人数数组
    total = int(Rate[1]) - int(Rate[0])
    # print(response,total)
    pages = math.ceil(total / 10)  #页数
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
            
            if row['propertyClass'] not in class_:
                class_[row['propertyClass']] = 1
            else:
                class_[row['propertyClass']] += 1
            if row['propertyClass'] == '21级软件技术B班': #筛选软件B班学生
                a+=(row['name'] +"&nbsp;&nbsp;&nbsp;&nbsp;"+ row['userId'] +"&nbsp;&nbsp;&nbsp;&nbsp;" + row['mobile'] +"<br/>")
                key_=True
                RJBlistNum+=1
                # print(row['name'], row['userId'], row['mobile'],sep="&nbsp;&nbsp;&nbsp;&nbsp;")
    if total:
        # print("未打卡人数：", str(total) + "人<br/>")
        # print("今日打卡统计:")
        a += "未打卡人数：" + str(total) + "人<br/>今日打卡统计:<br/>"
        for i in class_:
            a += (str(i) +"<br/>"+ str(class_[i]) + "人<br/>")
            # print(i, "<br/>"+str(class_[i]) + "人")
        
    else:
        key_=True
        a="今日打卡已完成！未打卡人数"

    print(a)
if __name__=="__main__":
    try:
        try:
            with open('cookie.json',"r") as f:
                Cookie_url=json.load(f)["cookie"]

            start(Cookie_url)
        except:
            Cookie_url="http://112.74.78.185:8101/school_info/"
            resp=requests.get(Cookie_url)
            new_f={
                "cookie":str(resp.json())
            }
            with open('cookie.json','w') as fp:#重新更替新数据
                json.dump(new_f,fp)#将dic转换为json数据并写入fp文件中
            start(resp.json())
    except:
        print("获取失败 未打卡人数NULL")
# def send(msg):
#     # 获取 access_token
#     get_access_token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
#     values = {
#         'corpid': 'ww249f1946b89f668c',
#         'corpsecret': 'R_5N3uPB5TyPtZ6fHRBMSu-ZYMaH-DA0VDMe1piJt3E',
#     }
#     res = requests.post(get_access_token_url, params=values).json()
#     access_token = res["access_token"]
#     # 推送消息
#     send_url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'
#     post_data = {
#         "touser": '@all',
#         "msgtype": "text",
#         "agentid": '1000002',
#         "text": {
#             "content": msg
#         },
#         "safe": "0"
#     }
#     q = requests.post(send_url, data=json.dumps(post_data)).json()
#     print(q)


# send(a)
