#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test_select.py 
@time: 2021/03/22 
"""

'''
下拉框一般会遇到两种，一种是一种使用的是html的标签select，另一种是使用input标签做的假下拉框。
'''

from time import sleep
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

'''
滚动页面至元素可见
'''

class TestSelect:
    def setup(self):
        self.driver=webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        patch = os.path.dirname(os.path.abspath(__file__))
        file_patch = 'file:///' + patch + '/test_select.html'
        self.driver.get(file_patch)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    # 定位<select>类型下拉框
    def test_select(self):
        s1=Select(self.driver.find_element_by_id("s1Id"))
        #三种选择方法，1、通过顺序，index从0开始 2、通过value属性 3、通过选项可见文本
        s1.select_by_index("1")
        sleep(1)
        s1.select_by_value("two")
        sleep(1)
        s1.deselect_by_visible_text("three")
        sleep(1)


    # 定位非<select>标签的下拉菜单，如input，ul
    def test_input_select(self):
        # 1、先定位到下拉菜单 2、在对下拉菜单中的选项进行选择
        ele = self.driver.find_element_by_id("gender")
        ele.find_element_by_id("nv").click()
        sleep(3)

    # 输入检索式选择框
    def test_search_select(self):
        # 1、定位输入框输入关键字 2、定位检索出来的选择列表 3、定位相应的值
        self.driver.find_element_by_id("food").send_keys(1)
        sleep(1)
        ele = self.driver.find_element_by_id("foodlist")
        ops = ele.find_elements_by_tag_name("option")
        for op in ops:
            if op == "1":
                op.click()
        sleep(2)
