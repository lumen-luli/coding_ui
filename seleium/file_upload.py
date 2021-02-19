#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: file_upload.py 
@time: 2021/02/18 
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

class TestFileUpload:
    def setup(self):
        self.driver=webdriver.Chrome()

        self.driver.implicitly_wait(3)


    def teardown(self):
        self.driver.quit()

    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_id("stfile").send_keys("/User/pang/Desktop/test.img")
        sleep(3)


    #弹框：div，alert，window
    #switch_to.alert()
    def test_alert(self):
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()





