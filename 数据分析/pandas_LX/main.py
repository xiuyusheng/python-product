import pandas as pd
from pandas import DataFrame

# ? 读取excel文件
# file_path = r"游戏合集.xlsx"
# excel = pd.read_excel(io=file_path, sheet_name="游戏资源")

# ?创建DataFrame对象
df = pd.DataFrame(
    {"sid": ["s1", "s2", "s3"], "name": ["xiaoming", "like", "Mike"]}
)  # ?传入一个字典，key为列名，value为值

print(df)
# ? DataFrame对象操作
# ? print(excel)  #? 打印全部，太多会用省略号省略
# ? print(excel.columns)  #? 打印数据列名，一般就是第一列
# ? print(excel.head())  #? 打印前五行，head可传入读取的行数
# ? print(excel.index)  #? 打印行，其实行号和末尾行号
# ? print(excel["姓名"])  #? 打印指定列名的列，找不到则会报错
# ? print(excel.describe())  #? 描述数据
# ? excel.loc[100] = ["val1", "val2", "val3", "val3", "val3", "val3"]  #? 修改某一行,超出最大索引值则新增一行
# ? excel["favorite"] = None #?新增一列空值
# ? excel.astype({"num": int}, errors="ignore")  #? 修改列的数据类型,errors="ignore"遇到错误跳过
# ?#? raise：如果遇到无法转换的数据，将引发ValueError错误。
# ?#? ignore：如果遇到无法转换的数据，将跳过它们，并将它们保留为原始的数据类型。
# ? excel["temp_f1"] = excel["num"] #? 修改指定列名的列，如果列名不存在则重新创建一列。

# ? 拼接DataFrame对象
# ? df1 = pd.DataFrame({"sid": ["s1", "s2"], "name": ["xiaoming", "Mike"]})
# ? df2 = pd.DataFrame({"sid": ["s3", "s4"], "name": ["Tom", "Peter"]})
# ? pd.concat([df1, df2], axis=0)  #? 纵向拼接两个DataFrame对象，以X轴行名为基准合并，axis=0，不写默认为0
# ? pd.concat([df1, df2], axis=1)  #? 横向拼接两个DataFrame对象，以Y轴行名为基准合并


# ? DataFrame(excel).to_excel(
# ?     file_path, sheet_name="游戏资源", index=False, header=True
# ? )  #? 写入excel
