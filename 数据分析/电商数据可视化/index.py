import pandas as pd
data = pd.read_csv('双十一淘宝美妆数据.csv')
# print(data.id)        # 单单输出一列
# print(data.head(20))  # head()方法默认查看csv前5行数据，也可增加n参数来读取更多行，如n=10可读取前10行数据
# print(data.shape)     #查看导入数据行列总
# print(data.describe())#对列进行描述
# print(data.info())    # 查看各字段信息，表格中每一列分别为列名、非空数据、数据类型
# print(data.describe())# 处理缺失值，查看每一列是否存在缺失值,isnull()，然而生成的却是所有数据的true／false矩阵，isnull().any() 会判断哪些”列”存在缺失值
# print(data.id.mode()) # sale_count的众数
# data = data.drop_duplicates()#删除重复数据