import time
import zipfile
import itertools


def extract(password, file):
    try:
        password = str(password)
        file.encoding='utf-8'
        file.extractall(path='.', pwd=password.encode('utf-8'))
        print("the password is {}".format(password))
        return True
    except Exception as e:
        pass

def main(password_length):
    zip_file = zipfile.ZipFile(r"a.zip", 'r')
    # 开始尝试
    data = "0123456789"
    num = 0
    for i in itertools.product(data, repeat=password_length):
        guess = "".join(i)
        # print(f"当前密码长度：{password_length}, 猜测的密码为：{guess}，尝试次数：{num}。")
        if extract(guess, zip_file):
            print(f"当前密码长度：{password_length}, 猜测的密码为：{guess}。实际密码为：{guess}，尝试次数：{num}，破解成功。")
            break
        num += 1


if __name__ == '__main__':
    start = time.time()
    main(6)
    end = time.time()
    print(f"破解耗时：{round(end - start, 2)}秒")