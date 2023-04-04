import xlrd
import os
data = xlrd.open_workbook('RJB.xlsx')
table=data.sheets()[0]
for i in range(1,54):

    print(f'\'{int(table.row(i)[2].value)}\':\'{table.row(i)[0].value}\',')
