import fun

def CV(Callback,Military):
    if len_>1:
        if  cmd[1].isdigit():
            if len_>2:
                if cmd[2].isdigit():
                    Callback(num=int(cmd[1]),grade=int(cmd[2]))
                else:
                    print(f'仅接收数字作为{Military}对象的等级')
            else:
                Callback(num=int(cmd[1]))
        else:
            print(f'仅接收数字作为{Military}对象的数量')
    else:
        cmd_=input(f'''
            请输入{Military}士兵的数量或等级
            例如：10 1
            第一列为数量，第二列为等级，如参数为‘0’则忽略
            例如：0 1
            代表仅仅{Military}等级为1的伤员，只输入一个参数或包含非数字退出
        ''').split()
        len__=len(cmd_)
        if len__==2 and cmd_[0].isdigit() and cmd_[1].isdigit():
            print(cmd_,len__)
            Callback(num=int(cmd_[0]),grade=int(cmd_[1]))
        

if __name__ == '__main__':
    fun_ = fun.games()
    fun_.Home('''
规则：
招募（Q）、商店（P 物品名（物资和武器） 套餐号*）
探寻（E 目标*）、治疗（T 治疗数量）
训练士兵（W 所要训练士兵的等级* 数量*）
训练俘虏（WW 俘虏等级* 数量*）''')
    while True:
        cmd = input('{}，下达你的命令：'.format(
            fun_.Military[fun_.myself['Military']])).split()
        if not cmd:
            continue
        len_ = len(cmd)
        if cmd[0] in ['Q', 'q', 'P', 'p', 'E', 'e', 'T', 't', 'W', 'w', 'WW', 'ww']:
            if cmd[0] == 'Q' or cmd[0] == 'q':
                fun_.recruit()
            elif cmd[0] == 'P' or cmd[0] == 'p':
                if len_ > 1 and cmd[1] in '物资，武器':
                    if len_ > 2 and cmd[2].isdigit():
                        fun_.shop(name='Material' if cmd[1]=='物资' else 'Weapon', num=int(cmd[2]))
                    else:
                        fun_.shop(name='Material' if cmd[1]=='物资' else 'Weapon', id=int(input(f'''
    |---------------------------------------|
    |  套餐一（id=1）：50金币---->100物资     |
    |  套餐二（id=2）：100金币---->200物资    |
    |  套餐三（id=3）：500金币---->1000物资   |
    |  套餐四（id=4）：1000金币---->2000物资  |
    |---------------------------------------|
    |---------------------------------------|
    |  套餐一（id=1）：50金币---->50武器      |
    |  套餐二（id=2）：100金币---->100武器    |
    |  套餐三（id=3）：500金币---->500武器    |
    |  套餐四（id=4）：1000金币---->1000武器  |
    |---------------------------------------|
    您选购的是{cmd[1]}
    请输入id:
    ''')))
                else:
                    print('请正确输入商品名,‘物资’、‘武器’')
            elif cmd[0] == 'E' or cmd[0] == 'e':
                if len_ > 1 and 0 < (int(cmd[1]) if cmd[1].isdigit() else False) <= len(fun_.Attack):
                    fun_.explore(int(cmd[1]))
                else:
                    print('随机探寻')
                    fun_.explore()
            elif cmd[0] == 'T' or cmd[0] == 't':
                CV(fun_.Therapeutic,'治疗')
            elif cmd[0] == 'W' or cmd[0] == 'w':
                CV(fun_.training_Soldiers,'训练')
            elif cmd[0] == 'WW' or cmd[0] == 'ww':
                CV(fun_.training_Captures,'说服俘虏')
        else:
            print('‘{}’命令错误'.format(cmd[0]))
