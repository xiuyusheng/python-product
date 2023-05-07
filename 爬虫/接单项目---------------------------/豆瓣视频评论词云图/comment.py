import requests
import re
from lxml import etree
import time
import jieba
import wordcloud

url = 'https://movie.douban.com/subject/35267208/reviews'
headers = {
    'Referer': 'https://movie.douban.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'
}
response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding
tree_result = etree.HTML(response.text)
comment_container = '/html/body/div[3]/div[1]/div/div[1]/div[1]/div[*]/@data-cid'
get_data_cid = tree_result.xpath(comment_container)
# # 遍历 data-cid
# for i in range(len(get_data_cid)):
#     print(get_data_cid[i])
#     # 评论链接
#     comment_url = 'https://movie.douban.com/j/review/'+get_data_cid[i]+'/full'
#     response = requests.get(url=comment_url, headers=headers)
#     response.encoding = response.apparent_encoding
#     com_data = etree.HTML(response.json()['body'])
#     movie_data = com_data.xpath('//text()')
#     n = 0
#     # 去除数据中的换行和空格
#     while n < len(movie_data):
#         movie_data[n] = re.sub('[\\n|\s]', '', movie_data[n])
#         if movie_data[n] == '':
#             movie_data.pop(n)
#             n -= 1
#         n += 1
#     movie_data = str(movie_data)
#     with open("test.txt", "a+", encoding='utf-8') as f:  # 打开文件
#         data = f.read()  # 读取文件
#         f.write(movie_data)  # 将movie_data写入文件
#     print(get_data_cid[i] + 'ok')
#     time.sleep(1)
print('done')
# 读取文本
with open("test.txt", encoding="utf-8") as f:
    s = f.read()
print(s)
ls = jieba.lcut(s)  # 生成分词列表
text = ' '.join(ls)  # 连接成字符串
stopwords = ["的", "是", "了",'和','在','都']  # 去掉不需要显示的词
wc = wordcloud.WordCloud(font_path="msyh.ttc",
                         width=2000,
                         height=2000,
                         background_color='white',
                         max_words=10000, stopwords=stopwords)
# msyh.ttc电脑本地字体，写可以写成绝对路径
wc.generate(text)  # 加载词云文本
wc.to_file("流浪地球2.png")  # 保存词云文件
