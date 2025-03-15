from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
browser=webdriver.Chrome()
browser.get('https://www.baidu.com/')
input=browser.find_element_by_id('kw')
input.send_keys('python')
# input.send_keys(Keys.ENTER)
submit=browser.find_element_by_xpath('//*[@id="su"]')
submit.click()
wait=WebDriverWait(browser,10)
wait.until(EC.presence_of_element_located((By.ID,'3002')))
# response=browser.page_source
# print(response)
input.clear()
input.send_keys('电影')
submit.click()
wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[3]/div[1]/div[3]/div[2]/h3/a')))
link=browser.find_elements_by_xpath('//h3[@class="t"]/a')
texts=browser.find_elements_by_xpath('//td[@class="toplist1-td opr-toplist1-link"]/a')
# time.sleep(1)
# browser.back()
# time.sleep(1)
# browser.forward()
browser.add_cookie()
print(browser.get_cookies())
# for i in link:
#     print(i.get_attribute('href'))
# for texta  in texts:
#     print(texta.text)