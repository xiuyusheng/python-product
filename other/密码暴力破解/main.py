"""
?破解的思路：

?1、获取目标密码长度，一般为4,6,12,15,18位长度。

?2、获取目标密码组成的范围，一般为数字，小写字母，大写字母，特殊符号

?3、组装密码，通过itertools模块组装。Python：常见排列组合问题处理

?4、枚举破译。
"""
import random
import itertools
import time


def test_bank_card_password(password_length=6):
    data = "0123456789"#设置密码中存在的字符，此处用的是纯密码
    bank_card_password = '20030216'#random.randint 返回指定范围内的整数，最大为数为每位数都为9
    if len(bank_card_password) < password_length:#当测试密码长度小于正确密码长度时，在最高位前面补零
        bank_card_password = "0" * (password_length - len(bank_card_password)) + bank_card_password

    print(f"银行卡密码为：{bank_card_password}")

    num = 0
    for i in itertools.product(data, repeat=password_length):#itertools.product() 方法,参数1：密码所存在的字符；参数2：密码长度-->返回元组可迭代对象
        guess = "".join(i)#拼接元组元素
        if bank_card_password == guess:
            print(f"当前密码长度：{password_length}, 猜测的密码为：{guess}。实际密码为：{bank_card_password}，尝试次数：{num}，破解成功。",end='\r')
            break
        else:
            print(f"当前密码长度：{password_length}, 猜测的密码为：{guess}。实际密码为：{bank_card_password}，尝试次数：{num}，破解成功。",end='\r')
        num += 1


if __name__ == '__main__':
    start = time.time()
    test_bank_card_password(8)#参数为正确密码长度
    end = time.time()
    print(f"破解耗时：{round(end - start, 2)}秒")