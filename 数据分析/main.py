from matplotlib import pyplot as plt
from matplotlib import rc

font = {
    'family': 'MicroSoft YaHei',
    'weight': 'bold',
    'size': 'larger'
}
rc("font", **font)
x = list('你好，{}'.format(i) for i in range(1, 4))
y = list(range(1, 4))
plt.figure()
plt.plot(x, y)
plt.show()
