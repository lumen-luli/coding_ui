#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 等待.py 
@time: 2021/02/03 
"""
from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions




'''
直接等待:sleep(3)
隐式等待:
设置一个等待时间，轮询查找元素是否出现,没有出现就抛出异常.作用于所有的 find element 方法
self.driver.implicitly_wait(3)
显示等待:
在代码中定义等待条件，条件发生时继续执行代码
WebDriverWait配合until() 、until_not()方法
'''

class TestWait:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(3)

    def test_wait(self):
        #sleep(3)
        #print("hello")
        self.driver.find_element(By.XPATH,"元素的定位").click()
        def wait(x):
            return len(self.driver.find_elements(By.XPATH,"元素")) >=1
        #python 传参不要写括号，wait()是调用
        WebDriverWait(self.driver,10).until(wait)

        # 使用内置条件
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '元素')))


