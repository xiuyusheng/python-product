import os
from scapy.all import *



# def get_pcap(ifs,ip=None,size=100):
#     ''' 获取指定 ifs(网卡), 指定数量size 的数据包;如果有指定ip，则这里只接收tcp，80端口，指定ip的包 '''
#     filter = ""
#     if ip:
#         filter += "ip src %s and tcp"%ip
#         dpkt = sniff(iface=ifs,filter=filter,count=size)
#     else:
#         dpkt = sniff(iface=ifs,count=size)
#     # wrpcap("pc1.pcap",dpkt) # 保存数据包到文件
#     wrpcap("demo.pcap", dpkt)
#     return dpkt

# def get_ip_pcap(ifs,sender,size=100):
#     ''' 获取指定 ifs(网卡), 指定发送方 sender(域名或ip) 的数据包
#         size：(一次获取数据包的数量） '''
#     if 'www.' in sender:
#         v = os.popen('ping %s'%sender).read()
#         ip = v.split()[8]
#         print("准备接收IP为 %s 的数据包..."%ip)
#     else:
#         ip = sender
#         print("准备接收IP为 %s 的数据包..."%ip)
#     count = 0  
#     with open('e.txt','w',encoding='utf-8') as f:
#         while count<10:
#             d = get_pcap(ifs,ip=ip,size=size)
#             for i in d:
                
#                 try:
#                     # if i[IP].src==ip: # 发送方的IP为：ip  接收方的IP：i[IP].dst==ip
#                     print(i)
#                     f.write(i[Raw].load)
#                 except:
#                     pass
#             count+=1



def main():
    ifs = 'MediaTek Wi-Fi 6 MT7921 Wireless LAN Card' # 网卡
    ip = "vd.l.qq.com"  # ip地址，也可写域名，如：www.baidu.com
    # get_ip_pcap(ifs,ip,size=10)  # 一次接收一个包
    dpkt = sniff(iface=ifs,count=20,filter="ip src %s and tcp"%ip)
    for i in dpkt:
        try:
            print(i[Raw].load.decode())
            # with open('1.txt','w+') as f:
            #     f.write(i[Raw].load.decode())
        except:
            pass


if __name__ =='__main__':
    main()
