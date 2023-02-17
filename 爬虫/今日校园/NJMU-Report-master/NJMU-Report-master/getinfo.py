from common import SchoolLogin,get_info
import login


def parse(info):
    info.update({'CREATED_AT': '',
                 'CZRQ': '',
                 'FILL_TIME': '',
                 'NEED_CHECKIN_DATE': '',
                 'WID': ''})
    with open('疫情打卡提交信息.txt', 'w+', encoding='utf-8') as f:
        for i in info.keys():
            if info[i] is None:
                line = i + ': '
            else:
                line = i + ': ' + info[i]
            print(line, file=f)


s = SchoolLogin()
cookies = login.login()
info_dict = get_info(cookies)
parse(info_dict)
