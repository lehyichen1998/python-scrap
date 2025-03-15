import time

from selenium import webdriver

browser = webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')

browser.get('https://www.baidu.com')
browser.get('https://www.taobao.com')

time.sleep(3)
browser.execute_script('window.open()')
time.sleep(3)
print(browser.page_source)
# print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
# time.sleep(3)
browser.get('https://www.taobao.com')

time.sleep(1)

browser.switch_to_window(browser.window_handles[0])

browser.get('https://python.org')