#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test_screenshot.py 
@time: 2021/03/23 
"""
'''
UI 自动化中截图必不可少，截图可以展现测试过程 ，也可以检查错误情况。甚至在某种情况下还可以通过截图对比来判断程序的正确性。

自动化测试过程中 ，需要截图有以下几个用途：
记录测试过程
脚本发生异常或者失败情况时截图
部分页面需要截图对比断言
获取验证码图片用于验证码识别

Selenium 中提供的截图有两种截图方式。一种是截取当前浏览器窗口，第二种是截取可见元素。
'''


from time import sleep
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestScreenshot:
    def setup(self):
        self.driver=webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        patch = os.path.dirname(os.path.abspath(__file__))
        file_patch = 'file:///' + patch + '/screenshot.html'
        self.driver.get(file_patch)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    # 截取当前浏览器窗口
    def test_screen(self):
        # 必须保存为 png 格式的图片,窗口截取时，只会截取当前能看到的窗口，如果看不到的部分是不会截图的。
        self.driver.get_screenshot_as_file("test.png")
        self.driver.save_screenshot("test.png")   #底层是调用get_screenshot_as_file
        #保存为base64位字符串,可以直接将图像直接写入 HTML 页面中。可以用于将图像放入测试报告
        self.driver.get_screenshot_as_base64()
        #  保存为二进制数据
        self.driver.get_screenshot_as_png()

    # 截取可见元素
    def test_screen_enable(self):
        self.driver.find_element_by_id("canvas").screenshot('验证码.png')
        # 返回二进制或者 base64 格式
        self.driver.find_element_by_id('canvas').screenshot_as_png()  # => 保存为二进制格式
        self.driver.find_element_by_id('canvas').screenshot_as_base64()  # => 保存为 base64
