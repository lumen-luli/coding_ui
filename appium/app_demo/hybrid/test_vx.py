#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test_vx.py 
@time: 2021/01/28 
"""


from appium import webdriver
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
'''
微信小程序demo
'''

class TestWeixin():


    def setup(self):
        des_caps={
            'platformName':'android',
            'platformVersion':'6.0.1',
            'appPackage':'com.tencent.mm',
            'appActivity':"com.tencent.mm.ui.LauncherUI",
            'deviceName':'emulator-5554',
            'unicodeKeyboard':True,
            'resetKeyboard':True,
            'noReset':True,
            #指定driver地址
            #'chromedriverExecutable':'/User/panglu/Dowlonds/chromedriver'
            'showChromedriverLog':True,
            'chromeOptions':{'androidProcess':"com.tencent.mm:appbrand0"},
            'adbPort':5038

        }
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",des_caps)
        self.driver.implicitly_wait(10)

        self.driver.find_element(By.XPATH,'//*[@text="通讯录"]')

        #打开小程序
        #进入webview


        #  找VISIBLE窗口
        def find_top_window(self):
            for window in self.driver.window_handles:
                print(window)
                if ":VISIBLE" in self.driver.title:
                    print(self.driver.title)
                    return True
                else:
                    self.driver.switch_to.window(window)

            return False
