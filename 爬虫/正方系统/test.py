import requests

import re

from PIL import Image

from urllib.parse import urlencode

import webbrowser

import chaojiying

import json

import os

url_Total = {

    'default2': 'http://zf.gdep.edu.cn/default2.aspx',

    'CheckCode': 'http://zf.gdep.edu.cn/CheckCode.aspx'

}





def logindata():  # 请求登录参数（首页）

    url = url_Total['default2']

    head = {

        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

        'Accept-Encoding': 'gzip, deflate',

        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',

        'Cache-Control': 'max-age=0',

        'Connection': 'close',

        'Host': 'zf.gdep.edu.cn',

        'Upgrade-Insecure-Requests': '1',

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52'}

    resp_ = requests.get(url, allow_redirects=True, headers=head)

    login_data = []

    cookie = resp_.headers['Set-Cookie'].split(';')[0]  # 分割可用coookie

    # print(resp_.headers)

    login_data.append(cookie)

    __VIEWSTATE = re.search(

        r'id="__VIEWSTATE" value="(?P<__VIEWSTATE>.*?)"', resp_.text).group('__VIEWSTATE')

    login_data.append(__VIEWSTATE)

    __EVENTVALIDATION = re.search(

        r'id="__EVENTVALIDATION" value="(?P<__EVENTVALIDATION>.*?)"', resp_.text).group('__EVENTVALIDATION')

    login_data.append(__EVENTVALIDATION)

    resp_.close()

    return login_data





def CheckCode(cookie):  # 获取验证码

    url = url_Total['CheckCode']

    head = {

        'Accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',

        'Accept-Encoding': 'gzip, deflate',

        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',

        'Connection': 'close',

        'Cookie': cookie,

        'Host': 'zf.gdep.edu.cn',

        'Referer': 'http://zf.gdep.edu.cn/default2.aspx',

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52'

    }

    CheckCode_img = requests.get(url=url, headers=head)

    return chaojiying.yzm(CheckCode_img.content)





def login(login_data, CheckCode_, userid, userpassword):  # 登录系统

    head_login = {

        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

        'Accept-Encoding': 'gzip, deflate',

        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',

        'Cache-Control': 'max-age=0',

        'Connection': 'close',

        'Content-Length': '313',

        'Content-Type': 'application/x-www-form-urlencoded',

        'Cookie': login_data[0],

        'Host': 'zf.gdep.edu.cn',

        'Origin': 'http://zf.gdep.edu.cn',

        'Referer': 'http://zf.gdep.edu.cn/default2.aspx',

        'Upgrade-Insecure-Requests': '1',

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52'

    }

    data_login = {

        '__VIEWSTATE': login_data[1],

        '__EVENTVALIDATION': login_data[2],

        'TextBox1':

        userid,

        'TextBox2':

        userpassword,

        'TextBox3': CheckCode_,

        'RadioButtonList1': '',

        'Button1': ''

    }

    data_login = urlencode(data_login).split('RadioButtonList1=')[

        0]+'RadioButtonList1=%D1%A7%C9%FA'+urlencode(data_login).split('RadioButtonList1=')[1]

    resp_login = requests.post(

        url=url_Total['default2'], headers=head_login, data=data_login, allow_redirects=False)  # 第一次登录校验

    xs_main_url = 'http://zf.gdep.edu.cn' + \
resp_login.headers['Location']  # 解析第二次登录url

    resp_login.close()

    head_xs_main = {

        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

        'Accept-Encoding': 'gzip, deflate',

        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',

        'Cache-Control': 'max-age=0',

        'Connection': 'keep-alive',

        'Cookie': login_data[0],

        'Host': 'zf.gdep.edu.cn',

        'Referer': 'http://zf.gdep.edu.cn/default2.aspx',

        'Upgrade-Insecure-Requests': '1',

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52'}

    loct = requests.get(url=xs_main_url, headers=head_xs_main)

    return loct  # 返回第二次登录respons





def xs_cj(cookie, referer):

    xscj_gc2_url = 'tjkbcx.aspx?xh=2106200248&xm=%u674e%u7855&gnmkdm=N121601'

    xscj_gc2_head = {

        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

    'Accept-Encoding': 'gzip, deflate',

    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',

    'Cache-Control': 'no-cache',

    'Connection': 'keep-alive',

    'Cookie': cookie,

    'Host': 'zf.gdep.edu.cn',

    'Pragma': 'no-cache',

    'Referer': referer,

    'Upgrade-Insecure-Requests': '1',

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56'    }

    cs_resp = requests.get(url='http://zf.gdep.edu.cn/'+xscj_gc2_url,

                            headers=xscj_gc2_head)  # 请求成绩HTML文件

    cs_resp_text = cs_resp.text.replace(

        'charset=gb2312"', 'charset=utf-8"')  # 将网页的gb2312编码格式改为正常显示的utf-8格式

    return cs_resp_text




if __name__=="__main__":
  login_data = logindata()
  Check_Code = CheckCode(login_data[0])
  CheckCode_ = Check_Code['pic_str']
  userid = input('账号：')
  userpassword = input('密码：')
  login_ = login(login_data, CheckCode_, userid=userid,
                 userpassword=userpassword)
  html_=xs_cj(login_data[0], login_.url)
  with open('课程表.html','w') as f:
    f.write(html_)
  file_path='/home/runner/app/课程表.html'
  webbrowser.open_new_tab(file_path)

