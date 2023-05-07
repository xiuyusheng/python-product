import requests
import re
head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}


def get_url(num, session):
    url = 'https://ieltspracticeonline.com/ielts-writing/page/{}/'.format(num)
    resp = session.get(url=url, headers=head)
    with open('1.html','w',encoding='utf-8') as f:
        f.write(resp.text)
    return resp


if __name__ == "__main__":
    session = requests.Session()

    print(get_url(2,session=session).text)