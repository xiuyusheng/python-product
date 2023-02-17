import  requests
url = 'https://localhost.ptlogin2.qq.com:4301/pt_get_uins?callback=ptui_getuins_CB&pt_local_tk=1'
headers = {
    'Cookie': 'pt_local_token=1',
    'Referer': 'https://xui.ptlogin2.qq.com/'
}
print(requests.get(url=url,headers=headers).text)