from selenium import webdriver
browser = webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')