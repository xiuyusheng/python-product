import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # 获取元素
from selenium.webdriver.support.ui import WebDriverWait  # 等待元素
from selenium.webdriver.support import expected_conditions as EC  # 等待搜索
import json
import re
import xlwt
import time
import random
if __name__ == "__main__":
    
    # 创建ChromeOptions对象
    chrome_options = Options()

    # 启用无头模式
    # chrome_options.add_argument('--headless')

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



    browser = webdriver.Chrome(service=s,options=chrome_options)
    wait = WebDriverWait(browser, 20)

    browser.get('https://piao.qunar.com/')

    # 获取cookie
    cookies = browser.get_cookies()

    # 将cookie转换为字典格式
    cookie_dict = requests.utils.dict_from_cookiejar(
        requests.utils.cookiejar_from_dict({c['name']: c['value'] for c in cookies}))
    
    browser.get('https://piao.qunar.com/ticket/list.htm?keyword=%E6%AD%A6%E6%B1%89&region=null&from=mps_search_suggest')


    for i in  wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[3]/div[1]/div'))):
        print(i.text)
        i.click()
        hao=wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[8]/ul/li[4]'))).text.replace('全部(').replace(')')
        zong=wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[8]/div[1]/div[3]/span[2]')))
        hao_lv=str(int(hao)/int(zong)*100)+"%"
        #关闭
        # browser.close()
        # print(i.text)

    time.sleep(20)
    # 关闭浏览器
    browser.quit()

    
    new_data.save('地址.xls')
            # with open('op.json','w',encoding='utf-8') as f:
            #     json.dump(resp.json(),f)
            # print(resp.json())
