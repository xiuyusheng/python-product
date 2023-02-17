from urllib import response
import requests
url = 'https://errlog.umeng.com/apm_logs'
header = {
    'Accept':
    '*/*',
    'Accept-Encoding':
    'gzip, deflate, br',
    'Accept-Language':
    'zh-Hans-CN;q=1',
    'Connection':
    'keep-alive',
    'Content-Length':
    '659',
    'Content-Type':
    'multipart/form-data; boundary=Boundary+DBDC49FFE9870BAC',
    'Host':
    'errlog.umeng.com',
    'User-Agent':
    'CampusNext/9.2.1 (iPhone; iOS 15.5; Scale/2.00)',
    'Wpk-header':
    'app=58ac3a2a4544cb4a91001516&cver=1651209273&de=1&os=iOS&seq=1661912895344&sver=1.5.6.umeng&tm=1661912894&type=startperf&ud=A3944AA2-6B4C-474E-B3DB-39F012B57C2B&um_sdk_ver=1.5.6&ver=9.2.1&sign=53a6b5a642d4c3f2bcd797acc65ddfe6'
}
data = {
    "ctime":"1661912890",
    "wd_exec": 1661910451600,
    "um_crash_sdk_version": "1.5.6",
    "wl_page": 180,
    "w_pgid": "C303B5E0-081D-4A94-9BD9-FF0FC805AF42",
    "dsp_w": "375",
    "dsp_h": "667",
    "wd_init": 1661912852904,
    "um_ver": "9.2.1",
    "lang": "zh-Hans",
    "wd_inittm": 1661912853226,
    "tzone": "Asia\/Shanghai",
    "wd_buildtm": 1661912853234,
    "um_sdk_type": "iOS",
    "wl_exec": 2401303,
    "um_app_provider": "",
    "wd_exectm": 1661912852904,
    "vcode": "1",
    "type": "startperf",
    "wd_pagetm": 1661912853414,
    "um_access_subtype": "unknown",
    "rom": "15.5",
    "wd_build": 1661912853226,
    "brand": "Apple",
    "w_type": 1,
    "um_umid": "6b1f761c7a88c6725b5257d13d82f3b",
    "wl_init": 322,
    "um_root": "NO",
    "um_vcode": "1",
    "pkg": "com.wisedu.cpdaily",
    "um_app_channel": "Testing",
    "um_app_carrier": "Carrier",
    "w_url": "MCPTabBarViewController",
    "model": "iPhone10,4",
    "w_tm": "1661912890",
    "stime": "1661912855",
    "um_app_puid": "",
    "um_app_key": "58ac3a2a4544cb4a91001516",
    "appid": "58ac3a2a4544cb4a91001516",
    "os": "iOS",
    "appmem": "38",
    "fr": "ios",
    "tmem": "2068037632",
    "wd_page": 1661912853234,
    "um_app_start_time": 1661912855329,
    "wl_build": 8,
    "wid": "A3944AA2-6B4C-474E-B3DB-39F012B57C2B",
    "um_access": "WiFi",
    "net": "wifi",
    "ver": "9.2.1",
    "sdk_ver": "1.5.6.umeng",
    "wl_avgv": 2401813
}
respons=requests.post(url,header,data)
print(respons.text)