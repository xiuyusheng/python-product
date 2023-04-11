import matplotlib.pyplot as plt
from matplotlib import rcParams
import json
import login
login.get()#刷新数据
data=list()#数据
data_n=list()#标签
explode=list()#偏移值
with open('1024code.json','r',encoding='utf-8') as f:
    d_list=json.load(f)['data']
    for i in d_list:
        data.append(i['发布'])
        if i['name']=='黑色史莱姆':
            explode.append(0.2)
        else:
            explode.append(0)
        data_n.append(i['name'] if i['发布'] else '')

rcParams['font.family'] = 'SimHei'#全局字体
plt.figure(figsize=(20, 20),dpi=40)#页面大小
my_font ={'family': 'SimHei',       #属性
        'color':  'darkred',
        'weight': 'normal',
        'size': 30,
        }
plt.pie(data, labels=data_n, textprops={'fontsize': 20},explode=explode)#生成饼图
plt.legend(title='图例', loc='best', bbox_to_anchor=(1.6, 1.2), fontsize=20)#生成图例
plt.title('1024发布数统计表', fontdict=my_font)#生成标题
plt.show()

