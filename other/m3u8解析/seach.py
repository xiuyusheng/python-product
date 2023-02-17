import  requests
session=requests.Session()
a=session.get('https://v.qq.com/x/search/?q=%E4%B8%80%E4%BA%BA%E4%B9%8B%E4%B8%8B%20%E7%AC%AC5%E5%AD%A3&stag=0&&is_client=1')
a.encoding='utf-8'
with open('yrzx.txt','w',encoding='utf-8') as f:
    f.write(a.text)
print(a.text)