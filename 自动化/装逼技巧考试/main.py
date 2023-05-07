from selenium import webdriver
from selenium.webdriver.common.by import By  # 获取元素
from selenium.webdriver.support.ui import WebDriverWait  # 等待元素
from selenium.webdriver.support import expected_conditions as EC  # 等待搜索
from selenium.webdriver.chrome.service import Service
import time
import json
import ddddocr#验证码识别库
ocr = ddddocr.DdddOcr()
if __name__ == "__main__":

    # 创建Chrome实例
    s = Service("./chromedriver.exe")
    driver = webdriver.Chrome(service=s)

    # 等待搜索框加载完成
    wait = WebDriverWait(driver, 160)

#     driver.get('https://passport2.chaoxing.com/login?loginType=3&newversion=true&fid=-1&hidecompletephone=0&ebook=0&allowSkip=0&forbidotherlogin=0&refer=http%3A%2F%2Fi.chaoxing.com&accounttip=&pwdtip=&doubleFactorLogin=0&independentId=0')
    
#     school=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/form/div[1]/input')))
#     userid=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/form/div[3]/input')))
#     password=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/form/div[4]/input')))
# #     img_=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/form/div[5]/div/img'))).get_attribute('src')
# #     js_code = """
# # var imgElement = document.querySelector('.image');


# # var canvas = document.createElement('canvas');

# # canvas.width = imgElement.width;
# # canvas.height = imgElement.height;

# # var ctx = canvas.getContext('2d');
# # ctx.drawImage(imgElement, 0, 0);

# # canvas.toBlob(function(blob) {}, 'image/png');
# #                 """
# #     file = driver.execute_script(js_code)
# #     print(file)
# #     Verification_code=ocr.classification(file)
#     Verification=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/form/div[5]/input')))
#     school.send_keys('广东工程职业技术学院')
#     userid.send_keys('2106200248')
#     password.send_keys('20030216abc')
#     Verification.click()
#     wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div[2]/div/div/h1'))).click()
#     wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/ul/li/h1'))).click()
#     time.sleep(2)
#     wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/ul/li[1]'))).click()
######################################################################################3

    driver.get('https://passport2.chaoxing.com/login?fid=&newversion=true&refer=https://i.chaoxing.com')
    element = wait.until(EC.title_contains('个人空间'))
    print('页面跳转')

    iframe=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[3]/iframe')))
    driver.switch_to.frame(iframe)
    wait = WebDriverWait(driver, 160)
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[1]'))).click()
    
    # 切换控制最后一个页面
    handles = driver.window_handles
    new_handle = handles[-1]
    driver.switch_to.window(new_handle)
    wait = WebDriverWait(driver, 160)
    # # 切回原标签页
    # old_handle = handles[0]
    # driver.switch_to.window(old_handle)

    #点击任务
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/ul[1]/li[5]/a'))).click()
    classId=driver.find_element(By.ID,'clazzid').get_attribute('value')
    cpi=driver.find_element(By.ID,'cpi').get_attribute('value')
    # 转入iframe
    iframe=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/iframe[2]')))
    driver.switch_to.frame(iframe)
    wait = WebDriverWait(driver, 160)
    script=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/ul/li/div[1]'))).get_attribute('onclick')
    
    def goTest(courseId, tId, id, endTime, paperId, isRetest,lookpaperEnc):
        driver.get('https://mooc1.chaoxing.com/exam-ans/exam/test/examcode/examnotes?courseId={}&classId={}&examId={}&cpi={}'.format(courseId,classId,tId,driver.find_element(By.ID,'cpi').text))
    eval(script[:-1].replace('false','False'))
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[3]/i'))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[4]/div[1]/a'))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[8]/div/div[4]/a[1]'))).click()
    with open('1.json','r',encoding='utf-8') as f:
        answer=list(i['answer'] for i in json.load(f)['data'])
    print(answer)
    for _ in range(len(answer)):
        time.sleep(1)
        for i in wait.until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[3]/div[2]/div/div/div[1]/form/div/div'))):
            print(i.text[2:])
            
            if i.text[2:] in answer:
                i.click()
                print(i.text)
        time.sleep(1)
        wait.until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[3]/div[2]/div/div/div[2]/a')))[-1].click()






    time.sleep(20)