import m3u8#?m3u8解析
import requests
from urllib.parse import urlparse,urljoin#?url解析重组
from tkinter import *#?图形化界面
from tkinter.simpledialog import *#?警示框包
import os#?本次用于创建文件夹
from threading import Thread#?多线程，防止程序后台执行导致页面无响应
import colorama#?print()彩色文字输出
colorama.init(autoreset=True)#?打包exe后仍然可以彩色文字输出

if __name__=="__main__":
    def start_A():
        try:#?排除错误url
            a=urlparse(url.get())#?解析url
            print(f'\033[1;34;40m解析m3u8\033[0m')
            with open('./.m3u8','r') as f:

                play_list = m3u8.load(f.read())#?解析m3u8文件
        except :
            print('\033[1;31;40murl错误\033[0m')
            return
        with open('mp4/'+filename.get()+'.mp4','wb') as f:#?写入视频
            len_=len(play_list.segments)#?m3u8文件解析后的长度
            for index,segment in enumerate(play_list.segments):#?枚举m3u8列表
                ur = segment.uri#?读取单元的url值
                tsurl= urljoin(str(a[0])+'://'+''.join(a[1:3]),ur)#?拼接新的url
                print(f'download......    第\033[1;34;40m{index}\033[0m节,共\033[1;34;40m{len_}\033[0m节,进度\033[1;31;40m{int(index/len_*100)}%\033[0m',end='\r')
                try:
                    ts=requests.get(tsurl)#?防止服务器端主动断开连接而报错
                except:
                    start.configure(text='下载失败',bg='red',fg='#00000')#?修改按钮属性
                    print('\033[1;31;40m【下载失败】\033[0m')
                    return
                f.write(ts.content)#?写入文件
                start.configure(text=f'正在下载...({int(index/len_*100)}%)',fg='red',bg='#fc8289')
        print(f'download......    第\033[1;34;40m{len_}\033[0m节,进度\033[1;31;40m100%\033[0m',end='\n')
        print('\033[1;36;40m【下载完成】\033[0m')
        start.configure(text='下载完成',bg='#a5e88d',fg='#356848')
    def files_():
        if  url.get()!='':#?判断是否为空
            if not os.path.exists('mp4'):#?判断是否存在mp4文件夹，没有则创建
                os.makedirs('mp4')
            Thread(target=start_A).start()#?分线程执行下载函数
    root =Tk()#?创建图形化界面
    root.title('m3u8解析器')#?标题
    root.geometry('400x200')#?大小，长*宽，乘号用小写x代替
    Label(root,text='url:',font=('华文新魏',12),relief=GROOVE,width=5).place(relx=0.1,y=13,relwidth=0.2)#?标签
    url=Entry(root,width=30)#?输入框
    url.place(relx=0.31,y=10,relheight=0.1,relwidth=0.5)
    Label(root,text='filename:',font=('华文新魏',12),relief=GROOVE,width=5).place(relx=0.1,rely=0.2,relwidth=0.2)
    filename=Entry(root,width=30)
    filename.place(relx=0.31,rely=0.2,relheight=0.1,relwidth=0.5)
    start=Button(root,text='开始下载',bg='#fc8289',fg='red',font=('华文新魏',12),width=7,height=2,command=files_)#?按钮
    start.place(relx=0.25,rely=0.4,relwidth=0.5)
    print('\033[1;36;44m准备就绪,准备解析\033[0m')
    root.mainloop()#?启动页面