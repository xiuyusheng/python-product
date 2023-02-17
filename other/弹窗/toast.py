from win11toast import toast,notify, update_progress
import time
# toast('Hello', 'Hello from Python', duration='long',input='reply', audio={'src':'https://nyanpass.com/nyanpass.mp3','loop': 'true'})


#duration='long'弹窗时间延长
# audio='https://nyanpass.com/nyanpass.mp3'---->访问音频地址
# 'loop': 'true'---->循环播放
# 'silent': 'true'---->静音
# dialogue='你好'---->语音播报
# ocr='https://i.imgur.com/oYojrJW.png'---->图像文字识别
# input='reply'---->输入框

# toast('Hello', 'Type anything', input='reply', button={'activationType': 'protocol', 'arguments': 'http:', 'content': 'Send', 'hint-inputId': 'reply'})


# toast('Hello', 'Hello from Python', button={'activationType': 'protocol', 'arguments': 'https://google.com', 'content': '打开谷歌'})#按钮点击事件

# buttons = [
#     {'activationType': 'protocol', 'arguments': 'C:\Windows\Media\Alarm01.wav', 'content': 'Play'},
#     {'activationType': 'protocol', 'arguments': 'file:///C:/Windows/Media', 'content': 'Open Folder'}#多按钮弹窗
# ]
# toast('Music Player', 'Download Finished', buttons=buttons)

# icon = {
#     'src': 'https://unsplash.it/64?image=669',
#     'placement': 'appLogoOverride'
# }
# image = {
#     'src': 'https://unsplash.it/64?image=669',
#     'placement': 'hero'
# }
# toast('你好',icon=icon,image=image)#icon通知图标，image通知内容的大图

# toast('Hello', 'Which do you like?', selection=['Apple', 'Banana', 'Grape'], button='Submit')
# {'arguments': 'dismiss', 'user_input': {'selection': 'Grape'}}
#---------------------------------------------------------进度条------------------------------------------------------------
notify(progress={
    'title': 'YouTube',
    'status': 'Downloading...',
    'value': '0',
    'valueStringOverride': '0/15 videos'
})

for i in range(1, 15+1):
    time.sleep(1)
    update_progress({'value': i/15, 'valueStringOverride': f'{i}/15 videos'})

update_progress({'status': 'Completed!'})


