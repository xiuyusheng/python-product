from Crypto import Random
from Crypto.PublicKey import RSA


import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher  
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5

# random_generator = Random.new().read  # 生成随机偏移量
# print(random_generator)
# rsa = RSA.generate(1024, random_generator)  # 生成一个私钥
# print(rsa)
# 生成私钥
# private_key = rsa.exportKey()  # 导出私钥
# print(private_key.decode())  
# 生成公钥
# public_key = rsa.publickey().exportKey()  # 生成私钥所对应的公钥
# print(public_key.decode())




# def get_key(key_file):
#     with open(key_file) as f:
#         data = f.read()  # 获取，密钥信息
#         key = RSA.importKey(data)
#         # print(data)
#     return key


def encrypt_data(msg,public_key):
    # print(public_key)
    public_key = RSA.importKey(public_key)  # 读取公钥信息
    # print(public_key)
    cipher = Cipher_pkcs1_v1_5.new(public_key)  # 生成一个加密的类
    encrypt_text = base64.b64encode(cipher.encrypt(msg.encode('utf-8')))  # 对数据进行加密
    return encrypt_text.decode('utf-8')  # 对文本进行解码码


# def decrypt_data(encrypt_msg,private_key):
#     private_key = RSA.importKey(private_key) # 读取私钥信息
#     # print(private_key)
#     cipher = PKCS1_cipher.new(private_key)  # 生成一个解密的类
#     back_text = cipher.decrypt(base64.b64decode(encrypt_msg), 0)  # 进行解密
#     return back_text.decode()  # 对文本内容进行解码


def stay(password,public_key):
    encrypt_text = encrypt_data(password,public_key)  # 加密

    # decrypt_text = decrypt_data(encrypt_text,private_key)  # 解密
    # print(encrypt_text)
    return encrypt_text


stay('20030216abc','''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDwuEQ7SAZxGgJ/Kvzlvvqs3KCO
G1eRdWcOwESDtckqZf1kq7pkuy7TodEOknVPI64HnH5x1vEUvBFuAQtOPVfGxytk
dr7GSFhw4m33ke2sPWFPCFWSwDVDdt06IdJqEM2Wh0e5SlAr+eLJbxQHy5aZId5A
jxVF831WZ+bGuHcikQIDAQAB
-----END PUBLIC KEY-----
'''.encode())
# xr6orFMm6KxyKZSjw36bOEtE86bWOi0fsxOstlFYFG4KUvwlJc7ODx2AQR8vIyppZOpuHIKYNmhV3+IYmlVpBZ1O3vn7EHN7pJCgYbpGyT8q+OgyKHjKf7+EnkhyNkHbnBNZIMWmLMTL/QJNDASH14l/dGSFzKKkFNlPtKspNLM=
# A5S+kuTJTaGJvw6oxHlhT0NrCgnJkJ34D7yET7LCjjSA9qyF73T8tg5uBFlZT0Qc2GcJkOlain94SXnuWwKbP2C/YgeIplWhOqVwBgi/vtamuLJRmk2+bqOILeD5mjAzfIQJ/682Jx9aH5wOLG64owlcqQRxNuPUAWQX4xHCd5M=
# print(decrypt_text, encrypt_text,sep='\n')
