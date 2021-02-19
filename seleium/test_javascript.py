#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test_javascript.py 
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
js处理
execute_script:执行js
return：可以返回js的返回结果
execute_script: arguments传参
'''

class TestJs:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(3)


    def teardown(self):
        self.driver.quit()

    def test_js_scroll(self):
        self.driver.find_element_by_id("kw").send_keys("测试seleium")
        ele=self.driver.execute_script("return document.getElementById('su')")
        ele.click()
        sleep(3)
        self.driver.execute_script("document.documentElement.scrollTop=1000")
        sleep(3)
        for code in[
            'return document.title','return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))