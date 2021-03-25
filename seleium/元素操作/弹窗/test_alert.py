#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test_alert.py 
@time: 2021/03/19 
"""
from time import sleep
import os
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
from selenium.webdriver.common.keys import Keys



class TestReview:
    def setup(self):
        self.driver=webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        patch = os.path.dirname(os.path.abspath(__file__))
        file_patch = 'file:///' + patch + '/alert.html'
        print(file_patch)
        self.driver.get(file_patch)
        self.driver.implicitly_wait(3)


    def teardown(self):
        self.driver.quit()

    def test_alert(self):
        """点击alert弹框的处理方法"""
        self.driver.find_element_by_id("alert").click()
        sleep(1)
        alert=self.driver.switch_to.alert
        print(alert.text)
        sleep(3)
        alert.accept()

    def test_confirm(self):
        """处理confirm方法"""
        self.driver.find_element_by_id('confirm').click()
        sleep(1)
        # 切换到confirm
        confirm = self.driver.switch_to.alert
        print(confirm.text)
        sleep(1)
        # 点击确定按钮
        # confirm.accept()
        # 点击取消按钮
        confirm.dismiss()
        sleep(3)

    def test_prompt(self):
        # 处理prompt方法
        self.driver.find_element_by_id('prompt').click()
        sleep(1)
        # 切换弹窗
        prompt = self.driver.switch_to.alert
        #返回弹窗文本内容
        print(prompt.text)
        #弹窗输入文字
        prompt.send_keys("222")
        sleep(1)
        prompt.accept()
        sleep(3)






