import base64
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pksc1_v1_5
from Crypto.PublicKey import RSA

def encrpt(password, public_key):
    rsakey = RSA.importKey(public_key)
    cipher = Cipher_pksc1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(password.encode()))
    return cipher_text.decode()

# key是公钥，需要修改成自己的之后再进行加密
# key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDIrn+WB2Yi4ABAL5Tq6E09tumYqVTFdpU01kCDUmClczJOCGZriLNMrshmN9NJxazpqizPthwS1OIK3HwRLEP9D3GL7gCnvN6lpIpoVwppWd65f/rK2ewv6dstN0fCmtVj4WsLUchWlgNuVTfWljiBK/DcYkfslRZzCq5Fl3ooowIDAQAB'
# public_key = '-----BEGIN PUBLIC KEY-----\n' + key + '\n-----END PUBLIC KEY-----'
# password = encrpt('fKSMrw==$gitee$123', public_key)
# print('password:', password)