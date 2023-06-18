# https://www.jianshu.com/p/3df95dcbd92f/
# https://blog.csdn.net/qq_41831288/article/details/88706618?

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlencode
import csv
from selenium.common.exceptions import TimeoutException
import datetime
from selenium.webdriver.chrome.service import Service


#######################################
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"

# 设置谷歌驱动器的环境
options = webdriver.ChromeOptions()
# 设置chrome不加在图片，提高速度
# options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
# # 设置不显示窗口
# options.add_argument('--headless')
# 创建一个谷歌驱动器
s = Service("./chromedriver.exe")
driver = webdriver.Chrome(options=options, service=s)
driver.set_window_size(800, 900)
# driver.implicitly_wait(30)
# driver.maximize_window()


def ask_url():
    for page_year in range(86, 88):
        params = {
            "page_year": page_year,
        }
        url = "https://academic.oup.com/restud/issue/" + urlencode(params)
        url = url.replace("page_year=", "")
        # print(url)
        for page_month in range(1, 7):
            params = {
                "page_month": page_month,
            }
            url2 = url + "/" + urlencode(params)
            url2 = url2.replace("page_month=", "")
            print(url2)
            get_detail(url2)


def get_detail(url):
    # 打开每期期刊链接
    driver.get(url)
    time.sleep(19)

    # 获取每期期刊列表
    total = driver.find_elements(
        By.XPATH, '//div[@class="content al-article-list-group"]/div'
    )
    count = 1
    for li in total:
        try:
            time.sleep(5)
            # 每篇论文链接
            try:
                link = li.find_element(By.XPATH, "./div/h5/a").get_attribute("href")
                # print(link, '\n')
                get_url_detail(link)
            except:
                link = ""

        except:
            print(f"第{count}条爬取失败\n")
            # 跳过本条，接着下一个
            continue
        finally:
            # 如果有多个窗口，关闭第二个窗口，切换回主页
            n2 = driver.window_handles
            if len(n2) > 1:
                driver.close()
                driver.switch_to.window(n2[0])


def get_url_detail(link):
    # 打开新的标签页
    js = 'window.open("{}")'.format(link)
    driver.execute_script(js)
    time.sleep(5)
    # 获取driver的句柄
    n = driver.window_handles
    # driver切换至最新生产的页面
    driver.switch_to.window(n[-1])
    #
    article_info = {}
    time.sleep(5)
    # index = '第' + f'{count}' + "篇"
    # # print(index)
    # count += 1
    # 每篇论文标题
    try:
        name = driver.find_element(By.XPATH, '//div[@class="title-wrap"]/h1').text
        print(name)
    except:
        name = ""
        print("无标题")

    # 每篇论文日期
    try:
        date = driver.find_element(By.XPATH, '//div[@class="ww-citation-primary"]').text
        # print(date)
    except:
        date = ""
        print("无日期")
    # 每篇论文作者
    try:
        author = (
            driver.find_element(By.XPATH, '//div[@class="al-authors-list"]')
            .text.strip()
            .replace("\r", "")
            .replace("\n", "")
        )
        # print(author)
    except:
        author = ""
        print("无作者")
    # 每篇论文摘要
    try:
        Abstract = driver.find_element(By.XPATH, '//p[@class="chapter-para"]').text
        # print(Abstract)
    except:
        Abstract = ""
        print("无摘要")

    # items = '\n' + '================================' + '\n序号' + index + '\n日期' + date + '\n标题' + name + '\n作者' + author + '\n摘要' + Abstract
    items = (
        "\n"
        + "================================"
        + "\n日期"
        + date
        + "\n标题"
        + name
        + "\n作者"
        + author
        + "\n摘要"
        + Abstract
        + "\n"
    )
    # print(items)
    print(name)

    save_to_mongo(items)


def save_to_mongo(items):
    with open(
        "The Review of Economic Studies_2019-2021.txt",
        "a+",
        encoding="UTF-8",
        newline="",
    ) as fp:
        fp.write(items)


def main():
    start_time = datetime.datetime.now()
    try:
        ask_url()
    except Exception as e:
        raise e
    finally:
        driver.close()
    end_time = datetime.datetime.now()
    print("开始时间", start_time)
    print("结束时间", end_time)


if __name__ == "__main__":
    main()
