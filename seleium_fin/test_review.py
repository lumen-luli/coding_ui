#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test_review.py
@time: 2021/03/19 
"""

""" 
三方支付审核
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
js处理
execute_script:执行js
return：可以返回js的返回结果
execute_script: arguments传参
'''

class TestReview:
    def setup(self):
        self.driver=webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        self.driver.get("http://oa-test.yangqianguan.com/")
        self.driver.implicitly_wait(3)


    def teardown(self):
        self.driver.quit()

    def test_accept(self):
        self.driver.find_element_by_css_selector(".ant-modal-footer>div>button.ant-btn.ant-btn-primary").click()
        sleep(1)
        self.driver.find_element_by_css_selector(".login-type-icon.b-icon-user").click()
        sleep(1)
        self.driver.find_element_by_css_selector(".content>input").send_keys("00251")
        sleep(1)
        self.driver.find_element_by_css_selector(".toggleable-input").send_keys("1qaz@WSX")
        sleep(1)
        self.driver.find_element_by_css_selector(".block").click()
        sleep(2)
        self.driver.find_element_by_link_text("资金运营")


