from selenium import webdriver
from lxml import etree
import re
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pymongo


class DouBanSpider(object):
    driver_path = r"C:\Downloads\driver\chromedriver.exe"#谷歌自动测试机器人的存储路径
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=DouBanSpider.driver_path)
        self.url = 'https://movie.douban.com/review/best/?start=0'#起始页面
        self.movie=[]#存储最后的数据
    def run(self):
        self.driver.get(self.url)#打开起始页面
        while True:
            WebDriverWait(driver=self.driver, timeout=10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//span[@class='next']")))#显示等待，确保页面数据加载完成
            source = self.driver.page_source#获取起始页面的源代码
            self.parse_list_page(source)#执行获取每部电影url的方法


            try:
                next_btn = self.driver.find_element_by_xpath("//div[@class='paginator']/span[@class='next']")#定位到后页
                if '<link rel="next"' not in next_btn.get_attribute("innerHTML"):#如果没有后页则不点击

                    pass
                else:
                    next_btn.click()#自动点击后页

            except:
                print(source)
            break

    def parse_list_page(self,source):#传入参数起始页面源代码
        html = etree.HTML(source)
        links = html.xpath("//a[@class='subject-img']/@href")#列表获得所有电影url
        for link in links:
            self.request_detail_page(link)#将所有电影url传入下一个函数
            time.sleep(1)
            # print(self.movie)


    def request_detail_page(self, url):
        self.driver.execute_script("window.open('%s')" % url)#在新的标签页中打开电影url
        self.driver.switch_to.window(self.driver.window_handles[1])#切换到此url
        WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//h1//span[@property='v:itemreviewed']"))
        )#等待数据加载完全
        source = self.driver.page_source#获得电影页面源代码
        self.parse_detial_page(source)#将电影页面源代码传入函数，获取电影的一些信息
        self.get_Short_commentary_url(source)#将电影页面源代码传入参数，获取电影短评的url
        self.driver.close()#关闭电影页面
        self.driver.switch_to.window(self.driver.window_handles[0])# 切换回到列表页


    def parse_detial_page(self, source):#获取电影信息的函数
        html = etree.HTML(source)
        name = html.xpath("//h1//span[@property='v:itemreviewed']/text()")
        director = html.xpath("//div[@id='info']//a/text()")[0]
        actor = html.xpath("//div[@id='info']/span[@class='actor']//a/text()")
        try:
           score = html.xpath("//div[@class='rating_self clearfix']//strong[@class='ll rating_num']/text()")[0]
        except:
            pass
        movie={
            'name':name,
            'director':director,
            'actor':actor
        }
        self.movie.append(movie)




    def get_Short_commentary_url(self,source):#获取短评页面url
        html = etree.HTML(source)
        Short_commentary_url_before=html.xpath("//div[@id='mainpic']/a/@href")[0]
        Short_commentary_url_before=Short_commentary_url_before[0:-13]
        Short_commentary_url_after = html.xpath("//div[@id='hot-comments']/a[last()]/@href")[0]
        Short_commentary_url = Short_commentary_url_before+Short_commentary_url_after
        self.request_Short_commentary_page(Short_commentary_url)

    def request_Short_commentary_page(self, url):
        self.driver.execute_script("window.open('%s')" % url)#打开短评页面
        self.driver.switch_to.window(self.driver.window_handles[2])#因为当前有列表页，电影页面和短评页面，所以这里将窗口切到2
        WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@id='wrapper']"))
        )#等待数据加载完全
        source = self.driver.page_source#获取页面源代码
        self.parse_Short_commentary_detail_page(source)#将页面源代码传入下一个函数
        self.driver.close()#关闭短评页
        self.driver.switch_to.window(self.driver.window_handles[1]) # 因为不只获取一个电影的短评，所有要切换回到电影页面，并关闭短评和电影页面
    def parse_Short_commentary_detail_page(self,source):
        html = etree.HTML(source)
        commentary_lists=html.xpath("//div[@class='mod-bd']/div[@class='comment-item']")
        for commentary_list in commentary_lists:
            author = commentary_list.xpath(".//span[@class='comment-info']/a/text()")[0]
            votes = commentary_list.xpath(".//span[@class='votes']/text()")[0]
            time = commentary_list.xpath(".//span[@class='comment-time ']/text()")[0]
            time = re.sub('\n','',time).strip()#这里是用正则去掉了\n
            short_commentary=commentary_list.xpath('.//span[@class="short"]/text()')[0]
            movie={
                "author":author,
                "votes":votes,
                "time":time,
                "short_commentary":short_commentary
            }
            self.movie.append(movie)#将字典存入全局列表中






if __name__ == '__main__':
    spyder  = DouBanSpider()
    spyder.run()
    print(spyder.movie)
    # 获取连接mongodb的对象
    # client = pymongo.MongoClient("127.0.0.1", port=27017)
    # # 获取数据库
    # db = client.douban
    # # 获取数据库中的集合
    # collection = db.commentary
    # # 存入数据库
    # collection.insert(spyder.movie)





