# '''
# ?          规则：
# ?         招募（Q）、商店（P 物品名（物资和武器） 套餐号*）
# ?         探寻（E 目标*）、治疗（T 治疗数量）
# ?         训练士兵（W 所要训练士兵的等级* 数量*）
# ?         训练俘虏（WW 俘虏等级* 数量*）
# '''
import random
from numpy import random as random_
import sys
sys.setrecursionlimit(100000) #例如这里设置为十万 

class games():
    def __init__(self) -> None:
        self.Attack = ['土匪', '军队', '军团']
        self.Military = ['大兵', '班长', '排长', '连长', '营长', '团长', '旅长', '师长', '军长']
        self.Soldiers = []  # 士兵等级数
        self.Capture = []  # 俘虏等级数
        self.Woundeds = [0]  # 伤员
        self.myself = {
            'Money': 200,  # 金币
            'Material': 0,  # 物资
            'Weapon': 0,  # 武器
            'Prestige': 100,  # 声望
            'Military': 0,  # 军衔
            'Attack': 1  # 攻击目标
        }

    def Home(self, msg=''):  # 会话
        print(f'''
        您的资产：

        【\033[35m物资\033[0m】{self.myself['Material']}\t【\033[{'31m' if not sum(self.Woundeds) else '33;5m'}伤员\033[0m】{sum(self.Woundeds)}
        \t【\033[33m金币\033[0m】{self.myself['Money']}
        【\033[36m士兵\033[0m】{sum(self.Soldiers)}\t【\033[36m俘虏\033[0m】{sum(self.Capture)}

        【\033[33m声望\033[0m】{self.myself['Prestige']}\t【\033[37m武器\033[0m】{self.myself['Weapon']}
|---------------------------------------|
|       【\033[33m军衔\033[0m】{self.Military[self.myself['Military']]}\t【\033[31m战力\033[0m】{sum((i+1)*j for i,j in enumerate(self.Soldiers))+self.myself['Weapon'] }\t|
|---------------------------------------|
        ''')
        print('\033[4;32m'+msg+'\033[0m')
        print('\n'.join(f'{i+1}等兵:{j}人' for i, j in enumerate(self.Soldiers) if j!=0))
        print('\n'.join(f'{i+1}等伤员:{j}人' for i, j in enumerate(self.Woundeds) if j!=0))
        print('可攻打：' + '、'.join(self.Attack[:self.myself['Attack']]))
        self.upgrade()

    def recruit(self):  # 招募
        if len(self.Soldiers):  # 是否有初始队伍
            # 士兵数量不能超过军衔限制人数
            if sum(self.Soldiers) < ((10*(self.myself['Military']+1))**2)//2:
                # 招募人数以威望为基准向两边扩散威望半只范围为随机招募人数
                nums = random.randint(
                    self.myself['Prestige']//2, self.myself['Prestige']//2*3)
                self.Soldiers[0] += nums
                self.Home(f'招募到了{nums}人')
            else:
                self.Home('请提升战力，更高的军衔可以招募更多的士兵╰（‵□′）╯')
                return
        else:  # 初始化队伍
            self.Soldiers.append(0)
            self.recruit()

    def training_Soldiers(self, num=None, grade=None):  # 训练士兵
        if num or grade:
            def XL(num_, grade_):
                M = min(num_, self.Soldiers[grade_-1],
                        self.myself['Material']//grade_, self.myself['Weapon'])
                num_ -= M
                self.Soldiers[grade_-1] -= M
                self.myself['Material'] -= M*grade_
                self.myself['Weapon'] -= M
                if grade_ == len(self.Soldiers):
                    self.Soldiers.append(0)
                self.Soldiers[grade_] += M
                return M
            nums = 0
            if grade:
                if num:
                    nums = XL(num, grade)
                else:
                    nums = XL(self.Soldiers[grade], grade)
            else:
                nums = num
                for i in range(len(self.Soldiers)):
                    num -= XL(num, i+1)
                nums -= num
            self.Home('训练了{}个士兵'.format(nums))
        else:
            self.Home('{}，您啥信息都不给，属下无法完成'.format(
                self.Military[self.myself['Military']]))

    def training_Captures(self, num=None, grade=None):  # 说服俘虏
        if num or grade:
            def XL(num_, grade_):
                M = min(num_, self.Capture[grade_-1],
                        self.myself['Material']//grade_)
                self.Capture[grade_-1] -= M
                self.myself['Material'] -= M*grade_
                self.Soldiers[grade_-1] += M
                return M
            nums = 0
            if grade:
                if num:
                    nums = XL(num, grade)
                else:
                    nums = XL(self.Soldiers[grade], grade)

            else:
                nums = num
                for i in range(len(self.Soldiers)):
                    num -= XL(num, i+1)
                nums -= num
            self.Home('说服了{}个俘虏'.format(nums))
        else:
            self.Home('{}，您啥信息都不给，属下无法完成'.format(
                self.Military[self.myself['Military']]))

    def Therapeutic(self, num=None, grade=None):  # 治疗
        def xL(i, j, num_):
            if self.myself['Material'] >= (i+1)*j:
                self.Soldiers[i] += self.Woundeds[i]
                self.myself['Material'] -= (i+1)*j
                self.Woundeds[i] = 0
                num_ += (i+1)*j
            else:
                self.Woundeds[i] -= self.myself['Material']//(i+1)
                self.Soldiers[i] += self.myself['Material']//(i+1)
                num_ += self.myself['Material']//(i+1)
                self.myself['Material'] = 1 if self.myself['Material'] % (
                    i+1) else 0
            return num_
        num_ = 0
        if not num:
            sum_Woundeds_Material = sum(
                (i+1)*j for i, j in enumerate(self.Woundeds) if (grade-1 if grade else i) == i)
            if self.myself['Material'] >= sum_Woundeds_Material:
                if not grade:
                    for i in range(len(self.Soldiers)):
                        self.Soldiers[i] += self.Woundeds[i]
                        num_ += self.Woundeds[i]
                        self.Woundeds[i] = 0
                else:
                    self.Soldiers[grade-1] += self.Woundeds[grade-1]
                    num_ += self.Woundeds[grade-1]
                    self.Woundeds[grade-1] = 0
                self.myself['Material'] -= sum_Woundeds_Material
            else:
                if not grade:
                    for i, j in enumerate(self.Woundeds):
                        num_ = xL(i, j, num_)
                else:
                    num_ = xL(grade-1, self.Woundeds[grade-1], num_)
            self.Home('治疗了{}个伤员..{}'.format(num_,'（请准备好物资）' if not num_ else '' ))
        else:
            if grade and num > self.Woundeds[grade-1]:
                num_ = self.Therapeutic(0, grade)
                return
            elif not grade and num > sum(self.Woundeds):
                num_ = self.Therapeutic()
                return
            else:
                if grade:
                    if self.myself['Material'] >= self.Woundeds[grade-1]*grade:
                        num_ = num
                        self.myself['Material'] -= num*grade
                        self.Woundeds[grade-1] -= num
                        self.Soldiers[grade-1] += num
                    else:
                        num_ = self.myself['Material']//grade
                        self.Woundeds[grade-1] -= num_
                        self.myself['Material'] = 1 if self.myself['Material'] % grade else 0
                        self.Soldiers[grade-1] += num_
                else:
                    for i in range(len(self.Woundeds)):
                        if self.myself['Material']//(i+1) >= num:
                            if self.Woundeds[i] >= num:
                                self.Woundeds[i] -= num
                                self.myself['Material'] -= num*(i+1)
                                self.Soldiers[i] += num
                                num_ += num
                                num = 0
                                break
                            else:
                                N = self.Woundeds[i]
                                num -= N
                                self.Soldiers[i] += N
                                self.myself['Material'] -= N*(i+1)
                                num_ += N
                                self.Woundeds[i] = 0
                        else:
                            if self.Woundeds[i] >= self.myself['Material']//(i+1):
                                N = self.myself['Material']//(i+1)
                                self.Woundeds[i] -= N
                                self.Soldiers[i] += N
                                num_ += N
                                num -= N
                                break
                            else:
                                N = self.Woundeds[i]*(i+1)
                                self.myself['Material'] -= N
                                self.Soldiers[i] += N
                                num_ += N
                                num -= N
            self.Home('治疗了{}个伤员...'.format(num_))

    '''
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
    '''

    def shop(self, name, num=None, id=None):  # 商店
        def GW(name_, num_):
            price = {
                'Material': 1,
                'Weapon': 2
            }
            if self.myself['Money'] >= num_*price[name_]:
                self.myself['Money'] -= num_*price[name_]
                self.myself[name_] += num_
                self.Home('已购买了{}个{}'.format(
                    num_, '物资' if name_ == 'Material' else '武器'))
            else:
                self.Home('{}，您的金币已不足，请另下决策'.format(
                    self.Military[self.myself['Military']]))
        if id == 1:
            GW(name_=name, num_=100 if name == 'Material' else 50)
        elif id == 2:
            GW(name_=name, num_=200 if name == 'Material' else 100)
        elif id == 3:
            GW(name_=name, num_=1000 if name == 'Material' else 500)
        elif id == 4:
            GW(name_=name, num_=2000 if name == 'Material' else 1000)
        else:
            if num:
                if name in 'Material,Weapon':
                    GW(name_=name, num_=num)
                else:
                    self.Home('属下听不懂您的命令')
            else:
                self.Home('属下不明白您需要多少的{}'.format(
                    '物资' if name == 'Material' else '武器'))

    def upgrade(self):  # 越级
        sum_ = sum((i+1)*j for i, j in enumerate(self.Soldiers)) + \
            self.myself['Weapon']
        if sum_//(100*((self.myself['Military']+1)**2)):
            if self.myself['Military'] == len(self.Military)-1:
                return
            self.myself['Military'] += 1
            print('恭喜您晋升为{}了'.format(self.Military[self.myself['Military']]))
            self.upgrade()
        else:
            return

    '''
    |---------------------------------------|
    |            发现                       |
    |           士兵数量：soldiers           |
    |                                       |
    |---------------------------------------|
    '''

    def explore(self, Attack=None):  # 探寻
        def TC(Attack_):
            power = random.randint((10*(Attack_-1)*2)**2, (10*Attack_*2)**2)
            Weapon = random.randint(power//4, power//2)
            Soldier_power = power-Weapon  # 战力限制
            Soldiers = [0]  # 兵力限制
            Soldiers[0] += random.randint(0, Soldier_power//3)
            Soldier_power = (Soldier_power//3)*2
            n = 2
            while True:
                if Soldier_power//n > 1:
                    if n >= 8:
                        Soldiers[0] += Soldier_power
                        break
                    Soldiers.append(0)
                    Soldiers[n-1] = random.choices(
                        range(Soldier_power//n), cum_weights=range(Soldier_power//n))
                    Soldiers[n-1] = Soldiers[n-1][0]
                    Soldier_power -= Soldiers[n-1]
                    n += 1
                else:
                    Soldiers[0] += Soldier_power
                    break
            return Attack_, Soldiers, power
        Attack__, Soldier, power = TC(
            Attack if Attack else random.randint(1, self.myself['Attack']))
        result = input('''
---------------------------------------------
|                发现敌人：{}           \t|
|                士兵数量：{}           \t|
|           是否对其展开攻击（Y（是）、\t|
|           任意键（否）、E（重新））\t|
---------------------------------------------
        '''.format(self.Attack[Attack__-1], sum(Soldier)))
        if result == 'E' or result == 'e':
            self.explore(Attack if Attack else random.randint(
                1, self.myself['Attack']))
        elif result == 'Y' or result == 'y':
            attack_result = random.choices([True, False], cum_weights=[sum(
                (i+1)*j for i, j in enumerate(self.Soldiers))+self.myself['Weapon'], power])
            result_updata={
                'Prestige':'',#?声望
                'Soldiers':'',#?武器
                'Woundeds':'',#?伤员
                'Weapon':'',#?武器
                'Capture':'',#?俘虏
                'Material': '',  #?物资
                'Money':''#?金币
            }
            #声望
            result_updata['Prestige']='{}{}\033[0m'.format('\033[32m+' if attack_result[0] else '\033[31m-',self.myself['Prestige']//10)
            self.myself['Prestige']+=(self.myself['Prestige']//10) if attack_result[0] else (-self.myself['Prestige']//10)
            
            #武器
            result_updata['Weapon']='\033[31m-{}\033[0m'.format(self.myself['Weapon']//10 if attack_result[0] else self.myself['Weapon']//10)
            self.myself['Weapon']-=self.myself['Weapon']//10 if attack_result[0] else self.myself['Weapon']//20

            #死亡
            result_updata['Soldiers']='\033[31m+'+str(sum(Soldier)//(10 if attack_result[0] else 8))+'\033[0m'
            len__=len(self.Soldiers)
            def SW(Soldier_):
                len_=len(Soldier_)
                for i in range(len__):
                    if i==len_-1:
                        return
                    self.Soldiers[i]-=Soldier_[i]//10  #士兵减少 
                    if i==len__-1:
                        SW(Soldier_=Soldier_[len__:])
                        return
            SW(Soldier_=Soldier)
            
            #伤员
            result_updata['Woundeds']='\033[31m+'+str(sum(Soldier)//(random.randint(16,23) if attack_result[0] else 15))+'\033[0m'
            len__=len(self.Woundeds)
            def SS(Soldier_):
                len_=len(Soldier_)
                for i in range(len__):
                    if i==len_-1:
                        return
                    self.Woundeds[i]+=Soldier_[i]//20 #伤员增加
                    self.Soldiers[i]-=Soldier_[i]//20 #士兵减少
                    if i==len__-1:
                        SS(Soldier_=Soldier_[len__:])
                        return
            SS(Soldier_=Soldier)

            #俘虏

            def FL(Soldier_):
                Capture_=0
                len_=len(Soldier_)
                len__=len(self.Capture)
                for i in range(len_):
                    if len__==i:
                        self.Capture.append(0)
                        len__+=1
                    self.Capture[i]+=Soldier_[i]//(10 if attack_result[0] else 20) #伤员增加
                    Capture_+=Soldier_[i]//(10 if attack_result[0] else 20)
                return Capture_
            Capture_=FL(Soldier_=Soldier)
            result_updata['Capture']='\033[32m+{}\033[0m'.format(Capture_)

            #物资
            weight=[2,3,4,5,6,7]
            weight.sort(reverse=(True if attack_result[0] else False))
            num=sum(self.Soldiers)//(random.choices(range(6,12),cum_weights=weight)[0])
            result_updata['Material']='{}{}\033[0m'.format('\033[32m+' if attack_result[0] else '\033[31m-',num)
            self.myself['Material']+=num

            #金币
            weight=list(range(1,5))[::(-1 if attack_result[0] else 1)]
            num=self.myself['Money']//(random.choices(range(8,12),cum_weights=weight)[0])
            result_updata['Money']='{}{}\033[0m'.format('\033[32m+' if attack_result[0] else '\033[31m-',num)
            self.myself['Money']+=num

            self.Home('{}，咱们{}了\n死亡：{}\n伤员：{}\n声望：{}\n武器：{}\n物资{}\n金币{}\n俘虏：{}'.format(
                self.Military[self.myself['Military']], '\033[33m胜利\033[0m' if attack_result[0] else '\033[31m战败\033[0m',result_updata['Soldiers'],result_updata['Woundeds'],result_updata['Prestige'],result_updata['Weapon'],result_updata['Material'],result_updata['Money'],result_updata['Capture']))
        else:
            self.Home('已结束探索')

# if __name__ == '__main__':
#     games = games()
#     games.Home()
#     # games.recruit()
#     # games.training_Soldiers()
#     # games.Therapeutic(40, 0)
#     # games.training_Captures(3,2)
#     # games.shop('Weapon',id=4)
#     # games.explore()
