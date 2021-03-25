#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test_login.py 
@time: 2021/03/23 
"""

from selenium import webdriver
import json

class TestLogin:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://oa-test.yangqianguan.com/oa/finance/capital-operation")
        cookies = self.driver.get_cookies()
        with open("cookies.txt", "w") as fp:
            json.dump(cookies, fp)
        # 登录时读取
        with open('cookies.txt', 'r') as f:
            cookies = json.loads(f.read())
        self.driver.get("https://oa-test.yangqianguan.com/oa/finance/capital-operation")
        for a in cookies:
            self.driver.add_cookie(a)
        self.driver.get("https://oa-test.yangqianguan.com/oa/finance/capital-operation")


    def teardown(self):
        self.driver.quit() #退出相关的驱动程序和关闭所有窗口
        #self.driver.close() #关闭当前窗口


    #操作浏览器
    def test_op_browser(self):
        pass