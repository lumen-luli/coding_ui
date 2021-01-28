#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test_web_app.py
@time: 2021/01/26 
"""
'''
安卓纯web页面app示例
'''

from appium import webdriver
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowers():
    def setup(self):
        des_caps={
            'platformName':'android',
            'platformVersion':'6.0.1',
            'browserName':'Browser',
            'noReset':True,
            'deviceName':'emulator-5554',
            #指定driver地址
            #'chromedriverExecutable':'/User/panglu/Dowlonds/chromedriver'

        }
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",des_caps)
        self.driver.implicitly_wait(10)


    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        self.driver.find_element_by_id("index-kw")
        self.driver.find_element_by_id("index-kw").send_keys("appium")
        search_locator=(By.ID,"index_bn")
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(search_locator))
        self.driver.find_element_by_id(*search_locator).click()
        sleep(5)
