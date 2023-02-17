import requests
import MAP
import PUSH
import time
import re
import socket

if __name__=="__main__":
    while True:
        try:
            url = requests.get("http://txt.go.sohu.com/ip/soip")
            break
        except:
            time.sleep(60)
            pass
    text = url.text
    ip = re.findall(r'\d+.\d+.\d+.\d+',text)[0]#获取本机公网IP
    
    gaode=MAP.gaode('a3a3ded5a6ace0345eb4b272665fd898')
    coordinate=gaode.dingwei().json()
    
    city=coordinate['province']+coordinate['city']
    location=coordinate['rectangle'].split(';')[0]
    markers=f'large,0xFF0000,A:{location}'
    push=PUSH.Push_plus('962e5cfffa8e4d0a9a6036f5fbabebce')
    t=time.localtime()
    time_=f'{t.tm_hour}时{t.tm_min}分{t.tm_sec}秒'
    push.Push(title='电脑定位',content=f'<p>公网IP:{ip}</br>\
            本机IP:{socket.gethostbyname(socket.gethostname())}</br>\
            alist端口:{socket.gethostbyname(socket.gethostname())}:5244</br>\
            地理位置:{city}</br>\
            坐标:{location}</p>\
            <img src=\'https://restapi.amap.com/v3/staticmap?key=a3a3ded5a6ace0345eb4b272665fd898&location={location}&zoom=10&markers={markers}&scale=2\'></br>{time_}')