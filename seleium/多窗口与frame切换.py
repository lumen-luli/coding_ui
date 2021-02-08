#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 多窗口与frame切换.py
@time: 2021/02/08 
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

'''
多窗口处理
点击某链接，会重新打开一个窗口，这种情况，想在新页面上草最，就需要先切换窗口
获取窗口的唯一标识用句柄标识，所以只需要切换句柄，就可以在多个页面灵活操作
'''

class TestFrame:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(3)


    def teardown(self):
        self.driver.quit()

    '''
    多窗口处理流程
    1、先获取当前窗口句柄
    2、再获取所有窗口句柄
    3、判断是否想操作的橙黄口，是则操作，否则跳转到另一个窗口
    '''

    def test_bd(self):
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_link_text("立即注册").click()
        # 切换
        print(self.driver.current_window_handle) #  打印当前窗口
        print(self.driver.window_handles) #打印所有窗口

        windows=self.driver.window_handles
        self.driver.switch_to.window(windows[-1]) #切换窗口
        self.driver.find_element_by_id("TANGRAM_PSP_4_userName").send_keys("username")

        self.driver.switch_to.window(windows[0]) #切换回来

    '''
    多frame
    frame有2种，一种是嵌套的，一种是未嵌套的
    未嵌套的：
    driver.switch_to_frame("frame id")
    driver.switch_to_frame("frame index") frame无id的时候依据索引来处理，索引从0开始
    嵌套的：
    先进入到frame父节点，再进到子节点，然后可以对子节点里的对象进行处理和操作
    driver.switch_to.frame("父节点")
    driver.switch_to.frame("子节点")
    '''


