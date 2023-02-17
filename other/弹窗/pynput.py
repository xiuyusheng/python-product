# 获取鼠标位置

from pynput.mouse import Controller,Button
mouse=Controller()
mouseposition = mouse.position
print("鼠标当前的位置是：{0}".format(mouseposition))
