#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test_scroll.py
@time: 2021/03/22 
"""

from time import sleep
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
滚动页面至元素可见
'''

class TestScroll:
    def setup(self):
        self.driver=webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        self.driver.get("https://www.runoob.com/cssref/css-selectors.html")
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_scroll_1(self):
        # 固定滚动
        '''
        window.scrollBy(0,500)　　   向下滚动500个像素
        window.scrollBy(0,-500)　　 向上滚动500个像素
        window.scrollBy(500,0)　　   向右滚动500个像素
        window.scrollBy(-500,0)　　 向左滚动500个像素
        在console中可模拟
        '''
        self.driver.execute_script('window.scrollBy(0,500)')
        sleep(1)
        self.driver.find_element_by_link_text("animation-fill-mode").click()
        sleep(2)


    def test_scroll_2(self):
        # 滚动至元素可见
        # scrollIntoView()参数为bool，如果为true，元素的顶端将和其所在滚动区的可视区域的顶端对齐，如果为false，元素的底端将和其所在滚动区的可视区域的底端对齐
        ele = self.driver.find_element_by_link_text("animation-fill-mode")
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        sleep(1)
        ele.click()
        sleep(2)


    def test_scroll_3(self):
        # 源码中，也是调用了js语句：arguments[0].scrollIntoView(true),默认与浏览器网页的可视区域顶部对齐
        ele =self.driver.find_element_by_link_text("animation-fill-mode")
        ele.location_once_scrolled_into_view
        sleep(1)
        ele.click()
        print(ele)
        sleep(2)
