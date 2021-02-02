#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 滑动操作.py 
@time: 2021/02/01 
"""


from appium import webdriver
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions





class TestHuadong():
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

    '''
    swipe
    '''
    def get_size(self):
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return x,y
    def swipe_up(self,t):
        screen=self.driver.get_window_size()
        self.driver.swipe(screen[0]*0.5,screen[1]*0.75,screen[0]*0.5,screen[1]*0.25,t)

    def swipe_down(self,t):
        screen=self.get_size()
        self.driver.swipe(screen[0]*0.5,screen[1]*0.25,screen[0]*0.5,screen[1]*0.75,t)

    def swipe_left(self,t):
        screen=self.get_size()
        self.driver.swipe(screen[0]*0.75,screen[1]*0.5,screen[0]*0.25,screen[1]*0.5,t)
    def swipe_right(self,t):
        screen=self.get_size()
        self.driver.swipe(screen[0]*0.25,screen[1]*0.5,screen[0]*0.75,screen[1]*0.5,t)

    '''
    scroll
    '''