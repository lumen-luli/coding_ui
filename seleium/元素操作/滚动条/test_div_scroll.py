#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test_div_scroll.py
@time: 2021/03/23 
"""


from time import sleep
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
滚动页面至元素可见
'''

class TestDivScroll:
    def setup(self):
        self.driver=webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        patch = os.path.dirname(os.path.abspath(__file__))
        file_patch = 'file:///' + patch + '/div_scroll.html'
        print(file_patch)
        self.driver.get(file_patch)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_scroll_1(self):
        sleep(2)
        js='document.getElementsByClassName("scroll")[0].scrollTop=10000'
        self.driver.execute_script(js)
        sleep(2)
        #document.getElementsByClassName("scroll")[0].scrollHeight  # 获取滚动条高度
        #document.getElementsByClassName("scroll")[0].scrollWidth  # 获取横向滚动条宽度
        #document.getElementsByClassName("scroll")[0].scrollLeft = xxx  # 控制横向滚动条位置