import login
import re
import time


class Exam():
    def __init__(self, session) -> None:
        self.session = session
        self.head = {
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62'
        }
        # print(self.session.cookies.get_dict())

    def exchange(self):
        url = 'https://www.yooc.me/yiban_account/sso?token={}'.format(
            self.session.cookies['yiban_user_token'], allow_redirects=False)
        self.session.get(url=url, headers=self.head)

    def get_group(self, groupname):
        url = 'https://www.yooc.me/group/joined?_={}&page=1'.format(
            int(time.time()))
        head = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'www.yooc.me',
            'Pragma': 'no-cache',
            'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'
        }
        resp = self.session.get(url=url, headers=head).json()
        # print(resp)
        for i in resp['items']:
            if i['title'] == groupname:
                self.group = 'https://www.yooc.me{}'.format(i['url'])
                break

    def user_id(self):
        head = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'www.yooc.me',
            'Pragma': 'no-cache',
            'Referer': 'https: // www.yooc.me/mobile/dashboard/my_group',
            'sec-ch-ua': '"Chromium",v = "112", "Microsoft Edge",v = "112", "Not:A-Brand",v = "99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0Win64x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'
        }
        self.session.get(
            'https://www.yooc.me/mobile/dashboard/my_group', headers=self.head)
        url = '{}/index'.format(self.group)
        resp = self.session.get(url=url, headers=self.head, allow_redirects=False)
        # print(resp.url)
        print(resp.text, self.session.cookies.get_dict())


if __name__ == "__main__":
    log = login.Login(USER='17676520416', PASSWORD='20030216abc')
    log.login_get()  # 获取密钥
    log.login()
    exam = Exam(log.session)
    exam.exchange()  # 更优课用token交换cookie
    exam.get_group("国家安全知识竞答")
    exam.user_id()
