import requests


class Push_plus():
    def __init__(self, token) -> None:
        self.token = token

    def Push(self,title='新消息',content='空',topic='',template='html',channel='wechat',webhook='',callbackUrl='',timestamp='',to=''):
        url = 'http://www.pushplus.plus/send'
        params = {
            # 用户令牌，可直接加到请求地址后，如：http://www.pushplus.plus/send/{token}
            'token': self.token,
            'title': title,  # 消息标题
            'content': content,  # 具体消息内容，根据不同template支持不同格式
            'topic': topic,  # 群组编码，不填仅发送给自己；channel为webhook时无效
            'template': template,  # 发送模板
            'channel': channel,  # 发送渠道
            'webhook': webhook,  # webhook编码
            'callbackUrl': callbackUrl,  # 发送结果回调地址
            'timestamp': timestamp,  # 毫秒时间戳。格式如：1632993318000。服务器时间戳大于此时间戳，则消息不会发送
            'to': to,  # 好友令牌，微信公众号渠道填写好友令牌，企业微信渠道填写企业微信用户id
        }
        params=dict((k,v) for k,v in params.items() if v!='')
        resp=requests.get(url=url,params=params)
        print(resp.text)
        return resp
    def help(self):
        print('''
\033[1;32;40m请求地址：\033[0m\033[4;37;40mhttp://www.pushplus.plus/send\033[0m  (直接调用Push()函数即可)

\033[1;32;40m请求方式：\033[0m\033[1;37;40mGET,POST,PUT,DELTE\033[0m

\033[1;32;40m请求参数，均支持url参数和body参数：\033[0m\033[1;37;40m\033[0mContent-Type: application/json

\033[1;34;40m参数\033[0m
|    token:用户令牌，可直接加到请求地址后，如：http://www.pushplus.plus/send/{token}
|    title:消息标题
|    content:消息内容
|    topic:群组编码，不填仅发送给自己；channel为webhook时无效
|    template:发送的模板
|    channel:发送渠道
|    webhook:webhook编码
|    callbackUrl:发送结果回调地址
|    timestamp:毫秒时间戳。格式如：1632993318000。服务器时间戳大于此时间戳，则消息不会发送
|    to:好友令牌，微信公众号渠道填写好友令牌，企业微信渠道填写企业微信用户id
------------------------------------------------------------------------------
\033[1;34;40m发送渠道（channel）枚举\033[0m
|    wechat:微信公众号
|    webhook:第三方webhook；HiFlow连接器、企业微信、钉钉、飞书、server酱、IFTTT；webhook机器人推送
|    cp:企业微信应用
|    mail:邮箱
|    sms(\033[1;31;40m收费\033[0m):短信
webhook参数说明。 
请到微信公众号菜单中预先进行webhook配置。当前字段需填写配置中的webHook编码。
------------------------------------------------------------------------------
\033[1;34;40m模板枚举（template默认html）\033[0m
|    html:html文本
|    txt:纯文本
|    json:内容基于Json格式展示
|    markdown:基于markdown格式展示
|    cloudMonitor:阿里云监控报警定制模板
|    jenkins:jenkins插件定制模板
|    route:路由器插件定制模板
|    pay:支付成功通知模板
------------------------------------------------------------------------------
\033[1;34;32m详情查看官方文档：http://www.pushplus.plus/doc/guide/api.html#%E4%B8%80%E3%80%81%E5%8F%91%E9%80%81%E6%B6%88%E6%81%AF%E6%8E%A5%E5%8F%A3\033[0m
                ''')
if __name__=="__main__":
    Push_plus=Push_plus('962e5cfffa8e4d0a9a6036f5fbabebce')
    # print(Push_plus.Push(title='支付模块测试',content='<img src=\'https://n.sinaimg.cn/sinakd10114/164/w603h361/20200717/0ddb-iwpcxkr6257804.jpg\'>',template='html').request.url)
    Push_plus.help()
