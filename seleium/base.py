#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: base.py
@time: 2021/02/08 
"""
import os

'''
多浏览器
'''
from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
from selenium.webdriver.common.keys import Keys

'''
多窗口处理
点击某链接，会重新打开一个窗口，这种情况，想在新页面上草最，就需要先切换窗口
获取窗口的唯一标识用句柄标识，所以只需要切换句柄，就可以在多个页面灵活操作
'''

class Base:
    def setup(self):
        browser = os.getenv("browser")
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "headless":
            self.driver=webdriver.PhantomJS()
        else:
            self.driver=webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(3)


    def teardown(self):
        self.driver.quit()