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
        sleep(3)
        #self.driver.find_element(By.CSS_SELECTOR,"#app > div > div > section > aside > div > div:nth-child(2) > ul > li:nth-child(2) > div > span > span:nth-child(2)").click()
        #sleep(2)
        #self.driver.find_element(By.CSS_SELECTOR,"#app > div > div > section > aside > div > div:nth-child(2) > ul > li:nth-child(3) > div > span > span").click()
        #sleep(2)
        #self.driver.find_element(By.CSS_SELECTOR,"#app > div > div > section > aside > div > div:nth-child(2) > ul > li:nth-child(3) > div > span > span")
        # js='document.querySelector(".ant-layout-sider-children>div:last-child").scrollTop=10000'
        # self.driver.execute_script(js)
        #self.driver.find_element(By.CSS_SELECTOR,".ant-layout-sider-children>div:last-child").send_keys(Keys.DOWN)
        #sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,"#app > div > div > section > aside > div > div:nth-child(2) > ul > li:nth-child(4) > div > span > span:nth-child(2)").click()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,"#账务管理\$Menu > li:nth-child(6) > a").click()
        sleep(1)
        self.driver.find_elements_by_class_name("ant-select-selection-search-input").send_keys("三方")
        sleep(3)




