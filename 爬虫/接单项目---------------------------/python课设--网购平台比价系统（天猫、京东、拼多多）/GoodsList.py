from CrawlProgram import CrawlProgram
from Goods import Goods
from DBConnection import DBConnection

class GoodsList:
    __goodslist = []
    __tmall = False
    __jd = False
    __pdd = False
    __keyword = ''
    __number = 0

    def __init__(self,keyword,number,tmall = False,jd = False,pdd = False):
        self.__goodslist = []
        self.__tmall = tmall
        self.__jd = jd
        self.__pdd = pdd
        self.__keyword = keyword
        self.__number = number

    def getGoodsList(self):
        return self.__goodslist

    def getGoods(self):
        crawl = CrawlProgram()
        if self.__tmall:
            self.__goodslist.extend(crawl.getItemsFromgome(self.__keyword,self.__number))
        if self.__jd:
            self.__goodslist.extend(crawl.getItemsFromJD(self.__keyword,self.__number))
        if self.__pdd:
            self.__goodslist.extend(crawl.getItemsFromPinduoduo(self.__keyword,self.__number))

    def sort(self,data = '',reverse = False):
        if data == '':
            data = self.__goodslist
        result = sorted(data,key = lambda x:int(x.getPrice()),reverse = reverse)
        return result

    def compare(self,goods):
        data = self.sort(goods)
        total = 0
        for item in data:
            total = int(total) + int(item.getPrice())
        avg = total/len(data)
        return '价格最低的是 \"' + data[0].getPlatform() + '\" 平台的 \"' + data[0].getTitle() + '\" ，其价格为： '+ str(data[0].getPrice()) +' 元，比这 ' + str(len(data)) + ' 个商品的平均价格便宜 ' + str(round(avg - data[0].getPrice(),2)) + ' 元'

if __name__ =='__main__':
    gl = GoodsList('钢笔',20,tmall = True,jd = True,pdd = True)
    gl.getGoods()
    ls = gl.sort()
    dbc = DBConnection()
    for it in ls:
        print(it.getID(),it.getPlatform(),it.getTitle(),it.getShop(),it.getPrice(),it.getSales(),it.getHref())
        #dbc.save(it)