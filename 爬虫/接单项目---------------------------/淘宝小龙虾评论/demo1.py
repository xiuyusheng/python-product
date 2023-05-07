import requests
import re
import time
import pandas as pd
for page in range(1, 2):
    time.sleep(5)
    print('===============================正在爬取第{}页评论========================================'.format(page))
    url = 'https://h5api.m.tmall.com/h5/mtop.alibaba.review.list.for.new.pc.detail/1.0/?jsv=2.7.0&appKey=12574478&t=1683217017847&sign=c438a18dbb16d90d6a7a883bc9bf16be&api=mtop.alibaba.review.list.for.new.pc.detail&v=1.0&isSec=0&ecode=0&timeout=10000&dataType=json&valueType=string&ttid=2022%40taobao_litepc_9.17.0&AntiFlood=true&AntiCreep=true&preventFallback=true&type=json&data=%7B%22itemId%22%3A%22707309391393%22%2C%22bizCode%22%3A%22ali.china.tmall%22%2C%22channel%22%3A%22pc_detail%22%2C%22pageSize%22%3A20%2C%22pageNum%22%3A1%7D'
    params = {
        'itemId': '629312145676',
        'spuId': '1868837056',
        'sellerId': '1917047079',
        'order': '3',
        'currentPage': page,
        'append': '0',
        'content': '1',
        'tagId': '',
        'posi': '',
        'picture': '',
        'groupId': '',
        'ua': '098#E1hvhvvUvbpvjQCkvvvvvjiWP2Sw0jiUPsMW1jnEPmPWAjiPPszZljYRR2FpljkevpvhvvCCB29CvvpvvhCv29hvCPMMvvvvvpvVvvBvpvvvKvhv8vvvphvvvvvvvvCj1Qvv9WyvvhNjvvvmjvvvBGwvvvUUvvCj1Qvvv9kIvpvUvvCCnlyyQrRUvpvVvpCmp/2hmvhvLvh0KfyaYb8rVXIaWXxrVBeK5kx/AWkKDBhBfvDrAEuK5u6aWXxrVBuK55CwiNoOVX+ffCuYiLUpVE6Fp+0xhCIaRoxBlwyzhboJEcg=',
        'needFold': '0',
        '_ksTS': '1607761234164_354',
        'callback': 'jsonp355',
    }
    headers = {
        'cookie': 'dnk=%5Cu4E0D%5Cu4E8C%5Cu4E8C%5Cu4F1F; uc1=cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&cookie14=Uoe8idJozkekeA%3D%3D&existShop=false&cookie21=U%2BGCWk%2F7p4mBoUyS4E9C&pas=0; uc3=lg2=U%2BGCWk%2F75gdr5Q%3D%3D&id2=UU27K3%2BhaZQKTg%3D%3D&vt3=F8dCsfPl3NbIbQiB7eI%3D&nk2=0XmC%2F8Kl%2Bic%3D; tracknick=%5Cu4E0D%5Cu4E8C%5Cu4E8C%5Cu4F1F; lid=%E4%B8%8D%E4%BA%8C%E4%BA%8C%E4%BC%9F; uc4=id4=0%40U2%2F8nS7rYPcxHk8jIkhFe38yVCNP&nk4=0%4000Gp7rnFQQAzLeVXxTaYICjrJA%3D%3D; _l_g_=Ug%3D%3D; unb=2594645654; lgc=%5Cu4E0D%5Cu4E8C%5Cu4E8C%5Cu4F1F; cookie1=W8Dc1F8Y9Wqp22LRtJUy%2FXiYEd%2BOGMQT7zQSlkJoPeg%3D; login=true; cookie17=UU27K3%2BhaZQKTg%3D%3D; cookie2=1c736faf7911fa73a55646cf04b2fe21; _nk_=%5Cu4E0D%5Cu4E8C%5Cu4E8C%5Cu4F1F; sgcookie=E100FY2JgL0%2FiPfIvXIdr8Un%2FlYXIWZHqnDizHXyQHyU8wtGyAZ4NrWJf2UGYugqgocGWiLwO%2BhN2n8r9t%2FADgkJo%2FwbrXXJZuryRyy5to1Aad8%3D; cancelledSubSites=empty; t=d7c5e6ef7f103573a32e6614907d6ab5; sg=%E4%BC%9F44; csg=599ff2a1; _tb_token_=357e37ee1417; cna=BgzYHFCydAgBASQOA2Zmj4r2; xlly_s=1; _m_h5_tk=49954dc2dd420d345410a14f0bb4667d_1683221435104; _m_h5_tk_enc=bd61808e3a0faaa243a214d0369fcd61; tfstk=clafBux5jKvX2aQMox1zPzzg1o3fZQBSZiMYGtkh3YwNJfVfi68EdjTQjL0Z6b1..; l=fBa7hnoqNiXUkPqaBO5aourza77tiIObzsPzaNbMiIEGa6iFwFPqnNC_n1TJkdtjgTfjaetrBZyM6dEHJeap0YNc13fREpZwoxJw-bpU-L5..; isg=BPX1qdTP_ec5rxlaTcB6cbtVBHGvcqmEFoy1f3cbtmyjThdAP8IpVBjImBL4DsE8',
        'referer': 'https://detail.tmall.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }
    response = requests.get(url=url, params=params, headers=headers)
    lis = re.findall('"rateContent":"(.*?)"', response.text)
    for li in lis:
        with open('淘宝评论.txt', mode='a', encoding='utf-8') as f:
            f.write(li)
            f.write('\n')
            print(li)
            print(lis)
df = pd.DataFrame()
df['评论'] = lis
df.to_excel('小龙虾评论数据.xlsx',index=None)