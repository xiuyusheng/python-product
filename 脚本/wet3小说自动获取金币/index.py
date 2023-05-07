import requests
import re
import random
import json
import ddddocr  # 验证码识别库
ocr = ddddocr.DdddOcr()


class WET3():
    def __init__(self, userid, password) -> None:
        self.userid = userid
        self.password = password
        self.session = requests.Session()
        self.head = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34'
        }

    def member(self):
        url = 'https://www.wet3.com/member.php?mod=logging&action=login'
        resp = self.session.get(url=url).text
        self.login_params = {
            'mod': 'logging',
            'action': 'login',
            'loginsubmit': 'yes',
            'handlekey': 'login',
            'loginhash': re.search(r'name="login" id="loginform_(?P<value>.*?)"', resp, re.S).group('value'),
            'inajax': '1'
        }
        self.login_data = {
            'formhash': re.search(r'type="hidden" name="formhash" value="(?P<value>.*?)"', resp, re.S).group('value'),
            'referer': re.search(r'type="hidden" name="referer" value="(?P<value>.*?)"', resp, re.S).group('value'),
            'loginfield': 'username',
            'username': self.userid,
            'password': self.password,
            'questionid': '0',
            'answer': '',
            'seccodehash': re.search(r'span id="seccode_(?P<value>.*?)"', resp, re.S).group('value'),
            'seccodemodid': re.search(r'<input type="hidden" name="srhlocality" value="(?P<value>.*?)"', resp, re.S).group('value')
        }

    def verify(self):
        self.head['referer'] = 'referer: https://www.wet3.com/member.php?mod=logging&action=login'
        verify_link = self.session.get(url='https://www.wet3.com/misc.php?mod=seccode&action=update&idhash={}&{}&modid={}'.format(
            self.login_data['seccodehash'], round(random.random(), 15), self.login_data['seccodemodid']), headers=self.head)
        path_ = re.search(
            r'src="(?P<val>.*?)" class="vm" alt="" />\';', verify_link.text).group('val')
        head = {
            'accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'referer': 'https://www.wet3.com/member.php?mod=logging&action=login',
            'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'sec-fetch-dest': 'image',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34'
        }
        self.head['accept'] = 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
        TP = self.session.get(
            url='https://www.wet3.com/{}'.format(path_), headers=head)
        self.login_data['seccodeverify'] = ocr.classification(TP.content)

    def login(self):
        while True:
            with open('cookie.json','r',encoding='utf-8') as f:#cookie
                cookies=json.load(f)
                self.session.cookies.update(cookies)
            resp=self.session.get(url='https://www.wet3.com/replyreward_7ree-replyreward_7ree.html',cookies=cookies)
            key=re.search(r'class="unfinish_7ree">',resp.text,re.S)
            if key:
                self.member()
                print('data、params已生成')
                self.verify()
                print('验证码已生成')
                url = 'https://www.wet3.com/member.php'
                self.session.post(url=url,params=self.login_params,data=self.login_data)
                self.session.cookies['cRsd_2132_vnm7ree_9518']='{"tid":"147197","num":8}'
                with open('cookie.json','w',encoding='utf-8') as fp:
                    json.dump(cookies,fp)
            else:
                break
        # print(resp.text) 
    def get_money(self):
        # print(self.session.cookies.get_dict())
        resp=self.session.get(url='https://www.wet3.com/plugin.php?id=replyreward_7ree&code=4&type_7ree=3')
        print(resp.text)

if __name__ == "__main__":
    wet = WET3('gkgk', '13247754')
    wet.login()
    wet.get_money()