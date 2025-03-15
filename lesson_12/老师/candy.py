from chaojiying_Python.chaojiying import Chaojiying_Client
import random
import time
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

CHAOJIYING_NAME = '1219534922'  # 超级鹰账号
CHAOJIYING_PWD = 'w505377017'  # 超级鹰密码
CHAOJIYING_ID = 905045  # 软件ID
CHAOJIYING_KIND = 9103  # 验证码类型


class YYVerification(object):
    """
      此类用于YY的验证码识别，可以应用到类似的验证码识别上，这种验证码类型是
     点击类验证码.这里我们是对接超级鹰平台。
      """

    def __init__(self):
        self.url = 'https://aq.yy.com/p/reg/account.do?appid=&url=&fromadv=udbclsd_r'
        self.driver = webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')
        self.chaojiying = Chaojiying_Client(CHAOJIYING_NAME, CHAOJIYING_PWD, CHAOJIYING_ID)

    # @property
    # def __del__(self):
    #     self.driver.close()

    def screen_shot(self):
        """
        网页截屏
         :return: bool值
        """
        # self.driver.maximize_window()
        time.sleep(2)

    # # 用于网页的向下滚动
    # js = 'var q=document.documentElement.scrollTop=300'
    # self.driver.execute_script(js)
    # time.sleep(1)
        self.driver.save_screenshot('yy.png')
        return True


    def i_url(self):
        """
        实现对iframe标签的url请求，并定位新网页
        :return: 定位对象
         """
        i = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/iframe')


        url_1 = i.get_attribute('src')
        print(url_1)
        self.driver.get(url_1)
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="mPickWords"]/div[1]')))
        return element


    def shear_location(self):
        """
        计算对截屏剪切的坐标，注意这里不同电脑可能会修改start_x到end_y
         后边添加的数是根据作者的电脑优化的
         :return: 返回坐标以及网页剪切定位的对象
        """
        time.sleep(random.random() + 1)
        print('正在获取div')


        div = self.i_url()
        start_x = div.location['x']
        start_y = div.location['y']
        end_x = div.location['x']+20
        end_y = div.location['y']+20
        result = (start_x, start_y, end_x, end_y)
        print(result)
        return result, div


    @staticmethod
    def shear_image(axis):
        im = Image.open('yy.png')
        new_image = im.crop(axis)


        new_image.save('new_img.png')
        return new_image


    def upload_picture(self, img):
        """
        上传图片(Byte)，返回点击的坐标。这里对返回的坐标进行了处理，
       处理过程可以看成 shear_location 函数的坐标数据逆处理过程
         :param img: 上传的图片
        :return: 点击坐标
        """
        image = img
        byte_array = BytesIO()
        image.save(byte_array, format('PNG'))
        # 提交图片


        result = self.chaojiying.PostPic(byte_array.getvalue(), CHAOJIYING_KIND)
        print(result)
        if '无可用题分' in result['err_str']:
            print('题分已经不足请充值')
            raise ValueError
        pic_str = result['pic_str']
        pic_list = [[i for i in x.split(',')] for x in pic_str.split('|')]
        for i in pic_list:
            i[0] = int(int(i[0]) * (282 / 354))
            i[1] = int(int(i[1]) * (219 / 274))
        print(pic_list)
        return pic_list


    def click_now(self, coordinates, axis, element):
        """
         这里如果验证失败会进行回调，实现验证码的自动验证。
         :param coordinates: 点击坐标
         :param axis: 剪切坐标
          :param element: 剪切位置的定位
          :return: 返回点击的成功信息
         """
        print('点击开始')


        print(coordinates)
        for location in coordinates:
            ActionChains(self.driver).move_to_element_with_offset(element, location[0], location[1]).click().perform()
        time.sleep(random.random() + 1.8)
        submission = self.driver.find_element_by_xpath('//*[@id="mPickWords"]/div[2]/span[4]')
        submission.click()
        time.sleep(1)
        if 'pw_submit_disabled' in submission.get_attribute('class'):
            return '点击成功'
        else:
            time.sleep(2)
        print('正在重新识别新的验证码')
        self.revalidation(axis, element)
        return '点击成功'


    def revalidation(self, axis, element):
        """
        网页跳转之后，执行验证的主程序
       :param axis: 剪切坐标
         :param element: 剪切位置的定位对象
        :return: 验证成果
        """
        self.screen_shot()


        if not self.screen_shot():
            return '截图失败'
        time.sleep(1)
        # 剪切图片
        new_image = self.shear_image(axis)
        new_image.show()
        # 上传图片并返回点击坐标
        click_coordinates = self.upload_picture(new_image)
        # 点击验证码
        print(self.click_now(click_coordinates, axis, element))
        return '点击验证结束'


    def main(self):
        self.driver.get(self.url)


        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/iframe')))
        axis, element = self.shear_location()
        self.revalidation(axis, element)

if __name__ == '__main__':
    yy = YYVerification()
    yy.main()
