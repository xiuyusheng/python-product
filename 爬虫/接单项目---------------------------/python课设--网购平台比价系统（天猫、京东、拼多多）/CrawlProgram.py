import requests
import re
import time
import os
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Goods import Goods
import time


class CrawlProgram:
    def getHTMLText(self, url):
        try:
            kv = {"user-agent": "Mozilla/5.0"}
            r = requests.get(url, headers=kv, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            with open("1.html", "w", encoding="utf-8") as f:
                f.write(r.text)
            return r.text
        except:
            print("获取HTML失败")
            return ""

    def getItemsFromgome(self, keyword, number):
        # 单个页面最多获取60个商品
        session = requests.Session()

        url = f"https://search.gome.com.cn/search?search_mode=normal&reWrite=true&question={keyword}&searchType=goods&instock=1&facets=&page=1&bws=0&type=json&reWrite=true&rank=1"
        head = {
            "referer": "https://search.gome.com.cn",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68",
        }
        session.get(
            url="https://search.gome.com.cn/search?question=%E4%B9%A6%E5%8C%85&searchType=goods&pos=2&sq=&search_mode=history&reWrite=true&instock=1",
            headers=head,
        )

        # with open("2.txt", "w", encoding="utf-8") as f:
        #     f.write(soup.text)
        title_ls = list()
        href_ls = list()
        id_ls = list()
        sale_ls = list()
        price_ls = list()
        items = list()
        for _ in range(10):
            soup = session.get(url=url, headers=head)
            try:
                xy = soup.json()["content"]
                if "prodInfo" in xy:
                    for i in xy["prodInfo"]["products"][:number]:
                        title_ls.append(i["alt"])
                        href_ls.append("https:" + i["sUrl"])
                        id_ls.append("G" + i["skuId"])
                        "无相关信息"
                        try:
                            price_ls.append(
                                session.get(
                                    "https://ss.gome.com.cn/search/v1/price/single/{}/{}/{}/{}/31010000/flag/item".format(
                                        i["saleOrgId"] if i["saleOrgId"] else "null",
                                        i["shopId"],
                                        i["pId"],
                                        i["skuId"],
                                    ),
                                    headers=head,
                                ).json()["result"]["price"]
                            )
                        except:
                            price_ls.append(-1)

                        try:
                            sale_ls.append(
                                eval(
                                    session.get(
                                        url="https://ss.gome.com.cn/item/v1/prdevajsonp/appraiseNew/{}/1/all/0/10/flag/appraise/all?callback=all&_=1684637980973".format(
                                            price_ls[-1]
                                        ),
                                        headers={
                                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"
                                        },
                                    ).text[4:-1]
                                )["good"]
                            )
                        except:
                            sale_ls.append(-1)
                        items.append(
                            Goods(
                                id_ls[-1],
                                "国美",
                                title_ls[-1],
                                sale_ls[-1],
                                price_ls[-1],
                                sale_ls[-1],
                                href_ls[-1],
                            )
                        )
                    return items[:number]

            except Exception as e:
                print("获取国美商品信息失败{}".format(e))
                return []
        print("国美没有搜索到商品")
        return []

    def getItemsFromJD(self, keyword, number):
        # 单个页面最多获取30个商品，销量为月销量
        url = "https://search.jd.com/Search?keyword=" + keyword
        url2 = "https://search.jd.com/Search?keyword=" + keyword + "&page=2"
        soup = bs(self.getHTMLText(url) + self.getHTMLText(url2), "html.parser")
        try:
            shopid_ls = list()
            # get_price
            price_ls = []
            for item in soup.find_all("div", class_="p-price"):
                if item.find("i"):
                    price_ls.append(item.find("i").string)
                    shopid_ls.append(item.find("i")["data-price"])
                else:
                    price_ls.append(-1)
            # get_href and id
            href_ls = []
            id_ls = []
            reg = re.compile(r"\d{5,15}")
            for item in soup.find_all("div", class_="p-name p-name-type-2"):
                if item.find("a"):
                    href = "https:" + item.find("a").get("href")
                    href_ls.append(href)
                    id = reg.findall(href)
                    if id:
                        id_ls.append("J" + id[0])
                    else:
                        id_ls.append("无相关信息")
                else:
                    href_ls.append("无相关信息")
            # get_shop_info
            shop_ls = []
            for item in soup.find_all("div", class_="p-shop"):
                if item.find("a"):
                    shop_ls.append(item.find("a").get("title"))
                elif item.find("span"):
                    shop_ls.append(item.find("span").string)
                else:
                    shop_ls.append("无相关信息")
            # get_title
            title_ls = []
            for item in soup.find_all("div", class_="p-name p-name-type-2"):
                if item.find("em"):
                    text = item.find("em").get_text()
                    text = text.replace("\n", "")
                    title_ls.append(text)
                else:
                    title_ls.append("无相关信息")
            items = []
            for num in range(len(title_ls))[:number]:
                GOOD = (
                    requests.get(
                        url="https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productCommentSummaries&referenceIds={}".format(
                            shopid_ls[num]
                        ),
                        headers={
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"
                        },
                    )
                    .json()["CommentsCount"][0]["GoodCountStr"]
                    .replace("+", "")
                )
                if "万" in GOOD:
                    GOOD = eval(GOOD.replace("万", "")) * 10000
                else:
                    GOOD = eval(GOOD)
                print(GOOD)
                goods = Goods(
                    id_ls[num],
                    "京东",
                    title_ls[num],
                    shop_ls[num],
                    price_ls[num],
                    GOOD if GOOD else "",
                    href_ls[num],
                )
                items.append(goods)
            return items[:number]
        except:
            print("获取京东商品信息失败")

    def getItemsFromPinduoduo(self, keyword, number):
        # 单个页面最多获取60个商品
        url = "http://search.dangdang.com/?key=" + keyword
        soup = bs(self.getHTMLText(url), "html.parser")
        title_ls = list()
        href_ls = list()
        id_ls = list()
        sale_ls = list()
        price_ls = list()
        items = list()
        try:
            for i in soup.find("ul", {"id": "component_59"}):
                title_ls.append(i.find("p", {"class": "name"}).text)
                href_ls.append("http:" + i.find("a", {"class": "pic"})["href"])
                id_ls.append("P" + i["id"])
                sale_ls.append("无相关信息")
                price_ls.append(
                    re.search(
                        r"\s*¥(?P<price>\d+\.*\d*)(定价)*",
                        i.find("p", {"class": "price"}).text,
                    ).group("price")
                )
                items.append(
                    Goods(
                        id_ls[-1],
                        "拼多多",
                        title_ls[-1],
                        "无相关信息",
                        float(price_ls[-1]),
                        sale_ls[-1],
                        href_ls[-1],
                    )
                )
            return items[:number]
        except:
            print("获取拼多多商品信息失败")
            return []

    # 使用这个方法需要配置好驱动器，驱动器会随代码一起发送，请保持驱动器和代码在同一文件夹下
    def seleniumGerHTML(self, url):
        firefox_opts = webdriver.ChromeOptions()
        firefox_opts.add_argument("--headless")
        # 网页驱动器地址
        service = Service("./chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=firefox_opts)
        driver.get(url)
        time.sleep(1)
        html = driver.find_element(By.XPATH, "//*").get_attribute("outerHTML")
        driver.quit()
        return html

    def getgomeItemInfo(self, goods):
        # try:
        newgoods = self.getItemsFromgome(goods.getTitle(), 1)[0]
        goods.setPrice(newgoods.getPrice())
        goods.setSales(newgoods.getSales())
        return int(newgoods.getPrice()) - int(goods.getPrice())

    # except:
    #     print('无法获取商品信息')
    #     return 0

    def getJDItemInfo(self, goods):
        soup = bs(self.seleniumGerHTML(goods.getHref()), "html.parser")
        oldprice = goods.getPrice()
        try:
            price = soup.find_all("div", class_="itemInfo-wrap")[0]
            price = price.find("span", class_="p-price")
            price = price.find("span", class_=True)
            goods.setPrice(eval(price.string))
            return eval(price.string) - oldprice
        except:
            print("无法获取商品信息")
            return 0

    def getPinduoduoItemInfo(self, goods):
        soup = bs(self.seleniumGerHTML(goods.getHref()), "html.parser")
        oldprice = goods.getPrice()
        try:
            soup = soup.find_all("div", class_="price-wrapper")[0]
            price = soup.find("span", class_="price")
            goods.setPrice(eval(price.string[1:]))
            sales = soup.find_all("p", class_=False)[1]
            goods.setSales(sales.get_text()[7:])
            return goods.getPrice() - oldprice
        except:
            print("无法获取商品信息")
            return 0


if __name__ == "__main__":
    # 测试用例
    input_keyword = "手机"
    input_number = 20
    cr = CrawlProgram()
    its = []
    its.extend(cr.getItemsFromJD(input_keyword, input_number))
    # its.extend(cr.getItemsFromgome(input_keyword, input_number))
    # its.extend(cr.getItemsFromPinduoduo(input_keyword,input_number))
    for it in its:
        print(
            it.getID(),
            it.getPlatform(),
            it.getTitle(),
            it.getShop(),
            it.getPrice(),
            it.getSales(),
            it.getHref(),
        )
