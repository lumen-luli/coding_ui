#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test_op_browser.py
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




class TestOpBrowser:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit() #退出相关的驱动程序和关闭所有窗口
        #self.driver.close() #关闭当前窗口

    #操作浏览器
    def test_op_browser(self):
        self.driver.maximize_window() #全屏
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("测试")
        self.driver.find_element(By.CSS_SELECTOR, '[id=su]').click()
        sleep(2)
        self.driver.back()  #后退
        sleep(2)
        self.driver.refresh() #刷新
        sleep(2)
        self.driver.forward() #前进
        sleep(2)
        self.driver.close() #关闭