import requests
import login_token

token=login_token.token()#青年大学习网页token
MyclassName = {#团员名单
    '李佳泉': 2106200202,
    '曾勇辉': 2106200204,
    '吴玉萍': 2106200205,
    '叶俊威': 2106200206,
    '陈美静': 2106200207,
    '林育生': 2106200209,
    '胡梦芹': 2106200213,
    '郑腾跃': 2106200214,
    '庄佳胜': 2106200215,
    '李灿植': 2106200216,
    '林炼培': 2106200218,
    '孙湃钒': 2106200219,
    '卢敏如': 2106200222,
    '阮宇航': 2106200223,
    '蔡梓沛': 2106200226,
    '郭卓佳': 2106200231,
    '林曼如': 2106200232,
    '林小荣': 2106200235,
    '方洪宇': 2106200236,
    '郑凯立': 2106200237,
    '钟广源': 2106200238,
    '邓林彬': 2106200239,
    '刘纯娜': 2106200240,
    '李铧斌': 2106200245,
    '李健宏': 2106200246,
    '李硕': 2106200248,
    '林杰鹏': 2106200253
}
head3 = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27',
    'X-Litemall-IdentiFication': 'young'
}
resp4 = requests.post(
    f'https://youthstudy.12355.net/apibackend/user/info?token={token}',
    headers=head3)

# print(resp4.text)
resp4_json = resp4.json()

organizeId = resp4_json['data']['entity']['organizeId']  #organizeId既oid
head2 = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27',
    'X-Litemall-Admin-Token':
    token,
    'X-Litemall-IdentiFication': 'young'
}
for i in range(1,3):
    resp4=requests.get(f'https://youthstudy.12355.net/apibackend/admin/young/organize/sort/count?idList={organizeId}',headers=head2)
    learn_numbers=resp4.json()

    resp3 = requests.get(
        f'https://youthstudy.12355.net/apibackend/admin/young/organize/userList?organizedId={organizeId}&member=0&pageNo={i}',
        headers=head2)
    List = resp3.json()
    for j in List['data']['list']:
        del MyclassName[j['name']]#将以学习的名单从团员字典中删除


tuan_learn_number=learn_numbers['data']['entity']['resultList'][0]['data']['learns']#团员学习人数
qun_learn_number=learn_numbers['data']['entity']['resultList'][0]['data']['thisLearnsMasses']#群众学习人数
# print(tuan_learn_number)
# print(qun_learn_number)
if(not len(MyclassName) == 0):
    print("青年大学习未学习名单：\n")
    for i in MyclassName:
        print(i,MyclassName[i])
else:
    print('本周团员已全部学习')