from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(r'D:\formatfile\Chrome\chromedriver.exe')
browser.get('https://www.baidu.com/')
input = browser.find_element_by_id('kw')
input.send_keys('python')
input.send_keys(Keys.ENTER)

# submit = browser.find_element_by_xpath('//input[@class="bg s_btn"]')
submit = browser.find_element_by_xpath('//*[@id="su"]')
# submit = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div/div/form/span[2]/input')
submit.click()
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.ID, '3002')))

response = browser.page_source
input.click()
input.send_keys('电影')
submit.click()
# link = browser.find_element_by_xpath((By.XPATH,'//*[@id="3"]/h3/a')))
print(response)
# browser.close()
