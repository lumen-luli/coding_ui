#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test_touch_action.py 
@time: 2021/03/24 
"""

from time import sleep
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.touch_actions import TouchActions


'''
类似于ActionChains，主要针对h5页面手势操作，比如滑动、长按、拖动等
'''

class TestTouchAction:
    def setup(self):
        options=webdriver.ChromeOptions()
        #设置手机模式
        options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone X'}) #设备可以右键-检查-setting-devices查看
        #打开开发者模式
        #options.add_argument("--auto-open-devtools-for-tabs")
        self.driver=webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',options=options)

        self.driver.get("https://www.baidu.com")
        #self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    #指定设备
    # def setup(self):
    #     options = webdriver.ChromeOptions()
    #     options.add_experimental_option("mobileEmulation",
    #             {"deviceMetrics": {"width": 320, #设备宽度
    #                                 "height": 640, #设备高度
    #                                 "piexelRatio": 3.0, #浏览器密度
    #                                 "userAgent": "Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3"
    #                         }
    #             })
    #
    #     self.driver = webdriver.Chrome(options=options)
    #     self.driver.get("http://m.baidu.com")


    def teardown(self):
        self.driver.quit()

    def test_action(self):
        #设置成手机模式，无法识别元素可以获取绝对坐标值，模拟鼠标点击
        pass