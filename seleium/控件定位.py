#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 控件定位.py
@time: 2021/02/05 
"""
from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



class TestLocator:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(3)
    # 定位 Xpath， css_selector
    '''
    xpath:xml path language(速度慢，从头到尾遍历，可用于appium，seleium)
    / 代表子元素  //代表所有子孙元素  . 选取当前节点  .. 选取当前节点的父节点 @ 选取属性
    表达式  结果
    /books/book[1] 选取books子元素的第一个book元素
    /books/book[last()] 选取books子元素的最后一个book元素
    /books/book[last()-1]  选取books子元素的倒数第二个book元素
    /books/book[position()<3] 选取最前面的两个属于books元素的子元素的book属性
    //title[@lang='eng]  选取所有title冤死，切这些元素拥有职位eng的lang属性
    /books/book[price>35]  选取books所有books元素，且其中的price必须大于35
    /books/book[price>35]/title  选取books元素在book元素的所有title，且book的price必须大于35
    
    在console中用 $x('//*[@id="s_tab"]//a[0]')  
    '''

    '''
    css_selector:不能用于appium，应用里面嵌套的网页可以，比xpath快
    在console中用 $('[id=kw]')
    '''



    # 点击与输入
    def test_click_and_input(self):
        #self.driver.find_element(By.ID,'kw').send_keys("测试")
        #self.driver.find_element(By.ID,'su').click()

        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("测试")
        self.driver.find_element(By.CSS_SELECTOR, '[id=su]').click()
