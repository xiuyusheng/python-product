
import requests
import json


def main():
        
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=XwBZxPgRYxRM26aacVRDIYXE&client_secret=bhIxtuY0yrirxlLwcdr1KSD6ckp3yjEE"
    
    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload).json()
    
    print(response['access_token'])
    

if __name__ == '__main__':
    main()