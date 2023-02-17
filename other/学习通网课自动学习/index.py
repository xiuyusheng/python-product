from email import header
import requests
import time
import login
import re

cookie = login.start()


def courseid():
    courseid_url = 'https://mooc1-1.chaoxing.com/visit/courselistdata'
    courseid_head = {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '80',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': cookie,
        'Host': 'mooc1-1.chaoxing.com',
        'Origin': 'https://mooc1-1.chaoxing.com',
        'Referer':
        'https://mooc1-1.chaoxing.com/visit/interaction?s=34036ee147761f786961ba0e597f3e33',
        'sec-ch-ua':
        '"Microsoft Edge";v="105", " Not;A Brand";v="99", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42',
        'X-Requested-With': 'XMLHttpRequest'
    }
    courseid_data = {
        'courseType': 1,
        'courseFolderId': 0,
        'baseEducation': 0,
        'superstarClass': '',
        'courseFolderSize': 0
    }
    courseid_resp=requests.post(url=courseid_url,headers=courseid_head,data=courseid_data)
    head_url=re.search(r'<a  class="color1" href="(?P<href>.*?)" target="_blank">.*?舞蹈鉴赏</span>',courseid_resp.text,re.S)
    return head_url.group('href')

def head(head_url):
    head_head={}

def video():
    video_url = f'https://s1.ananas.chaoxing.com/video/49/f9/44/1320069b42d78e47de70a8ab6be624f1/sd.mp4?at_={int(time.time())}&ak_=9ed5ca9afaeb84f41c63003bf3526314&ad_=500c205decaf298055fbb95ad4165079'

    video_head = {
        'accept-ranges': 'bytes',
        'age': '133113',
        'ali-swift-global-savetime': str(int(time.time())),
        'Content-Length': '79497632',
        'Content-Range': 'bytes=0-',
        'content-type': 'video/mp4',
        'date': 'Fri, 16 Sep 2022 01:46:56 GMT',
        'eagleid': '78e92ea416634259299023169e',
        'etag': "61dd2c26-4e789a0",
        'last-modified': 'Tue, 11 Jan 2022 07:05:10 GMT',
        'ohc-cache-hit': 'qd8un60 [4], linf2un54 [3], qdix88 [1]',
        'ohc-file-size': '82282912',
        'server': 'Tengine',
        'timing-allow-origin': '*, *',
        'via':
        'cache43.l2cn2270[0,0,206-0,H], cache55.l2cn2270[0,0], cache14.cn4174[0,0,206-0,H], cache16.cn4174[4,0]',
        'x-cache': 'HIT TCP_MEM_HIT dirn:11:483322236 mlen:0',
        'x-cache-status': 'HIT',
        'x-swift-cachetime': '30995116',
        'x-swift-savetime': 'Sat, 17 Sep 2022 08:01:40 GMT'
    }
    video_resp = requests.get(url=video_url, headers=video_head)
    print(video_resp)


courseid()