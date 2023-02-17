import requests
import execjs#node操作js执行解码程序
import time
import ddddocr#验证码识别库
ocr = ddddocr.DdddOcr()


ctx = execjs.compile('''var CryptoJS=require('crypto-js')

function login(verifyCode,time_t,userid,userpassword){
  const initKey = "xie2gg";
  const keySize = 128;
  /*
   * 生成密钥字节数组, 原始密钥字符串不足128位, 补填0.
   * @param {string} key - 原始 key 值
   * @return Buffer
   */
  const fillKey = (key) => {
    const filledKey = Buffer.alloc(keySize / 8);
    const keys = Buffer.from(key);
    if (keys.length < filledKey.length) {
      filledKey.forEach((b, i) => {
        filledKey[i] = keys[i];
      });
    }
  
    return filledKey;
  };
  const key = CryptoJS.enc.Utf8.parse(fillKey(initKey));
  console.log(key)
  const aesEncrypt = (data, key) => {
      /**
       * CipherOption, 加密的一些选项:
       *   mode: 加密模式, 可取值(CBC, CFB, CTR, CTRGladman, OFB, ECB), 都在 CryptoJS.mode 对象下
       *   padding: 填充方式, 可取值(Pkcs7, AnsiX923, Iso10126, Iso97971, ZeroPadding, NoPadding), 都在 CryptoJS.pad 对象下
       *   iv: 偏移量, mode === ECB 时, 不需要 iv
       * 返回的是一个加密对象
       */
      const cipher = CryptoJS.AES.encrypt(data, key, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7,
        iv: ''
      });
       // 将加密后的数据转换成 Base64
       const base64Cipher = cipher.ciphertext.toString(CryptoJS.enc.Base64);
      // console.log(base64Cipher)
       // 处理 Android 某些低版的BUG
       const resultCipher = base64Cipher.replace(/\+/g, '-').replace(/\//g, '_');
  
       // 返回加密后的经过处理的 Base64
       return resultCipher;
  //z9zoEo5XJT0lLsQVCeeAZtMlpjf6Z8VP8evDnU2ejYeCm1t5NI1GyLJm3DFZqMgnugyf2mRaZFnTbfiEPJog3ukYeQBI-_ecgRDaPbxBoj0q8v6VZ1lio1TW_F21OCBkrlPOkC2BXrT-4uk0j15dtKJ5e5dMbFLj46sqLRTQAmo=
  //z9zoEo5XJT0lLsQVCeeAZtMlpjf6Z8VP8evDnU2ejYeCm1t5NI1GyLJm3DFZqMgnugyf2mRaZFnTbfiEPJog3ukYeQBI-_ecgRDaPbxBoj1aNNm6J-q-YUiYBssB9c4QrlPOkC2BXrT-4uk0j15dtKJ5e5dMbFLj46sqLRTQAmo=
       
     };
  const encrypted = aesEncrypt(JSON.stringify({
        keyNumber: userid,
        password: userpassword,
        tenantCode: '4144013930', 
        time: time_t, 
        verifyCode: verifyCode
      }), key);
      return encrypted 
}

  ''')#编译js代码





loginURL = f'https://weiban.mycourse.cn/pharos/login/login.do?timestamp={int(time.time())}'  # 登录请求 URL

# 登录请求
def login(verifyCode,userid,userpassword,yzm_time):
    # print(verifyCode,userid,userpassword,yzm_time)
    result = ctx.call('login', verifyCode,yzm_time,userid,userpassword)#通过js加密数据
    # print(result)
    param = {
        'data':result
    }
    resp=requests.post(url=loginURL, data=param).json()#发出登录请求
    return resp
# get_yzm()

def stat(UserId,UserPassword):
    yzm_time=int(time.time()*1000)#获取验证码时间
# def get_yzm():
    yzm_url=f'https://weiban.mycourse.cn/pharos/login/randLetterImage.do?time={yzm_time}'
    yzm_resp=requests.get(url=yzm_url)
    userid=UserId
    yzm_= ocr.classification(yzm_resp.content)
    # yzm_=chaojiying.yzm(yzm_resp.content)['pic_str']#验证码
    userpassword=UserPassword
    if(userpassword==''):#密码为空则直接默认账号为密码
        userpassword=userid
    json1=login(yzm_,userid,userpassword,yzm_time)#登录执行
    return json1