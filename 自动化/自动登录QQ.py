import pywinauto
import time
import pyautogui
from pyperclip import copy,paste
#启动exe
# path = r'D:\Program Files (x86)\Tencent\QQ\Bin\QQScLauncher.exe'
# app = pywinauto.Application().start(path)

#打开搜索
pyautogui.hotkey('win', 's')
copy('腾讯QQ')
pyautogui.hotkey('ctrl', 'v')

pyautogui.press('enter')

time.sleep(3)
a = pyautogui.locateOnScreen(r'img\user.png')
print(a)
pyautogui.click(a[0], a[1], button='left')
pyautogui.typewrite('3044639452',interval=0.25)
pyautogui.press('tab')
pyautogui.typewrite('20030216abcde',interval=0.25)
pyautogui.press('enter')
print(a[0])