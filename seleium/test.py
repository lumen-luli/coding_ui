#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test.py 
@time: 2021/02/03 
"""
import selenium
from selenium import webdriver

def test_seleium():
    driver=webdriver.Chrome()
    driver.get("https://www.baidu.com")



