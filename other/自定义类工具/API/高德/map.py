import requests

class gaode():

    ###############################################################
    ##https://lbs.amap.com/api/webservice/guide/api   api在线文档##
    ###############################################################

    def __init__(self,key) -> None:#高德官网认证获取token
        self.key=key
        
    def tianqi(self,city='440106',extensions='',output='JSON'):
        url='https://restapi.amap.com/v3/weather/weatherInfo'
        params={
            'key':self.key,
            'city':city,#城市镇区的编号
            'extensions':extensions,#可选值：base/all   base:返回实况天气 all:返回预报天气
            'output':output#返回格式  可选值：JSON,XML
        }
        params=dict((k,v) for k,v in params.items() if v!='')
        resp=requests.get(url=url,params=params)#天气
        return resp

    def dingwei(self,ip='',sig=''):
        url='https://restapi.amap.com/v3/ip'
        params={
            'key':self.key,
            'ip':ip,#填写则根据此IP进行解析地址，不填写则用请求所带IP
            'sig':sig#付费用户填写的签名认证
        }
        params=dict((k,v) for k,v in params.items() if v!='')
        resp = requests.get(url=url,params=params)
        return resp

    def static_map(self,location='116.481485,39.990464',name=False,zoom=10,size='400*400',scale='1',markers='',labels='',paths='',traffic=0,sig=''):
        url='https://restapi.amap.com/v3/staticmap'
        name=location if not name else name
        params={
            'key':self.key,
            'location':location,#坐标   规则：经度和纬度用","分隔 经纬度小数点后不得超过6位。
            'zoom':zoom,#地图缩放级别:[1,17]
            'size':size,#图片宽度*图片高度。最大值为1024*1024
            'scale':scale,#默认为1 1:返回普通图；2:调用高清图，图片高度和宽度都增加一倍，zoom也增加一倍（当zoom为最大值时，zoom不再改变)
            'markers':markers,#标注最大数10个
                        #格式：
                        #markers=markersStyle1:location1;location2..|markersStyle2:location3;location4..|markersStyleN:locationN;locationM.. 
                        #ocation为经纬度信息，经纬度之间使用","分隔，不同的点使用";"分隔。 markersStyle可以使用系统提供的样式，也可以使用自定义图片。
                        #系统marersStyle：label，font ,bold, fontSize，fontColor，background。
            'labels':labels,#标签最大数10个
                        #格式：
                        #labels=labelsStyle1:location1;location2..|labelsStyle2:location3;location4..|labelsStyleN:locationN;locationM.. 
                        #location为经纬度信息，经纬度之间使用","分隔，不同的点使用";"分隔。
                        #labelsStyle：label, font, bold, fontSize, fontColor, background。 各参数使用","分隔，如有默认值则可为空
            'paths':paths,#折线和多边形最大数4个
                        #格式：      
                        #paths=pathsStyle1:location1;location2..|pathsStyle2:location3;location4..|pathsStyleN:locationN;locationM..     
                        #location为经纬度，经纬度之间使用","分隔，不同的点使用";"分隔。
                        #pathsStyle：weight, color, transparency, fillcolor, fillTransparency。
            'traffic':traffic,#底图是否展现实时路况。 可选值： 0，不展现；1，展现。
            'sig':sig#付费用户填写的签名认证
        }
        params=dict((k,v) for k,v in params.items() if v!='')
        resp=requests.get(url=url,params=params)
        with open(f'{name}.png','wb') as f:
            f.write(resp.content)
        return resp
if __name__ == "__main__":
    # gaode=gaode(key='a3a3ded5a6ace0345eb4b272665fd898')
    # print(gaode.tianqi(city='440106').text)
    # print(gaode.dingwei().text)
    # gaode.static_map()
    pass
