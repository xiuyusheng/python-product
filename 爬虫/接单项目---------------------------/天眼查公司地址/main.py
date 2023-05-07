import requests
import xlrd
import xlwt
import re
import json


if __name__=="__main__":
    session=requests.Session()
    new_data = xlwt.Workbook()
    work_sheet = new_data.add_sheet('sheet1')
    data = xlrd.open_workbook(r'./新建 XLSX 工作表.xlsx')
    table = data.sheets()[0]
    row = table.row(0)
    work_sheet.write(0,0,'申请人')
    work_sheet.write(0,1,'地址')
    work_sheet.write(0,2,'省份')
    work_sheet.write(0,3,'备注')

    for k,j in enumerate(list(i.value for i in table.col(0,start_rowx=1))):
        work_sheet.write(k+1,0,j)
        con_name=j##
        print(con_name)
        head={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
        }
        url='https://www.tianyancha.com/search?key={}'.format(con_name)
        Resp=session.get(url=url,headers=head)
        json_=json.loads(re.search(r'<script id="__NEXT_DATA__" type="application/json">(?P<json_>.*?)</script>',Resp.text).group('json_'))
        with open('op.json','w',encoding='utf-8') as f:
            json.dump(json_,f,ensure_ascii=False)
        try:
            text_=json_['props']['pageProps']['dehydratedState']['queries'][0]['state']['data']['data']['companyList'][0]
            # if text_['name'].replace('<em>','').replace('</em>','')==con_name:
            work_sheet.write(k+1,1,text_['regLocation'].replace('<em>','').replace('</em>','') if text_['regLocation'].replace('<em>','').replace('</em>','') else 'NA')
            work_sheet.write(k+1,2,text_['base'] if text_['base'] else 'NA')
            if text_['name'].replace('<em>','').replace('</em>','')!=con_name:
                work_sheet.write(k+1,3,text_['name'].replace('<em>','').replace('</em>',''))
            else:
                work_sheet.write(k+1,3,'无')

            print(text_['regLocation'].replace('<em>','').replace('</em>',''))
        except:
            work_sheet.write(k+1,1,'NA')
            work_sheet.write(k+1,2,'NA')
            work_sheet.write(k+1,3,'无')
            print('无')
        Resp.close()
    new_data.save('地址.xls')
