import pymssql
from Goods import Goods


class DBConnection:
    def connect(self):
        database = pymssql.connect(server="127.0.0.1", database="Goods")
        try:
            cursor = database.cursor()
            cursor.execute(
                "create table goods(goodsID nvarchar(20) Primary key,platform nvarchar(10),title nvarchar(100),shop nvarchar(100),price float,sales nvarchar(10),href nvarchar(300))"
            )
            database.commit()
        except:
            pass
        if database:
            return database
        else:
            print("连接数据库失败")
            return

    def save(self, goods):
        database = self.connect()
        cursor = database.cursor()
        try:
            cursor.execute(
                "select * from goods where goods.goodsID = %s", (goods.getID())
            )
            if cursor.fetchone():
                print(goods.getID() + "已存在")
                return 0
            cursor.execute(
                "insert into goods values(%s,%s,%s,%s,%d,%s,%s)",
                (
                    goods.getID(),
                    goods.getPlatform(),
                    goods.getTitle(),
                    goods.getShop(),
                    goods.getPrice(),
                    goods.getSales(),
                    goods.getHref(),
                ),
            )
            database.commit()
            database.close()
            return 1
        except:
            database.rollback()
            database.close()
            return 0

    def delete(self, goods):
        try:
            database = self.connect()
            cursor = database.cursor()
            cursor.execute(
                "delete from goods where goods.goodsID = %s", (goods.getID())
            )
            database.commit()
            database.close()
            print(goods.getID() + "已成功删除")
        except:
            print("不存在该对象")

    def getInfo(self):
        # try:
        info = []
        database = self.connect()
        cursor = database.cursor()
        cursor.execute("select * from goods")
        row = cursor.fetchone()
        if row:
            while row:
                info.append(list(row))
                row = cursor.fetchone()
        else:
            print("当前数据库中无数据")
        return info

    # except:
    #     print('获取信息失败')
    #     return info

    def update(self, goods):
        database = self.connect()
        cursor = database.cursor()
        try:
            cursor.execute("begin transaction")
            cursor.execute(
                "update goods set price = %d,sales = %s where goodsID = %s;",
                (goods.getPrice(), goods.getSales(), goods.getID()),
            )
            cursor.execute("commit transaction;")
            database.close()
            print(goods.getID() + "已成功更新")
        except Exception as e:
            database.rollback()
            database.close()
            print(goods.getID() + "更新失败" + str(e))


# if __name__ == "__main__":
#     # 测试用例
#     dbc = DBConnection()
#     # g = Goods('11111', 'test', 'test', 'test', 20.00, '10万', 'test')
#     info = dbc.getInfo()
#     for i in info:
#         # gs = Goods(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
#         # dbc.save(gs)
#         print(i)
