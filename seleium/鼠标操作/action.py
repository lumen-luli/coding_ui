#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: action.py 
@time: 2021/03/24 
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
通过 ActionChains 的对象生成操作队列，在没有执行提交 perform() 之前，所有操作只是暂存于队列中，不会实际在页面上操作，需要执行 perform() 时才会实际执行操作。
ActionChains 只是针对PC端程序鼠标模拟的一系列操作对H5页面操作时无效，TouchAction可以对移动端页面自动化操作
'''

class TestAction:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_b693a7e0c79347089e1483e9966e3225")
        self.driver.implicitly_wait(3)


    def teardown(self):
        self.driver.quit()

    def test_action_move(self):
        e=self.driver.find_element_by_link_text("家用电器")
        #鼠标悬停
        ActionChains(self.driver).move_to_element(e).pause(0.3).perform()
        sleep(3)
        ActionChains(self.driver).move_to_element(e).perform() # 鼠标移动到指定元素
        ActionChains(self.driver).move_by_offset(100, 100).perform() # 鼠标移动坐标
        ActionChains(self.driver).move_to_element_with_offset(e, 100, 100).perform() #移动到指定坐标

    def test_action_click(self):
        e = self.driver.find_element_by_link_text("家用电器")
        ActionChains(self.driver).click(e).perform() #鼠标点击
        ActionChains(self.driver).double_click(e).perform() #鼠标双击
        ActionChains(self.driver).context_click(e).perform() #鼠标右击
        ActionChains(self.driver).click_and_hold(e).perform() #鼠标按住不放

    def test_action_drag(self):
        # 将元素1拖拽到元素2然后松开
        el1 = self.driver.find_element_by_id("元素1")
        el2 = self.driver.find_element_by_id("元素2")
        action = ActionChains(self.driver)
        action.drag_and_drop(el1, el2).perform()
        #  将元素1拖拽到某个坐标然后松开
        ActionChains(self.driver).drag_and_drop_by_offset(el1, -100, -100).perform()

    def test_action_key(self):
        #向指定元素发送按键
        e = self.driver.find_element_by_id('kw')
        ActionChains(self.driver).send_keys_to_element(e, '测试').perform()
        #在当前焦点元素发送按键
        ActionChains(self.driver).send_keys('手机').perform()
        #key_down(value, element=None)按下一个特殊按键只能用于Ctrl， Alt，Shif键，注意此时按键只是按下并没有松开，用于进行按键组合操作，如Ctrl + A。
        #key_up（ value, element = None) 释放一个按下的键与key_down()配套使用，用于释放一个已按下的按键，只能用于Ctrl， Alt，Shift键
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()


'''
队列操作
1. perform() 提交队列中的所有操作
所有操作都需要通过 perform() 才会实际提交到浏览器。

2. rest_actions() 清空队列中的操作
将队列中已存储的操作清空。

3. pause(seconds) 暂停所有动作
相当于等待，用于链式操作过程中的等待。

4. release(on_element=None) 松开按下的鼠标
如果有鼠标按下的操作，那么需要通过 release() 释放鼠标。
'''
