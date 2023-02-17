import pywinauto
import time
import pyautogui
from pyperclip import copy,paste
# #启动exe
# path = r'D:\Program Files (x86)\Tencent\QQLive\QQLive.exe'
# app = pywinauto.Application().start(path)

# time.sleep(2)
# a=pyautogui.locateOnScreen(r'img\log.png')
# print(a)
# if a==None:
#     pyautogui.hotkey('alt', 'tab')

# # time.sleep(1)

# # a = pyautogui.locateOnScreen(r'img\log.png')

# pyautogui.click(x=949, y=165, button='left')

# pyautogui.hotkey('ctrl', 'a')

# pyautogui.press('backspace')

# pyautogui.typewrite('yirenzhixia',interval=0.25)

# pyautogui.press('enter')
# pyautogui.press('enter')

# time.sleep(3)
b = pyautogui.locateOnScreen(r'img\vip.png')


print(b)

pyautogui.click(b[0], b[1]+b[3], button='left')




