#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test_hybrid_app.py 
@time: 2021/01/27 
"""
'''
安卓混合应用app示例
'''

from appium import webdriver
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support.wait import WebDriverWait


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

    def test_webview(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="我的"]').click()
        sleep(2)
        cash_back_locator = (MobileBy.XPATH,'//*[@text="邀友返现"]')
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(cash_back_locator))
        self.driver.find_element(*cash_back_locator).click()
        print(self.driver.contexts)
        #切换到h5
        self.driver.switch_to.context(self.driver.contexts[-1])
        #invite_locator = (MobileBy.XPATH,'//*[@text="当面邀请"]')
        invite_locator=(MobileBy.XPATH,'//*[@id="app"]/div[1]/div/div/div/div/div/div[3]/div[2]/span')
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(invite_locator))
        self.driver.find_element(*invite_locator).click()
        #操作
        # self.driver.switch_to.context(None)回到原生应用
        #print(self.driver.page_source)


        # print(self.driver.window_handles)
        # self.driver.switch_to.window()

        #根据content-desc,会有兼容问题
        #self.driver.find_element(MobileBy.ACXESSIBILITY_ID,'i has no focus').send_keys("this is a test")
        #print(self.driver.page_source)
