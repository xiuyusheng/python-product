import requests
import login
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

class coure():
    def __init__(self, login, uname, password) -> None:
        self.session = requests.Session
        self.session = login.login(uname, password)

    def my_Home_page(self):
        url = 'http://mooc1-1.chaoxing.com/visit/courselistdata'
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
        }
        data = {
            'courseType': '1',
            'courseFolderId': '0',
            'baseEducation': '0',
            'superstarClass': '',
            'courseFolderSize': '0'
        }
        resp = self.session.post(url=url, headers=head, data=data)
        return resp.text

    def coure(self, courseid='', clazzid='', cpi='',time_=''):
        url = f'https://mooc2-ans.chaoxing.com/mooc2-ans/mycourse/studentcourse?courseid={courseid}&clazzid={clazzid}&cpi={cpi}&ut=s&t={time_}'
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
        }
        requests.packages.urllib3.disable_warnings()
        resp = self.session.get(url=url, headers=head, verify=False)
        return resp.text


if __name__ == "__main__":
    #?#################################################################################requests
    login = login.login()
    coure = coure(login=login, uname='13680968220', password='zzaa187765')
    text = coure.my_Home_page()
    with open('1.html', 'w', encoding='utf-8') as f:
        f.write(text)
    a_href = re.findall(
        r'<a href="https://mooc1-1.chaoxing.com/visit/stucoursemiddle\?(.*?)".*?<p class="overHidden1">班级：默认班级</p>', text, re.S)
    ccc = a_href[0].split('&')
    courseid = ccc[0].split('=')[1]
    clazzid = ccc[1].split('=')[1]
    ismooc2 = ccc[4].split('=')[1]
    cpi = ccc[3].split('=')[1]
    time_='1677829619335'
    text_ = coure.coure(courseid=courseid, clazzid=clazzid, cpi=cpi,time_=time_)
    with open('2.html', 'w', encoding='utf-8') as f:
        f.write(text_)
    mooc1Domain = 'https://mooc1.chaoxing.com'
    enc = re.search(r'var enc = "(?P<enc>.*?)";', text_).group('enc')
    cpi = re.search(r'var cpi = (?P<cpi>.*?);', text_).group('cpi')
    ckc = re.search(r'.*onclick="toOld\((?P<ckc>.*?)\)".*?class="knowledgeJobCount"', text_,re.S).group('ckc')
    ckc = ckc.replace('\'', '').split(',')
    courseid, knowledgeId, clazzid = (i.replace(' ','') for i in ckc)
    
    #?############################################################################selenium
    # option = webdriver.ChromeOptions()
    # option.add_experimental_option("detach", True)
    # # option.add_argument('headless')
    # driver=webdriver.Chrome(options=option)
    # print(dict(coure.session.cookies))
    # driver.delete_all_cookies()
    # driver.add_cookie(cookie_dict=dict(coure.session.cookies))
    # driver.get(f'https://mooc1.chaoxing.com/mycourse/transfer?moocId={courseid}&clazzid={clazzid}&ut=s&refer=https%3A%2F%2Fmooc1.chaoxing.com%2Fmycourse%2Fstudentstudy%3FchapterId%3D{knowledgeId}%26courseId%3D{courseid}%26clazzid%3D{clazzid}%26cpi%3D{cpi}%26enc%3D{enc}%26mooc2%3D1')