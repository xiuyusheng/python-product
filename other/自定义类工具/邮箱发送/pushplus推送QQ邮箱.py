import smtplib#用于创建客户端会话对象实例
from email.message import EmailMessage#用于创建文件邮件对象和发送邮件
import win32ui#用于打开文件对话框
import os#用于根据选择路径读取文件
import mimetypes#用解析文件类型


class EmailClass():
    def __init__(self) -> None:
        self.port = 587  # 邮箱端口号
        self.host = 'smtp.qq.com'  # 邮箱接口
        self.MyEmail = '3044639452@qq.com'  # 我的邮箱
        self.MyPassword = 'jmeporprsdeldghe'  # 邮箱smpt协议生成密码
        self.Message = EmailMessage()  # 生成数据对象
        self.smtp = smtplib.SMTP(self.host, self.port)

    def send_(self, ToEmail, subject, content, isattach=False):
        self.Message['from'] = '3044639452@qq.com'  # 发送源（同于我的邮箱地址）
        self.Message['to'] = ToEmail  # 发送目标邮箱地址
        self.Message['subject'] = subject  # 邮箱主题
        self.Message.set_content(content)  # 邮箱的信息
        if isattach:
            self.add_attachment()
        self.send_msg()

    def add_attachment(self):
        dlg = win32ui.CreateFileDialog(1)           # 参数 1 表示打开文件对话框
        dlg.SetOFNInitialDir('C://')                # 设置打开文件对话框中的初始显示目录
        dlg.DoModal()  # 打开文件选择器
        path = dlg.GetPathName()  # 选择文件（文件夹）路径
        if path != '':
            ctype, encoding = mimetypes.guess_type(path)  # 解析为文件类型
            if ctype is None:  # 类型为空时补充为其他类型
                ctype = "application/octet-stream"
            maintype, subtype = ctype.split("/")  # 导出文件类型和发送类型
            with open(path, "rb") as r:
                self.Message.add_attachment(
                    r.read(), maintype=maintype, subtype=subtype, filename=os.path.basename(path))

    def send_msg(self):
        with self.smtp:
            try:
                self.smtp.login(self.MyEmail, self.MyPassword)  # 登陆QQ邮箱
            except smtplib.SMTPAuthenticationError as e:  # 邮箱错误对象
                print("登录失败:%s", e.args)
            else:
                print('开始发送')
                self.smtp.send_message(self.Message)  # 发送邮箱
                print("发送成功")


if __name__ == "__main__":
    Email = EmailClass()
    Email.send_('3394954185@qq.com', '测试', '123', True)
