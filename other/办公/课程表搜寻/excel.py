       #文件名以及路径，如果路径或者文件名有中文给前面加一个 r
        # data = xlrd.open_workbook(path)
        #根据索引获取工作表
        # table = data.sheets()[0]
        #通过名称获取工作表
        # table1 = data.sheet_by_name('sheet')
        #返回工作表名称
        # names = data.sheet_names()

        


        # #行操作#####################################
        # # 获取该sheet中的行数，注，这里table.nrows后面不带()
        # nrows = table.nrows
        # row=table.row(1)
        # # 返回由该行中所有的单元格对象组成的列表,这与tabel.raw()方法并没有区别。
        # table.row_slice(1)
        # # 返回由该行中所有的单元格对象组成的列表
        # table.row_types(0, start_colx=0, end_colx=None)
        # # 返回由该行中所有单元格的数据类型组成的列表；
        # # 返回值为逻辑值列表，若类型为empy则为0，否则为1
        # table.row_values(1, start_colx=0, end_colx=None)
        # # 返回由该行中所有单元格的数据组成的列表
        # row_len=table.row_len(1)
        # # print(table.row_len(3))
        # # 返回该行的有效单元格长度，即这一行有多少个数据

        # #列操作#####################################
        # ncols = table.ncols
        # # print('列数为'+str(ncols))
        # # 获取列表的有效列数
        # table.col(0, start_rowx=0, end_rowx=None)
        # # 返回由该列中所有的单元格对象组成的列表
        # table.col_slice(0, start_rowx=0, end_rowx=None)
        # # 返回由该列中所有的单元格对象组成的列表
        # table.col_types(0, start_rowx=0, end_rowx=None)
        # # 返回由该列中所有单元格的数据类型组成的列表
        # table.col_values(0, start_rowx=0, end_rowx=None)
        # # 返回由该列中所有单元格的数据组成的列表

        # #单元格操作#####################################
        # table.cell(0, 0)
        # # 返回单元格对象
        # table.cell_type(0, 0)
        # # 返回对应位置单元格中的数据类型
        # value = table.cell_value(2, 1)
        # # 返回对应位置单元格中的数据