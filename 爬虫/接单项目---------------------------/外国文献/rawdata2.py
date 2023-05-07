#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:29:44 2023

@author: shihan_li
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
import re
import time
agent_list = [
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

# 爬取的年份、volumn和issue
year = 2022
volumn = 137
issues = [1, 2, 3, 4]  # 爬取的期数

# 存储文章信息的列表
articles = []
# 遍历每期期刊，爬取文章信息
for issue in issues:
    # 请求页面
    url = r"https://academic.oup.com/qje/issue/"+str(volumn)+"/"+str(issue)
    UA = random.choice(agent_list)
    response = requests.get(url, headers={'User-Agent': UA}, timeout=10)
    time.sleep(10)
    # 解析页面
    soup = BeautifulSoup(response.text, 'lxml')

    # 找到文章列表
    article_list = soup.find_all("div", class_="al-article-items")
    # 遍历每篇文章，提取标题和摘要信息，并存储到列表中
    for article in article_list:
        title = article.find("h5", class_="customLink item-title").text.strip()
        # abstract = article.find("section", class_="abstract").text.strip()
        ##################################################################3
        # 获取articleId
        data_articleid = soup.select('[data-articleid]')
        for o in data_articleid:
            time.sleep(3)
            try:
                # 请求Abstract
                resp = requests.get(url='https://academic.oup.com/qje/PlatformArticle/ArticleAbstractAjax?articleId={}&layAbstract=false'.format(
                    o['data-articleid']), headers={'User-Agent': UA, 'Referer': url}).json()
            except:
                break
            #正则匹配文章部分
            Abstract = re.search(
                r'<section class=\"abstract\"><p class=\"chapter-para\">(?P<html>.*?)</p></section>', resp['Html']).group('html')
            #####################################################################
            article_info = [year, volumn, issue, title, Abstract]
            print(f"Article info: {article_info}")
            articles.append(article_info)

# 将文章信息转换为DataFrame
df = pd.DataFrame(articles, columns=[
                  "Year", "Volumn", "Issue", "Title", "Abstract"])#此处添加了一列
# print(articles)
# 将DataFrame保存为Excel文件
df.to_excel("QJE_2022.xlsx", index=False)
