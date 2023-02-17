import requests
import login_token
import re
from io import BytesIO
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
import os
import time
import warnings

# -*- coding:utf-8 -*-
import json
def handler (event, context):
    warnings.filterwarnings("ignore",category=DeprecationWarning)#去除警告
    def ml_url():#图片链接和
        token=login_token.token()
        url='https://youthstudy.12355.net/apibackend/admin/young/QRCode'
        head = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27',
        'X-Litemall-Admin-Token':
        token,
        'X-Litemall-IdentiFication': 'young'
    }
        resp=requests.post(url=url,headers=head).json()
        entity=resp['data']['entity']
        return (re.search(r'\"url\":\"https://h5.cyol.com/special/daxuexi/(?P<url>.*?)/index.html\",',entity).group('url')),(re.search(r'index.html","chapterName":"(?P<chapterName>.*?)","chapterId"',entity).group('chapterName'))
    def end_img(mlurl):
        url=f'https://h5.cyol.com/special/daxuexi/{mlurl}/images/end.jpg'
        resp=requests.get(url=url)
        return resp.content
    def paste(img,ID,chapterName):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()).split(' ')[1][:-3]
        print(f'时间：{current_time}')
        bytes_stream = BytesIO(img)
        img_study = Image.open(bytes_stream)#获取图片对象
        img_top = Image.open('IN/'+ID)
        img_top = img_top.filter(ImageFilter.SHARPEN)
        img_top = img_top.filter(ImageFilter.SHARPEN)
        ID_=ID[:-4]
        img_top.thumbnail((img_study.size[0],img_top.size[1]*(img_top.size[0]/img_study.size[0])))#对图片进行缩放
        img3=Image.new('RGB', (img_study.size[0],img_study.size[1]+img_top.size[1]))#创建图片对象，第一个参数图片模式（一般为RGB模式），第二个参数为一个二位元组（宽，高），第三个可选参数为color，即一个单调颜色
        img3.paste(img_top, box=(0,0), mask = None)#图片粘贴，第一个为粘贴的图片对象，第二个为粘贴位置（通过像素点选择，二元组或者四元组）
        img3.paste(img_study, box=(0,img_top.size[1]), mask = None)
        img_draw = ImageDraw.Draw(img3)#声明图像绘图
        font=ImageFont.truetype(r'zt.ttf', 34)
        w,h=font.getsize(chapterName)
        font1=ImageFont.truetype(r'zt.ttf', 28)
        w1,h1=font.getsize(current_time)
        img_draw.text((random.random()*(img3.size[0]-600), random.random()*(img3.size[1]-400)+230), ID_,fill=(0,0,0), font=ImageFont.truetype(r'zt.ttf', 74))
        img_draw.text(((img3.size[0]-w)/2,100), chapterName,fill=(0,0,0),font=font )
        img_draw.text(((img3.size[0]-w1),17), current_time,fill=(0,0,0),font=font1 )
        
        img3.save('ON/'+str(ID))
        print(ID+'截图已生成')
        # img3.show()
        


    if __name__=="__main__":
        try:
            IDList=os.listdir('IN')
            if(IDList==[]):
                print('图片头部（IN文件夹下）不能为空，格式为一个学号一行')
            else:
                for i in IDList:
                    mlurl,chapterName=ml_url()
                    img=end_img(mlurl)
                    print(chapterName)
                    paste(img=img,ID=i,chapterName=chapterName)
            os.startfile('ON')
        except Exception as e:
            print('error: '+str(e))
        os.system("pause")
    return {
        "statusCode": 200,
        "isBase64Encoded": False,
        "body": json.dumps(event),
        "headers": {
            "Content-Type": "application/json"
        }
    }