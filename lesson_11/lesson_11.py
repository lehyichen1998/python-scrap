from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from PIL import Image
import numpy as np
from scipy import signal
import matplotlib as plt

TEST_URL = 'https://dun.163.com/trial/sense'
driver = webdriver.Chrome(executable_path=r'D:\formatfile\Chrome\chromedriver.exe')
wait = WebDriverWait(driver, 5)
driver.get(TEST_URL)
time.sleep(1)
button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div[1]/div/div[2]/div[2]/ul/li[2]')))
button.click()
time.sleep(2)
botton = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                '/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[3]/div/div/div[1]/div[1]/span')))
botton.click()
time.sleep(2)
img = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'yidun_bg-img')))
location = img.location
size = img.size
driver.save_screenshot('snap.png')
left = location['x']
top = location['y']
right = left + size['width']
bottom = top + size['height']
img_obg = Image.open('snap.png')
crop_img = img_obg.crop((left, top, right, bottom))
crop_img.save('crop.png')

im = np.array(crop_img.convert('L'))


def fun(x, y, sigma=1):
    return 100 * (1 / (2 * np.pi * sigma)) * np.exp(-((x - 2) ** 2 + (y - 2) ** 2) / (2.0 * sigma ** 2))


g = np.fromfunction(fun, (3, 3), sigma=1)
grad = signal.convolve2d(im, g, mode="same")
plt.figure(grad)
plt.show()
f = np.array([[-1, 0, 1],
              [-2, 0, 2],
              [-1, 0, 1]])

grad = signal.convolve2d(im, f, boundary='symm', mode="same")
