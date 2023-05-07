import Dec
import requests
import time


class exam():
    def __init__(self, cookies) -> None:
        self.session = requests.Session()
        self.session.cookies.update(cookies)
        self.head = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'www.yooc.me',
            'Pragma': 'no-cache',
            'Referer': 'https://www.yooc.me/dashboard/mygroup',
            'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39',
            'X-Requested-With': 'XMLHttpRequest'
        }

    def get_item(self):
        url = 'https://www.yooc.me/group/joined?_={}&page=1'.format(
            1681451110787)
        resp = self.session.get(url=url, headers=self.head)
        # print(self.session.cookies.get_dict())
        print(resp.text)


if __name__ == "__main__":
    # 定义一个 cookie 字符串
    cookie_str = 'csrftoken=3nOoCD2cLtPjCWTqD3RetgsYrJNn8RPO; Hm_lvt_435408cf352a14d68ef6861b9d51158c=1681439094,1681441937,1681442882,1681446475; user_token=dae173c9f6a2bf624de468c6a8731623; yiban_id=52645580; user_id=11920205; Hm_lpvt_435408cf352a14d68ef6861b9d51158c=1681459092'

    # 使用 requests.utils 方法将 cookie 字符串转换为字典
    cookie_dict = requests.utils.dict_from_cookiejar(requests.utils.cookiejar_from_dict(
        {i.split('=')[0]: i.split('=')[1] for i in cookie_str.split('; ')}))

    exam = exam(cookie_dict)
    exam.get_item()
