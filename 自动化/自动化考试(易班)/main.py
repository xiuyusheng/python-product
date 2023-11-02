from selenium import webdriver
from selenium.webdriver.common.by import By  # 获取元素
from selenium.webdriver.support.ui import WebDriverWait  # 等待元素
from selenium.webdriver.support import expected_conditions as EC  # 等待搜索
from selenium.webdriver.chrome.service import Service
import time
import re
import json
import Dec
import random

if __name__ == "__main__":


    # 创建Chrome实例
    
    with open('pack.json','r',encoding='utf-8') as f:
        Data=json.load(f)
    for D in Data['data']:
        s = Service("./msedgedriver.exe")
        driver = webdriver.Edge(service=s)

        # 打开网页
        driver.get(
            D['coure'])

        # 等待搜索框加载完成
        wait = WebDriverWait(driver, 20)
        phone = wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/section/div/form/div[1]/input')))
        password = wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/section/div/form/div[2]/input')))

        # 输入关键词
        phone.send_keys(D['userid'])
        password.send_keys(D['password'])

        submit = wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/section/div/form/div[4]/input')))
        # 通过js点击登录按钮
        driver.execute_script("arguments[0].click();", submit)

        aa = wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div[1]/button')))
        time.sleep(1)
        # ?加入课群
        if aa.text == '加入':
            aa.click()
            wait.until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/div[5]/div[3]/button[2]'))).click()
        # ?点击进入考试
        for p in  wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, '/html/body/div[1]/div/ul/li'))):
            if p.text == "在线考试" and aa.text != '加入':
                p.click()
        # ?XPATH地址
        path_ = '/html/body/div/div[1]/div[2]/main/article/div/div[5]/button[2]' \
            if '分' in wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[2]/main/article/div/div[3]/div/span'))).text else \
            '/html/body/div/div[1]/div[2]/main/article/div/div[5]/button'
        # 考试前一个按钮
        bb = wait.until(EC.presence_of_element_located((By.XPATH, path_)))
        c_key = False if bb.text == '继续考试' else True
        # elif '重做试卷' in bb.text:
        if '重做试卷' in bb.text:
            bb.click()
            wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div[1]/div[2]/main/article/div/div[5]/div/div/div[2]/button[2]'))).click()
        else:
            bb.click()

        wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div[1]/div[2]/main/article/div[3]/button'))).click()
        if c_key:
            wait.until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div/div[1]/div[2]/main/article/div[3]/div/div/div[2]/button[2]'))).click()

        # ?等待交卷按钮出现开始解析
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[3]/div/button')))
        # 获取localStorage数据
        local_storage = driver.execute_script('return window.localStorage;')
        for i in local_storage:
            if 'exam-paper-' in i:
                answers = json.loads(local_storage[i])
                # print(answers)

                # 获取加密的盐值
                js_code = """
                var xhr = new XMLHttpRequest();
                xhr.open('GET', 'https://exam.yooc.me/index-d5a27.js', false);
                xhr.send();
                return xhr.response;
                """
                file = driver.execute_script(js_code)
                iv = (re.search(r'u\(\"(?P<iv>.{16})\"\)', file).group('iv'))

                # 获取当前域名下的cookie
                cookies = driver.get_cookies()
                current_cookies = [
                    cookie for cookie in cookies if cookie['name'] == 'yiban_id']
                key = current_cookies[0]['value']

                # 答案解密
                decrypto = Dec.crypto(iv_=iv, yibanid=key)

                # 当前题目
                print('开始答题')
                for i in answers['value']['paper']:
                    print(i['subjects'])
                    for j in i['subjects']:
                        time.sleep(random.random()*2)
                        an =  re.search( r"\[\"(?P<uu>.*?)\"\]", decrypto.decrypto(j["answer"])).group("uu").encode('utf-8').decode('unicode_escape')
                        k = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'exam-input')))
                            #  for k in wait.until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/main/main/div/div/div/div/div/ul/li'))):
                        k[0].click()
                        print(an)
                        k[0].send_keys(an)
                        wait.until(EC.presence_of_element_located(
                            (By.XPATH, '/html/body/div[1]/div[1]/div[2]/main/main/div/ul/li[4]/button'))).click()
                wait.until(EC.presence_of_element_located(
                            (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[3]/div/button'))).click()
                wait.until(EC.presence_of_element_located(
                            (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[3]/div/div/div/div[2]/button[2]'))).click()
                time.sleep(1)
                driver.close()
