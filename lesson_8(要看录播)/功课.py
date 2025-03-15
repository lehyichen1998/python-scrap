from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

option = webdriver.ChromeOptions()
option.add_argument("--user-data-dir=" + r"C:/Users/javac/AppData?Local/Google/Chrome/User Data/")
browser = webdriver.Chrome(chrome_options=option, executable_path=r'D:\formatfile\Chrome\chromedriver.exe')

browser.get('http://www.youtube.com/')

search = browser.find_element_by_id('search')
search.send_keys('王力宏')
search.send_keys(Keys.ENTER)

wait = WebDriverWait(browser, 20)
wait.until(
    EC.presence_of_element_located((By.XPATH, '//h3[@class="title-and-badge style-scope ytd-video-renderer"]/a')))
html = browser.find_element_by_id('html')

for i in range(2):
    wait = WebDriverWait(browser, 10)
    html.send_keys(Keys.PAGE_DOWN)
title = browser.find_element_by_xpath('//h3[@class="title-and-badge style-scope ytd-video-renderer"]/a')

with open('王力宏.csv', 'w', encoding='utf-8', newline='')as f:
    writer = csv.writer(f)
    writer.writerow(['title', 'youtube link'])
    for i in title:
        writer.writerow([i.get_attribute('title'), i.get_attribute('href')])

print(browser.page_source)
browser.close()
