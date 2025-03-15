from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(r'D:\formatfile\Chrome\chromedriver.exe')
browser.get('https://passport.meituan.com/account/unitivelogin?service=maoyan&continue=https%3A%2F%2Fmaoyan.com%2Fpassport%2Flogin%3Fredirect%3D%252F')
