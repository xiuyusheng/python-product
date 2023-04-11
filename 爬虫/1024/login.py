import json
import requests
import time
import random

session = requests.Session()

resp = session.get(
    'https://1024code.com/api/v1/users/hot?page=1&range=last_week&page_size=77').json()  # 用户列表
result={
  'data':[]
}
for i in resp['items']:
    resp_ = session.get(
        url='https://1024code.com/api/v1/profile/{}'.format(i['slug'])).json()

    # 获取需要的信息
    result['data'].append({
        'name': resp_['name'],
        '主页地址': resp_['slug'],
        'phone': resp_['phone'],
        'readme': resp_['readme'],
        '公开': resp_['public_count'],
        '发布': resp_['publication_count']
    })
    
    # dumps方法用于  dict 转 json
    # ensure_ascii=False 防止json库将中文转换为unicode
    # result=json.dumps(result, ensure_ascii=False)

    # w+ 打开一个文件用于读写。如果该文件已存在则打开文件，
    # 并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
with open('1024code.json', 'w', encoding='utf-8') as f:
    # 将信息以json格式写入文件
    print(result)
    json.dump(result,f,ensure_ascii=False)
print('ok')