import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json
import re
import xlwt
import time
import random
if __name__ == "__main__":
    
    # 创建ChromeOptions对象
    chrome_options = Options()

    # 启用无头模式
    chrome_options.add_argument('--headless')

    # 创建一个Chrome浏览器实例
    s = Service("./chromedriver.exe")
    # 创建xls实例
    new_data = xlwt.Workbook()
    # 创建工作页
    work_sheet = new_data.add_sheet('sheet1')

    # 初始化列明

    work_sheet.write(0, 0, 'lat')
    work_sheet.write(0, 1, 'lng')
    work_sheet.write(0, 2, '景点名称')
    work_sheet.write(0, 3, '略提到的数')
    work_sheet.write(0, 4, '点评数')
    work_sheet.write(0, 5, '好评率')

    
    def head_get():
        '''
        随机获取一个headers
        '''
        user_agents =  ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50','Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11']
        headers = {'User-Agent':random.choice(user_agents)}
        return headers
    # browser.get('https://piao.qunar.com/')

    # # 获取cookie
    # cookies = browser.get_cookies()

    # # 将cookie转换为字典格式
    # cookie_dict = requests.utils.dict_from_cookiejar(
    #     requests.utils.cookiejar_from_dict({c['name']: c['value'] for c in cookies}))

    # session.cookies.update(cookie_dict)
    num=1
    for i in range(50):
        # 创建session实例
        session = requests.Session()

        browser = webdriver.Chrome(service=s,options=chrome_options)
        browser.get('https://piao.qunar.com/')

        # 获取cookie
        cookies = browser.get_cookies()

        # 将cookie转换为字典格式
        cookie_dict = requests.utils.dict_from_cookiejar(
        requests.utils.cookiejar_from_dict({c['name']: c['value'] for c in cookies}))

        # 关闭浏览器
        browser.quit()
        #转换cookie为可用字典
        session.cookies.update(cookie_dict)
        head=head_get()
        resp = session.get(
            'https://piao.qunar.com/ticket/list.json?keyword=%E6%AD%A6%E6%B1%89&region=null&from=mps_search_suggest&page={}'.format(i+1), headers=head)
        
        try:
            for j in resp.json()['data']['sightList']:
                session.get(
                    'https://piao.qunar.com/ticket/detail_824368214.html?st={}'.format(j['searchTrace']), headers=head)
                head['referer']='https://piao.qunar.com/ticket/detail_824368214.html?st={}'.format(j['searchTrace'])
                try:
                    zz=session.get('https://piao.qunar.com/ticket/detailLight/sightCommentList.json?sightId=201733&index=1&page=1&pageSize=10&tagType=0',headers=head).json()['data']
                    point=j['point'].split(',')
                    work_sheet.write(num, 0, point[0])
                    work_sheet.write(num, 1, point[1])
                    work_sheet.write(num, 2, j['sightName'])
                    work_sheet.write(num, 3, '略提到的数')
                    work_sheet.write(num, 4, zz['commentCount'])
                    work_sheet.write(num, 5, str(int(zz['tagList'][6]['tagNum']/zz['commentCount']*100))+'%')
                    num+=1
                    print(j['sightName'],num)
                except:
                    pass
        except:
            pass
    new_data.save('地址1.xls')
            # with open('op.json','w',encoding='utf-8') as f:
            #     json.dump(resp.json(),f)
            # print(resp.json())
