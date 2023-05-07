import requests
import uuid
class exam():
    def __init__(self) -> None:
        self.session=requests.Session()
    def check(self):
        # head={
        #     'Accept': '*/*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        # 'Cache-Control': 'no-cache',
        # 'Connection': 'keep-alive',
        # 'Host': 'exambackend.yooc.me',
        # 'Origin': 'https://exam.yooc.me',
        # 'Pragma': 'no-cache',
        # 'Referer': 'https://exam.yooc.me/',
        # 'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
        # 'sec-ch-ua-mobile': '?0',
        # 'sec-ch-ua-platform': "Windows",
        # 'Sec-Fetch-Dest': 'empty',
        # 'Sec-Fetch-Mode': 'cors',
        # 'Sec-Fetch-Site': 'same-site',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'
        # }
        # resp=self.session.get('https://exambackend.yooc.me/api/exam/user/check?groupId=7059928&userId=11920205&token=1291ee38487ad14ff91209a82a315287&yibanId=52645580',headers=head)
        # print(resp.cookies.get_dict())
        # resp=self.session.get('https://exambackend.yooc.me/api/exam/list/get?userId=11920205&token=1291ee38487ad14ff91209a82a315287&yibanId=52645580&groupId=7059928',headers=head)
        # print(resp.cookies.get_dict())
        resp=self.session.get('https://exambackend.yooc.me/api/exam/paper/get?examuserId=97001235&token=1291ee38487ad14ff91209a82a315287&yibanId=52645580')
        print(resp.text)
if __name__=="__main__":
    print('\u5206\u6570\u52a0\u5bc6\u9519\u8bef\uff01')
    # exam=exam()
    # exam.check()