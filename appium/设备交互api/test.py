#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test.py 
@time: 2021/01/28 
"""

from appium import webdriver
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions





class TestHybrid():
    def setup(self):
        des_caps={
            'platformName':'android',
            'platformVersion':'6.0.1',
            'appPackage':'com.lingyue.YqgAndroidTest',
            'appActivity':"com.lingyue.yqg.yqg.activities.MainPageActivity",
            'deviceName':'emulator-5554',
            'noReset':True

            #指定driver地址
            #'chromedriverExecutable':'/User/panglu/Dowlonds/chromedriver'

        }
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",des_caps)
        self.driver.implicitly_wait(10)




    def teardown(self):
        self.driver.quit()

    def test_mobile(self):
        #0无网络 1飞行模式 2仅wifi 4仅数据 6所有网络
        self.driver.set_network_connection(0)
        #打电话
        self.driver.make_gsm_call('13812341234', GsmCallActions.CALL)
        # 发短信
        self.driver.send_sms("13812341234","hello")

