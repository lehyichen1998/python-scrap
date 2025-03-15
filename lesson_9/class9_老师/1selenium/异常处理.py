#错误
# from selenium import webdriver
# browser = webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')
# browser.get('https://www.baidu.com')
# browser.find_element_by_id('hello')

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
browser = webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()