from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
# option.add_argument('headless')
driver=webdriver.Chrome(options=option)
driver.get('https://passport2.chaoxing.com/login?fid=&newversion=true&refer=http%3A%2F%2Fi.chaoxing.com')
driver.find_element(By.ID, "phone").send_keys('13680968220')
driver.find_element(By.ID, "pwd").send_keys('zzaa187765')
driver.find_element(By.ID, "loginBtn").click()
time.sleep(3)
driver.execute_script('window.open("https://mooc2-ans.chaoxing.com/mycourse/stu?courseid=233083344&clazzid=73321596&cpi=214872176&enc=9a04db2fa0c37566e27e26507f2dce3c&t=1677901544916&pageHeader=1&v=2")')
driver.forward()
driver.get('https://mooc2-ans.chaoxing.com/mooc2-ans/mycourse/studentcourse?courseid=233083344&clazzid=73321596&cpi=214872176&ut=s&t=1677901544916')
driver.forward()
