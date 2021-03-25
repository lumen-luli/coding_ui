#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: simple_op.py 
@time: 2021/03/22 
"""

from time import sleep
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

'''

'''

class TestLocate:
    def setup(self):
        self.driver=webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_op(self):
        self.driver.get("https://www.baidu.com/")
        kw=self.driver.find_element(By.ID,"kw")
        kw.send_keys("测试")
        sleep(1)
        kw.clear()
        sleep(2)

    def test_roll(self):
        self.driver.get("https://www.runoob.com/cssref/css-selectors.html")
        ele =self.driver.find_element_by_link_text("animation-fill-mode").location_once_scrolled_into_view
        print(ele)
        # ele.click()
        # sleep(2)
        #self.driver.find_element_by_link_text('合作招商').location_once_scrolled_into_view


