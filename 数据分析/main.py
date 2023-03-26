from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import font_manager
#设置系统字体
# font = {
#     'family': 'MicroSoft YaHei',
#     'weight': 'bold',
#     'size': 'larger'
# }
# rc("font", **font)

#创建中文字体实例
my_font = font_manager.FontProperties(fname='zt.ttf', size=20)

#x，y轴数据信息
x = list(range(1, 6))
y = list(range(1, 6))

#轴体显示信息
x_ = list('{},你好'.format(i) for i in range(1, 6))

#图框大小设置
plt.figure(figsize=(10, 8), dpi=50)

#介入数据
plt.plot(x, y)

#介入x轴
plt.xticks(x, x_, rotation=45, fontproperties=my_font)

plt.show()
