#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 控件交互.py
@time: 2021/02/05 
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




class TestAct:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(3)

    # seleium webdriverapi:https://selenium-python-zh.readthedocs.io/en/latest/api.html

    #ActionChans
    #模拟点击、右键、双击


    def teardown(self):
        self.driver.quit() #退出相关的驱动程序和关闭所有窗口
        #self.driver.close() #关闭当前窗口


    #操作浏览器
    def test_op_browser(self):
        self.driver.maximize_window() #全屏
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("测试")
        self.driver.find_element(By.CSS_SELECTOR, '[id=su]').click()
        sleep(2)
        self.driver.back()  #后退
        sleep(2)
        self.driver.refresh() #刷新
        sleep(2)
        self.driver.forward() #前进
        sleep(2)
        self.driver.close() #关闭

    #简单元素操作
    def test_op_element(self):
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("测试")
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').clear()  #清除输入内容

    #鼠标事件
    def test_mouse(self):
        el= self.driver.find_element_by_css_selector('input[name=wd]')
        action=ActionChains(self.driver)
        action.context_click(el) #右键
        action.move_to_element(el)  #悬停
        action.double_click(el) #双击
        action.perform()

        #action = ActionChains(self.driver).click(el).context_click(el).double_click(el).perform()
    #将光标移动到某个元素
    def test_move_eo_el(self):
        self.driver.maximize_window()
        el=self.driver.find_element_by_link_text("设置")
        action = ActionChains(self.driver)
        action.move_to_element(el)
        action.perform()

    #拖拽
    def test_dragdrop(self):
        #将元素1拖拽到元素2
        el1=self.driver.find_element_by_id("元素1")
        el2=self.driver.find_element_by_id("元素2")
        action = ActionChains(self.driver)
        action.drag_and_drop(el1,el2).perform()

        #action.click_and_hold(el1).release(el2).perform()

    #actionChains模拟按键
    def test_act_keys(self):
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').click()
        action = ActionChains(self.driver)

        action.send_keys("testt").send_keys(Keys.BACK_SPACE)
        #action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
        action.perform()
        sleep(3)

    # TouchAction 对h5页面操作
    #https://www.pianshen.com/article/2179418201/

    #键盘事件
    def test_keys(self):
        self.driver.find_element_by_css_selector('input[name=wd]').send_keys('seleniumm')  # 输入框输入内容
        self.driver.find_element_by_css_selector('input[name=wd]').send_keys(Keys.BACK_SPACE)  # 删除多输入的一个m

        sleep(2)
        self.driver.find_element_by_id('su').send_keys(Keys.ENTER)  # 通过回车键来代替单击操作



    # 截取当前页面
    def test_screen_shot(self):
        self.driver.get_screenshot_as_file('d.png')



