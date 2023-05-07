class Goods:
    __id = ''
    __platform = ''
    __title = ''
    __shop = ''
    __price = 0
    __sales = ''
    __href = ''

    def __init__(self,id,platform,title,shop,price,sales,href):
        self.__id = id
        self.__platform = platform
        self.__title = title
        self.__shop = shop
        self.__price = price
        self.__sales = sales
        self.__href = href

    def setID(self,id):
        self.__id = id

    def getID(self):
        return self.__id

    def setPlatform(self,platform):
        self.__platform = platform

    def getPlatform(self):
        return self.__platform

    def setTitle(self,title):
        self.__title = title

    def getTitle(self):
        return self.__title

    def setShop(self,shop):
        self.__shop = shop

    def getShop(self):
        return self.__shop

    def setPrice(self,price):
        self.__price = price

    def getPrice(self):
        return self.__price

    def setSales(self,sales):
        self.__sales = sales

    def getSales(self):
        return self.__sales

    def setHref(self,href):
        self.__href = href

    def getHref(self):
        return self.__href

    def update(self):
        from CrawlProgram import CrawlProgram
        from DBConnection import DBConnection
        crawl = CrawlProgram()
        abc = DBConnection()
        if self.__id[0] == 'G':
            p_change = crawl.getgomeItemInfo(self)
            abc.update(self)
            return p_change
        elif self.__id[0] == 'J':
            p_change = crawl.getJDItemInfo(self)
            abc.update(self)
            return p_change
        elif self.__id[0] == 'P':
            p_change = crawl.getPinduoduoItemInfo(self)
            abc.update(self)
            return p_change
        else:
            return 0

if __name__ == '__main__':
    goods1 = Goods('P1517243181', '拼多多', '小学生书包男1-3-6年级6-14岁男女孩背包儿童书包女学生韩版防水', '无相关信息',25.9, '3045' ,'https://youhui.pinduoduo.com/goods/goods-detail?goodsId=1517243181')
    goods2 = Goods('J65136898327', '京东', '耐拓 小学生书包男孩轻便减压1-3-6年级儿童书包 N897宝蓝大号3-6年级 均', '耐拓旗舰店', 79.0 ,'无相关信息' ,'https://item.jd.com/65136898327.html')
    goods3 = Goods('T566902039289', '天猫', 'Samsonite/新秀丽学院风双肩包男背包 商务男士旅行包潮流书包TQ5', '新秀丽背包旗舰店', 549.0 ,'375' ,'https://detail.tmall.com/item.htm?id=566902039289&skuId=3769598087310&user_id=2567440597&cat_id=2&is_b=1&rn=1e282ae86fedd74a5d8acbe63929f971')
    print(goods1.update())
    print(goods2.update())
    print(goods3.update())