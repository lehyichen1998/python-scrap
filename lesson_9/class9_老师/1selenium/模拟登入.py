from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
browser=webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')
url='https://passport.meituan.com/account/unitivelogin?service=maoyan&continue=https%3A%2F%2Fmaoyan.com%2Fpassport%2Flogin%3Fredirect%3D%252F'
browser.get(url)
input_username=browser.find_element_by_xpath('//*[@id="login-email"]')
input_username.send_keys('17778431263')
input_password=browser.find_element_by_xpath('//*[@id="login-password"]')
input_password.send_keys('w1219534922')
submit=browser.find_element_by_xpath('//*[@id="J-normal-form"]/div[5]/input[5]')
submit.click()
print(browser.page_source)
