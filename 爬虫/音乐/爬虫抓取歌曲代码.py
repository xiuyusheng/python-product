import tkinter as tk
import time
import requests
import urllib.parse as parse
import json
import os
from pygame import mixer
from mutagen.mp3 import MP3  # 用来的到一个.mp3文件的时长

num=0
id_1=True

def Get_Time(time_list):
    for i in range(len(time_list)):
        minute = time_list[i][1:3]
        second = time_list[i][4:6]
        h_second = time_list[i][7:9]
        time_list[i] = int(minute) * 60 + int(second) + float('0.' + h_second)
    return time_list

def M_musci(music_name):
    keyword = parse.urlencode({'keyword': music_name})
    keyword = keyword[keyword.find('=') + 1:]
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'}
    url = 'https://songsearch.kugou.com/song_search_v2?callback=jQuery1124042761514747027074_1580194546707&keyword=' + keyword + '&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1580194546709'
    json_1=requests.get(url=url,headers=headers).text
    json_1=json_1[json_1.find('(')+1:-2]

    json_1=json.loads(json_1)
    str_1=json_1['data']['lists']

    try:
        os.mkdir('./某某音乐')

    except:
        pass

    finally:
        for i in range(len(str_1)):
            str_hash=str_1[i]['FileHash'] # 歌曲hash
            str_id=str_1[i]['AlbumID']   # 歌曲id
            str_2 = str_1[i]['FileName']
            str_2=str_2.replace('<em>','')
            str_2=str_2.replace('</em>','') # 歌曲名称

            with open('./某某音乐/index.txt','a',encoding='utf-8') as f:
                f.write(str_2+'\t'+str_hash+'\t'+str_id+'\n')


def Information_from_file():
    with open('./某某音乐/index.txt','r',encoding='utf-8') as f:
        str_1=f.read()

    list_1=str_1.split('\n')[:-1]
    song_names=[];song_hash=[];song_id=[]
    for str_2 in list_1:
        str_2=str_2.split('\t')

        song_names.append(str_2[0])
        song_hash.append(str_2[1])
        song_id.append(str_2[2])

    return song_names,song_hash,song_id


def Downlad(music_hash,music_id):

    global num
    num+=1
    url = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash=' + music_hash \
          + '&album_id=' + music_id + '&dfid=2SSV0x4LWcsx0iylej1F6w7P&mid=44328d3dc4bfce21cf2b95cf9e76b968&platid=4'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'}
    content_1=requests.get(url=url,headers=headers)
    str_1=content_1.text
    if 'play_backup_url' in str_1:
        dict_song=json.loads(str_1)
        music_url = dict_song['data']['play_backup_url']
        song_content=dict_song['data']['lyrics']
        song_content=song_content[song_content.find('offset:'):]
        list_1=song_content[song_content.find(']')+3:]
        list_1=list_1.split('\r\n')[:-1]
        song_list=[];time_list=[]
        for str_1 in list_1:
            #歌曲时间
            str_2=str_1[:str_1.find(']')+1]
            time_list.append(str_2)

            str_1=str_1[str_1.find(']')+1:]
            song_list.append(str_1)
            # 歌词列表


        time_list=Get_Time(time_list)

        # print(music_url)
        content_song=requests.get(url=music_url,headers=headers)
        with open('./某某音乐/index{}.mp3'.format(num),'wb') as f:
            f.write(content_song.content)


        audio = MP3('./某某音乐/index{}.mp3'.format(num))
        time_music= audio.info.length
        # 播放音乐代码
        mixer.init()
        mixer.music.load('./某某音乐/index{}.mp3'.format(num))
        mixer.music.play()
        mixer.stop()

        return True,time_list,song_list,time_music

    else:

        return False,False,False,False


root=tk.Tk()
root.title('某某音乐')
root.geometry("800x400")
# 提醒用户输入
input_label=tk.Label(root,text='输入歌名：',font=('楷体',12))
input_label.grid(column=0)
# 输入框
v=tk.StringVar()
label_1=tk.Entry(root,textvariable=v,font=('隶书',12))
label_1.grid(row=0,column=1)
# 播放界面
label2=tk.Label(root,text='播放界面',font=('楷体',13))
label2.grid(row=0,column=2,padx=100)

#搜索框

list_box=tk.Listbox(root,font=('楷体',13),width=30)
list_box.grid(row=1,columnspan=2)

def select_1():
    M_musci(v.get())

    list_1=Information_from_file()[0]
    for i in range(len(list_1)):
        list_box.insert(tk.END,str(list_1[i]))

def select_4():  # 更新列表操作

    list_box.delete(0,tk.END)

    M_musci(v.get())

    list_1 = Information_from_file()[0]
    for i in range(len(list_1)):
        list_box.insert(tk.END, str(list_1[i]))



text_1=tk.Text(root,height=12,width=64,font=('楷体',12,'bold'),bg='black',fg='white')
text_1.grid(row=1,column=2,padx=5)

def select_2():

    dict_id={}
    dict_hash={}
    list_1=Information_from_file()[0] # 歌曲名
    list_2=Information_from_file()[1]  # hash
    list_3=Information_from_file()[2]  # id
    for i in range(len(list_1)):
        dict_id[list_1[i]]=list_2[i]
        dict_hash[list_1[i]]=list_3[i]

    name_1 = list_box.get(tk.ACTIVE)
    id1=dict_id[name_1]
    hash1=dict_hash[name_1]
    bool_1=Downlad(id1,hash1)
    # os.remove(path='./某某音乐/index.txt')

    # 显示一个进度条
    for i in range(1, 101):
        tk.Label(root, text='{}%|{}'.format(i, int(i / 4 % 26) * '■')).grid(row=3, columnspan=2, sticky=tk.W)
        root.update()


    if bool_1[0]:

        time_list=bool_1[1]
        song_list=bool_1[2]
        music_time=bool_1[3]
        # 加载完毕提示
        tk.Label(root, text='加载完毕，开始播放！', font=('楷体', 14)).grid(row=4, columnspan=2, sticky=tk.W)

        i = 0
        T = 0


        while True:
            try:

                text_1.insert('{}.0'.format(i + 1), (song_list[i] + '\n').center(36, ' '))

                i += 1

                if len(song_list[:i]) == 12:
                    song_list = song_list[1:]
                    text_1.delete('1.0', tk.END)
                    i = 11
                    if len(song_list) <= 12:
                        pass
                    else:
                        try:
                            for j in range(12):
                                text_1.insert('{}.0'.format(j + 1), (song_list[j] + '\n').center(36, ' '))
                        except:
                            pass

                if T == 0:
                    time.sleep(time_list[T])
                elif T == len(time_list) - 1:
                    time.sleep(5)
                else:
                    time.sleep(time_list[T + 1] - time_list[T])

                T += 1

                root.update()

            except:
                break

        if '纯音乐' not in song_list[0]:
            tk.Label(root,text='播放完毕！',font=('楷体',14),bg='black',fg='white')\
                .grid(row=2,column=2)
            time.sleep(15)

        else:

            time.sleep(music_time)

            tk.Label(root, text='纯音乐播放完毕！', font=('楷体', 14),bg='red',fg='green') \
                .grid(row=2, column=2)

    else:

        tk.Label(root, text='对不起，亲，出错啦，你没有该歌曲的版权！', font=('楷体', 14)).grid(row=4, columnspan=2, sticky=tk.W)


####### 搜索按钮

tk.Button(root,text='搜索',font=('楷体',14),command=select_1).grid(row=2,column=0,sticky=tk.W)
tk.Button(root,text='播放',font=('楷体',14),command=select_2).grid(row=2,column=1,sticky=tk.E)

def remove_txt():
    try:
        os.remove(path='./某某音乐/index.txt')

    except:
        pass

tk.Button(root,text='重新搜索',font=("方正楷体",14),command=remove_txt)\
    .grid(row=5,column=0,sticky=tk.W)

tk.Button(root,text='更新列表',font=('隶书',14),command=select_4)\
    .grid(row=5,column=1,sticky=tk.E)

####### 退出程序按钮
tk.Button(root,text='退出小程序！',font=('方正楷体',14),command=root.quit).grid(row=6,columnspan=2)

text_2=tk.Text(root,font=('宋体',10,'bold'),fg='red',width=64,height=5)

text_2.grid(row=3,column=2)

text_2.insert(tk.END,'''声明：\n
    1.本小程序仅供学习和娱乐,切莫用于商业用途,一经发现,概不负责！\n
    2.运行本小程序,开启比较慢，属于正常现象\n''')

try:
    os.remove(path='./某某音乐/index.txt')

except:

    pass

tk.mainloop()
