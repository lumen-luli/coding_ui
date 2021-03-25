#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test_check_box.py 
@time: 2021/03/24 
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
from selenium.webdriver.support.ui import Select



class TestCheckBox:
    def setup(self):
        self.driver=webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        patch = os.path.dirname(os.path.abspath(__file__))
        file_patch = 'file:///' + patch + '/check.html'
        print(file_patch)
        self.driver.get(file_patch)
        self.driver.implicitly_wait(3)


    def teardown(self):
        self.driver.quit()

    # 多选框
    def test_check_box(self):
        input=self.driver.find_element(By.CSS_SELECTOR,"input[value=bike]")
        selected=input.is_selected()
        if selected:
            print("已选中")
        else:
            input.click()
        sleep(2)

    # 单选框
    def test_radio(self):
        self.driver.find_element(By.CSS_SELECTOR,"input[value=male]").click()
        sleep(2)

    # 复选框
    def test_selected(self):
        select=Select(self.driver.find_element(By.ID,"select"))
        select.deselect_all() #取消所有选项
        sleep(1)
        select.select_by_value("conghua")
        select.select_by_index("1")
        select.deselect_by_visible_text("辣条")
        sleep(2)






