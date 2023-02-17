import requests
from urllib.parse import unquote
session = requests.Session()
response = requests.get('https://gpc.campusphere.net/iap/login?service=https://gpc.campusphere.net/wec-counselor-apps/counselor/mobile-v2/index.html')
print(unquote(response.url))
