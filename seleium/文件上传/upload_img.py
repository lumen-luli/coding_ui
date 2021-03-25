#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: upload_img.py 
@time: 2021/03/24 
"""

from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
from selenium.webdriver.common.keys import Keys


class TestFileUpload:
    def setup(self):
        self.driver=webdriver.Chrome()

        self.driver.implicitly_wait(3)


    def teardown(self):
        self.driver.quit()

    def test_img_upload(self):
        #  input标签可以直接使用send_keys(文件地址)上传文件
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element(By.ID,"uploadImg")
        self.driver.find_element_by_id("stfile").send_keys("/Users/panglu/Desktop/京东web登录.png")
        sleep(3)


