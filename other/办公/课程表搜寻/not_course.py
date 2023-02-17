import xlrd
import xlwt
import os
import re
if(not os.path.exists('course')):
    print('未找到发现course文件夹，同步地址后重试！')
else:
    os.system('cls')
    reg1 = re.compile(r'(\d{1,2})\s*[-~——－]*\s*(\d{1,2})*')  #提取时间
    time_re = re.compile(r'([1-5])>([0-2])')
    time_ = input('请输入查询时间（例如：1>0（周一上午）,“>”前1-5为周一至周五，“>”后0-2为上午、下午、晚上）\n')
    time_list_start = {'1': '周一', '2': '周二', '3': '周三', '4': '周四', '5': '周五'}
    time_list_end = {'0': '上午', '1': '下午', '2': '晚上'}
    timt_Summation = []  #最终时间
    pass_key = time_re.search(time_) == None  #是否重新输入
    while True:
        while (pass_key):
            os.system('cls')
            time_ = input(
                '请输入查询时间（例如：1>0（周一上午）,“>”前1-5为周一至周五，“>”后0-2为上午、下午、晚上）\n\033[31m请重新输入：\033[0m'
            )
            pass_key = time_re.search(time_) == None
        print(
            f'请确认时间：\033[4;93m{time_list_start[time_re.findall(time_)[0][0]]}{time_list_end[time_re.findall(time_)[0][1]]}\033[0m'
        )
        Confirm = input('Y（是）、N（否）:')
        if Confirm == 'Y' or Confirm == 'y':
            print('\033[1;92m时间确立√\033[0m')
            timt_Summation = time_re.findall(time_)[0]
            break
        pass_key = True
    # try:
    for root, dirs, files in os.walk('course'):
        for file in files:
            if((not (re.search(r'.xlsx',file) ==None and  re.search(r'.xls',file) ==None) and re.search(r'~\$22 ',file)==None)):
                # print(re.search(r'~\$22 ',file)==None)
                print(file.replace('.xlsx', ''))
                #文件名以及路径，如果路径或者文件名有中文给前面加一个 r
                data = xlrd.open_workbook(f'course/{file}')
                #根据索引获取工作表
                table = data.sheets()[0]
                nrows = table.nrows#表格的有效行数
                wh=[0,0]
                key=False
                for nrow in range(nrows):
                    if(key):
                        break
                    # print(table.row_values(ncol, start_colx=0, end_colx=10))
                    for index,val in  enumerate(table.row_values(nrow, start_colx=0, end_colx=10)):
                        if(not reg1.search(val)==None):
                            # print(wh[1])
                            wh[0]=nrow
                            wh[1]=index
                            key=True
                            break

                
                for i in [ 1,0]:
                    # print(f'{(int(timt_Summation[1]) + 1)*2+(wh[0]-1) -i},{int(timt_Summation[0])+(wh[1]-1)},{wh[0]},{wh[1]}')

                    value = table.cell_value(((int(timt_Summation[1]) + 1)*2+(wh[0]-1) -i),
                                            int(timt_Summation[0])+(wh[1]))
                    # print(f'{(int(timt_Summation[1]) + 1)*2+(wh[0]-1) -i},{int(timt_Summation[0])+(wh[1]-1)}')
                    if (reg1.search(value)==None):
                        print(('后一节' if i == 0 else '前一节') + '满课')
                    else:
                        text=''
                        for not_course in reg1.findall(value):
                            if(not not_course[1]==''):
                                text+=f'【\033[1;92m{not_course[0]}\033[0m周至\033[1;92m{not_course[1]}\033[0m周无课】'
                            else:
                                text+=f'【\033[1;92m{not_course[0]}\033[0m周周无课】'
                        print(text)

            else:
                print('\033[31m'+file+'格式错误跳过\033[0m')
            print('\n')
    # except:
    #     print('\033[31m未在目录中发现名为course的文件夹\033[0m')   
os.system("pause")
