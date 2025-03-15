from selenium import webdriver
from lxml import etree
import re
import timeit
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class DouBanSpider(object):
    def __init__(self):
        self.driver = webdriver.Chrome(r'D:\formatfile\Chrome\chromedriver.exe')
        self.url = 'https://movie.douban.com/review/best/?start=0'
        self.movie = []

    def run(self):
        self.driver.get(self.url)
        wait = WebDriverWait(driver=self.driver, timeout=10)
        wait.until(
            EC.presence_of_element_located((By.XPATH, 'span[@class="next"]'))
        )
        source = self.driver.page_source

    def parse_list_page(self, source):
        html = etree.HTML(source)
        links = html.xpath('//a[class="subject-img"]/@href')
        for link in links:
            self.request_detail_page(link)
            time.sleep(1)

    def request_detail_page(self, url):
        self.driver.execute_script("window.open('%s')") % url
        # self.driver.execute_script("window.open()")
        # self.driver.get(url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/h1/span[1]'))
        )
        source = self.driver.page_source
        self.parse_detail_pace(source)
        self.driver.close()
        self.driver.switch_to(self.driver.window_handles[0])

    def parse_detail_pace(self, source):
        html = etree.HTML(source)
        name = html.xpath("//h1/span[@property='v:itemreviewed']/text()")
        actor = html.xpath("//span[@class='actor']//a/text()")
        director = html.xpath("//div[@id='info']//a/text()")[0]
        try:
            score = html.xpath("//*[@id='interest-sectl']/div[1]/div[2]/strong/text()")[0]
        except:
            pass

        movie = {
            'name': name,
            'directoe': director,
            'actor': actor
        }
        self.movie.append(movie)

    def get_Short_commentary_url(self, source):
        html = etree.HTML(source)
        Short_commentary_url = html.xpath('//*[@id="comment-section"]/div[1]/h2/span/a')
        self.request_Short_commentary_url(Short_commentary_url)

    def request_Short_commentary_url(self, url):
        self.driver.execute_script("window.open('%s')") % url
        # self.driver.execute_script("window.open()")
        # self.driver.get(url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/h1/span[1]'))
        )
        source = self.driver.page_source
        self.parse_Short_commentary_detail_page(source)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def parse_Short_commentary_detail_page(self, source):
        html = etree.HTML(source)
        commentary_lists = html.xpath("//div[@class='mod-bd'/div[@class='comment-item']]")
        for commentary_list in commentary_lists:
            author = commentary_list.xpath(".span[@class='comment-info']/a/text()")[0]
            vote = commentary_list.xpath(".span[@class='vote vote-count']/text()")[0]
            time = commentary_list.xpath(".span[@class='comment-time']/text()")[0]
            short_commentary = commentary_list.xpath(".span[@class='short']/text()")[0]
            movie = {
                "author": author,
                "vote": vote,
                "time": time,
                "short_commentary": short_commentary
            }
            self.movie.append(movie)