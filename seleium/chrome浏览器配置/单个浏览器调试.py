#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 单个浏览器调试.py
@time: 2021/02/18 
"""


from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
from selenium.webdriver.common.keys import Keys

'''
复用浏览器参考，要加一个options参数
'''

class TestTestDemo:
    def setup_method(self,method):

        option=Options()
        option.debugger_address="127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(3)


    def teardown(self,method):
        self.driver.quit()

    def test_demo(self):
        self.driver.get("https://www.baidu.com")
