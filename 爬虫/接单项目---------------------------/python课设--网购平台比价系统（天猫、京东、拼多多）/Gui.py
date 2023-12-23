# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from GoodsList import GoodsList
from Goods import Goods
from DBConnection import DBConnection
# import users_data
# import UserS


class GUI:
    def __init__(self, ):
        # self.data = user_data
        # 用于存放商品信息
        self.goodsinfo = []
        # 主窗口
        self.window = tk.Tk()
        # 框架划分
        self.frm_t = tk.Frame(self.window, width=1000, height=300).pack()
        self.frm_b = tk.Frame(self.window, width=1000, height=600).pack()
        self.frm_d = tk.Frame(self.window, width=1000, height=100).pack()
        # 平台选择
        self.tm_var = tk.IntVar()
        self.jd_var = tk.IntVar()
        self.pdd_var = tk.IntVar()
        self.c1 = tk.Checkbutton(
            self.frm_t, text="国美", variable=self.tm_var, onvalue=1, offvalue=0
        )
        self.c2 = tk.Checkbutton(
            self.frm_t, text="京东", variable=self.jd_var, onvalue=1, offvalue=0
        )
        self.c3 = tk.Checkbutton(
            self.frm_t, text="拼多多", variable=self.pdd_var, onvalue=1, offvalue=0
        )
        # 获取爬取商品数量
        self.dp_var = tk.IntVar()
        self.dp_en = tk.Entry(self.frm_t, textvariable=self.dp_var, width=3)
        # 获取搜索关键词
        self.goods_var = tk.StringVar()
        self.goods_en = tk.Entry(self.frm_t, textvariable=self.goods_var, width=10)
        # 排序方式
        self.sort_var = tk.IntVar()
        self.ch1 = tk.Radiobutton(
            self.frm_b, text="默认排序", variable=self.sort_var, value=1
        )
        self.ch2 = tk.Radiobutton(
            self.frm_b, text="价格升序", variable=self.sort_var, value=2
        )
        self.ch3 = tk.Radiobutton(
            self.frm_b, text="价格倒序", variable=self.sort_var, value=3
        )
        # 获取序号
        self.num_var = tk.StringVar()
        self.num_en = tk.Entry(self.frm_t, textvariable=self.num_var, width=50)
        # 表格
        self.tree = ttk.Treeview(
            self.frm_d,
            columns=["1", "2", "3", "4", "5", "6", "7", "8"],
            show="headings",
            height=25,
        )
        # 表格滚动条
        self.VScroll1 = ttk.Scrollbar(
            self.tree, orient="vertical", command=self.tree.yview
        )
        # 这个按钮后面在函数中需要变动，所以设为全局变量
        self.comfirm3 = tk.Button(self.frm_t, text="加入关注", width=20)
        # self.user_data = users_data.users()

    # 获取信息
    def getInfo(self):
        self.comfirm3.config(text="加入关注", command=self.addtoDB)
        self.goodsinfo.clear()
        tm = self.tm_var.get()
        jd = self.jd_var.get()
        pdd = self.pdd_var.get()
        number = self.dp_var.get()
        keyword = self.goods_var.get()
        if not tm and not jd and not pdd:
            tk.messagebox.showinfo(title="提示", message="您未选取任何平台")
            return
        check_numls = []
        for i in range(60):
            check_numls.append(i + 1)
        if number not in check_numls:
            tk.messagebox.showinfo(title="提示", message="请输入正确的爬取数量（1--60）")
            return
        if keyword == "":
            tk.messagebox.showinfo(title="提示", message="请输入关键词")
            return
        goodslist = GoodsList(keyword, number, tmall=tm, jd=jd, pdd=pdd)
        goodslist.getGoods()
        if self.sort_var.get() == 1:
            self.goodsinfo.extend(goodslist.getGoodsList())
        elif self.sort_var.get() == 2:
            self.goodsinfo.extend(goodslist.sort())
        else:
            self.goodsinfo.extend(goodslist.sort(reverse=True))
        self.showdata()
        tk.messagebox.showinfo(title="提示", message="爬取完成")

    # 显示信息
    def showdata(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        if not self.goodsinfo:
            tk.messagebox.showinfo(title="提示", message="当前无商品信息")
            return
        else:
            num = 1
            for goods in self.goodsinfo:
                goodslist = [
                    num,
                    goods.getID(),
                    goods.getPlatform(),
                    goods.getTitle(),
                    goods.getShop(),
                    goods.getPrice(),
                    goods.getSales(),
                    goods.getHref(),
                ]
                self.tree.insert("", "end", values=goodslist)
                num = num + 1

    # 比价
    def compare(self):
        num_ls = self.num_var.get().split(" ")
        num_ls = list(set(num_ls))
        self.compare_ls = []
        for num in num_ls:
            if num == "":
                continue
            try:
                if not isinstance(eval(num), int):
                    tk.messagebox.showinfo(title="提示", message="请输入正确的序号")
                    return
                elif eval(num) > len(self.goodsinfo) or eval(num) < 1:
                    tk.messagebox.showinfo(title="提示", message="请输入正确的序号")
                    return
                else:
                    self.compare_ls.append(self.goodsinfo[eval(num) - 1])
            except:
                tk.messagebox.showinfo(title="提示", message="请输入正确的序号")
                return
        # 生成选择窗口
        self.choose = tk.Toplevel(self.window)
        self.choose.geometry("350x80")
        self.choose.title("比较选项")

        # 选择按钮
        tk.Button(self.choose, text="比较价格", command=self.price_BJ, width=10).place(
            x=50, y=30
        )
        tk.Button(self.choose, text="比较好评", command=self.GOOD_BJ, width=10).place(
            x=230, y=30
        )

        # tk.messagebox.showinfo(title="比价结果", message=result)

    def price_BJ(self):
        goodslist = GoodsList("", 0)
        goodslist.compare(self.compare_ls)

    def GOOD_BJ(self):
        goodslist = GoodsList("", 0)
        goodslist.compare2(self.compare_ls)

    # 加入关注列表
    def addtoDB(self):
        num_ls = self.num_var.get().split(" ")
        num_ls = list(set(num_ls))
        add_ls = []
        for num in num_ls:
            if num == "":
                continue
            try:
                if not isinstance(eval(num), int):
                    tk.messagebox.showinfo(title="提示", message="请输入正确的序号")
                    return
                elif eval(num) > len(self.goodsinfo) or eval(num) < 1:
                    tk.messagebox.showinfo(title="提示", message="请输入正确的序号")
                    return
                else:
                    add_ls.append(self.goodsinfo[eval(num) - 1])
            except:
                tk.messagebox.showinfo(title="提示", message="请输入正确的序号")
                return
        dbc = DBConnection()
        result = ""
        for item in add_ls:
            if dbc.save(item):
                result = result + '"' + item.getTitle() + '" 已成功加入关注列表\n'
            else:
                result = result + '"' + item.getTitle() + '" 已在关注列表中\n'
        tk.messagebox.showinfo(title="提示", message=result)

    # 显示关注列表
    def showDB(self):
        self.comfirm3.config(text="移除关注", command=self.delete)
        self.goodsinfo = []
        dbc = DBConnection()
        g_ls = dbc.getInfo()
        for item in g_ls:
            goods = Goods(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            self.goodsinfo.append(goods)
        for item in self.tree.get_children():
            self.tree.delete(item)
        if not self.goodsinfo:
            tk.messagebox.showinfo(title="提示", message="当前关注列表无商品")
            return
        else:
            num = 1
            for goods in self.goodsinfo:
                li = [
                    num,
                    goods.getID(),
                    goods.getPlatform(),
                    goods.getTitle(),
                    goods.getShop(),
                    goods.getPrice(),
                    goods.getSales(),
                    goods.getHref(),
                ]
                self.tree.insert("", "end", values=li)
                num = num + 1

    def JD(self):
        # ?解冻主窗口
        self.window.attributes("-disabled", 0)
        self.window_sign_up.destroy()

    # def updata_(self):
    #     # result = self.user_data.update(
    #     #     UserS.user_data(
    #     #         userid=self.data.getuserid(),
    #     #         passwd=self.userPassword.get(),
    #     #         name=self.username.get(),
    #     #         emails=self.useremails.get(),
    #     #         phone=self.userphone.get(),
    #     #     )
    #     # )
    #     if result:
    #         tk.messagebox.showinfo(title="提示", message="修改成功")

    #     else:
    #         tk.messagebox.showinfo(title="提示", message="修改失败")
    #     self.window_sign_up.destroy()
    #     self.window.attributes("-disabled", 0)

    # 个人中心
    # def personal(self):
    #     # ?冻结主窗口
    #     self.window.attributes("-disabled", 1)
    #     # ?子页面
    #     self.window_sign_up = tk.Toplevel(self.window)
    #     self.window_sign_up.geometry("350x380")
    #     self.window_sign_up.title("Personal center")

    #     self.userPassword = tk.StringVar()
    #     self.userPassword.set(self.data.getpasswd())
    #     self.username = tk.StringVar()
    #     self.username.set(self.data.getname())
    #     self.useremails = tk.StringVar()
    #     self.useremails.set(self.data.getemails())
    #     self.userphone = tk.StringVar()
    #     self.userphone.set(self.data.getphone())

        x, y = 60, 50
        X_L = 50
        tk.Label(self.window_sign_up, text="UserID:").place(x=x, y=y)
        tk.Label(self.window_sign_up, text="Password:").place(x=x, y=y + 50)
        tk.Label(self.window_sign_up, text="name:").place(x=x, y=y + 100)
        tk.Label(self.window_sign_up, text="emails:").place(x=x, y=y + 150)
        tk.Label(self.window_sign_up, text="phone:").place(x=x, y=y + 200)

        # tk.Label(self.window_sign_up, text=self.data.getuserid()).place(x=x + X_L, y=y)
        tk.Entry(self.window_sign_up, textvariable=self.userPassword).place(
            x=x + X_L, y=y + 50
        )
        tk.Entry(self.window_sign_up, textvariable=self.username).place(
            x=x + X_L, y=y + 100
        )
        tk.Entry(self.window_sign_up, textvariable=self.useremails).place(
            x=x + X_L, y=y + 150
        )
        tk.Entry(self.window_sign_up, textvariable=self.userphone).place(
            x=x + X_L, y=y + 200
        )

        tk.Button(
            self.window_sign_up,
            text="修改",
            command=self.updata_,
            width=20,
        ).place(x=x + X_L, y=y + 240)

        self.window_sign_up.protocol("WM_DELETE_WINDOW", self.JD)

    # 更新关注列表内容
    def updateDB(self):
        change_ls = []
        dbc = DBConnection()
        self.goodsinfo = []
        g_ls = dbc.getInfo()
        for item in g_ls:
            goods = Goods(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            self.goodsinfo.append(goods)
        for item in self.goodsinfo:
            change = item.update()
            if change != 0:
                change_ls.append([item.getTitle(), change])
        if change_ls:
            s = ""
            for item in change_ls:
                if item[1] > 0:
                    s = s + '"' + item[0] + '" 价格增加了 ' + str(item[1]) + " 元\n"
                else:
                    s = s + '"' + item[0] + '" 价格降低了 ' + str(abs(item[1])) + " 元\n"
        else:
            s = "关注列表中所有商品价格均无变动"
        tk.messagebox.showinfo(title="提示", message=s)

    # 从关注列表删除
    def delete(self):
        num_ls = self.num_var.get().split(" ")
        num_ls = list(set(num_ls))
        delete_ls = []
        for num in num_ls:
            if num == "":
                continue
            try:
                if not isinstance(eval(num), int):
                    tk.messagebox.showinfo(title="提示", message="请输入正确的序号")
                    return
                elif eval(num) > len(self.goodsinfo) or eval(num) < 1:
                    tk.messagebox.showinfo(title="提示", message="请输入正确的序号")
                    return
                else:
                    delete_ls.append(self.goodsinfo[eval(num) - 1])
            except:
                tk.messagebox.showinfo(title="提示", message="请输入正确的序号")
                return
        dbc = DBConnection()
        for item in delete_ls:
            dbc.delete(item)
        tk.messagebox.showinfo(title="提示", message="删除成功")

    # 主窗口
    def mainwindow(self):
        self.window.title("网上商城比价系统")
        self.window.geometry("1150x700")

        # 网站选择
        tk.Label(self.frm_t, text="平台选择:").place(x=30, y=30)
        self.c1.place(x=100, y=28)
        self.tm_var.set(True)
        self.c2.place(x=170, y=28)
        self.jd_var.set(True)
        self.c3.place(x=240, y=28)
        self.pdd_var.set(True)

        # 商品数选择
        tk.Label(self.frm_t, text="每个平台爬取数量:").place(x=330, y=30)
        self.dp_en.place(x=445, y=30)
        self.dp_var.set(1)

        # 商品选择
        tk.Label(self.frm_t, text="关键词:").place(x=500, y=30)
        self.goods_en.place(x=555, y=30)

        # 排序
        tk.Label(self.frm_b, text="排序方式：").place(x=655, y=30)
        self.sort_var.set(1)
        self.ch1.place(x=720, y=30)
        self.ch2.place(x=800, y=30)
        self.ch3.place(x=880, y=30)

        # 商品选择
        tk.Label(self.frm_b, text="请输入序号:").place(x=30, y=90)
        self.num_en.place(x=105, y=90)
        self.num_var.set("（提示：若输入多个序号请用空格隔开）")

        # 确认
        comfirm1 = tk.Button(self.frm_t, text="开始爬取", command=self.getInfo, width=20)
        comfirm1.place(x=980, y=30)
        # 个人中心
        # comfirm = tk.Button(self.frm_t, text="个人中心", command=self.personal, width=16)
        # comfirm.place(x=350, y=90)
        # 开始比价
        comfirm2 = tk.Button(self.frm_t, text="开始比较", command=self.compare, width=16)
        comfirm2.place(x=500, y=90)

        # 加入关注列表
        self.comfirm3.config(command=self.addtoDB)
        self.comfirm3.place(x=650, y=90)

        # 显示关注列表
        comfirm4 = tk.Button(self.frm_t, text="关注列表", command=self.showDB, width=16)
        comfirm4.place(x=810, y=90)

        # 更新关注列表
        comfirm4 = tk.Button(
            self.frm_t, text="更新关注商品价格", command=self.updateDB, width=16
        )
        comfirm4.place(x=970, y=90)

        # 划线
        canvas1 = tk.Canvas(self.frm_b, bg="white", width=1095, height=3)
        canvas1.place(x=30, y=130)
        canvas2 = tk.Canvas(self.frm_b, bg="white", width=1095, height=3)
        canvas2.place(x=30, y=70)

        # 打印表格头部
        self.tree.column("1", width=50, anchor="w")
        self.tree.heading("1", text="序号")
        self.tree.column("2", width=100, anchor="w")
        self.tree.heading("2", text="ID")
        self.tree.column("3", width=80, anchor="w")
        self.tree.heading("3", text="平台")
        self.tree.column("4", width=300, anchor="w")
        self.tree.heading("4", text="标题")
        self.tree.column("5", width=150, anchor="w")
        self.tree.heading("5", text="商铺")
        self.tree.column("6", width=80, anchor="w")
        self.tree.heading("6", text="价格")
        self.tree.column("7", width=80, anchor="w")
        self.tree.heading("7", text="好评数")
        self.tree.column("8", width=255, anchor="w")
        self.tree.heading("8", text="链接")
        self.VScroll1.place(relx=0.979, rely=0, relwidth=0.020, relheight=1)
        self.tree.configure(yscrollcommand=self.VScroll1.set)
        self.tree.place(x=30, y=150)
        # self.window.mainloop()


if __name__ =='__main__':
    ui = GUI()
    ui.mainwindow()
