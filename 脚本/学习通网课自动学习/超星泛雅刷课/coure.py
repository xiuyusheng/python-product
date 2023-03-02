import requests
import login
import time
import re


class coure():
    def __init__(self, login) -> None:
        self.session = requests.Session
        self.session = login.login(uname='13680968220', password='zzaa187765')

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
        resp = self.session.post(url=url, headers=head,data=data)
        return resp.text

    def coure(self, courseid='', clazzid='', cpi=''):
        url = 'https://mooc2-ans.chaoxing.com/mooc2-ans/mycourse/studentcourse?courseid=233083403&clazzid=73321670&cpi=214872176&ut=s&t=1677735136584'
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
        }
        requests.packages.urllib3.disable_warnings()
        resp = self.session.get(url=url, headers=head, verify=False)
        return resp.text


if __name__ == "__main__":
    login = login.login()
    coure = coure(login=login)
    text = coure.my_Home_page()
    with open('1.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    a_href = re.findall(r'<a href="https://mooc1-1.chaoxing.com/visit/stucoursemiddle\?(.*?)".*?<p class="overHidden1">班级：默认班级</p>', text,re.S)
    print(a_href[:2])
    text_ = coure.coure()
    with open('2.txt', 'w', encoding='utf-8') as f:
        f.write(text_)
    # print(text_)
    mooc1Domain = 'https://mooc1.chaoxing.com'
    enc = re.search(r'var enc = "(?P<enc>.*?)";', text_).group('enc')
    cpi = re.search(r'var cpi = (?P<cpi>.*?);', text_).group('cpi')
    ckc = re.search(r'onclick="toOld\((?P<ckc>.*?)\)"', text_).group('ckc')
    ckc = ckc.replace('\'', '').split(',')
    courseid, knowledgeId, clazzid = (i for i in ckc)
