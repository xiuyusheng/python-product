import requests


class BMC(object):
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

        self.headers = {
            "content-type": "application/json"
        }
        self.session = requests.session()

        # 认证
        self.session.auth(self.username, self.password)

    def start_up(self, data):
        # 开机
        url = f'https://{self.host}/redfish/v1/Systems/1/Actions/ComputerSystem.Reset'
        response = self.session.post(url=url, verify=False, json=data, headers=self.headers)
        print(f"返回信息：{response}")

    def shut_down(self, data):
        # 关机
        url = f'https://{self.host}/redfish/v1/Systems/1/Actions/ComputerSystem.Reset'
        response = self.session.post(url=url, verify=False, json=data, headers=self.headers)
        print(f"返回信息：{response}")

    def graceful_restart(self, data):
        # 优雅重启
        url = f'https://{self.host}/redfish/v1/Systems/1/Actions/ComputerSystem.Reset'
        response = self.session.post(url=url, verify=False, json=data, headers=self.headers)
        print(f"返回信息：{response}")

    def force_restart(self, data):
        # 强制重启：相当于reboot，拔掉电源
        url = f'https://{self.host}/redfish/v1/Systems/1/Actions/ComputerSystem.Reset'
        response = self.session.post(url=url, verify=False, json=data, headers=self.headers)
        print(f"返回信息：{response}")


if __name__ == '__main__':
    host = "111.112.113.114"  # BMC地址
    username = "admin"
    password = "1234567890"
    bmc = BMC(host, username, password)
    bmc.start_up({"ResetType": "ForceOn"})
    bmc.shut_down({"ResetType": "ForceOff"})
    bmc.graceful_restart({"ResetType": "GracefulRestart"})
    bmc.force_restart({"ResetType": "ForceRestart"})