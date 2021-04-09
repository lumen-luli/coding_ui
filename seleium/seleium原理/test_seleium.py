#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test_seleium.py 
@time: 2021/03/25 
"""

'''
在这个过程中，Python 解释器就相当于客户端，WebDriver 会先将你写的操作代码（如 find_element, click等）封装成 HTTP 请求发送给浏览器驱动生成的远程服务，
再由浏览器驱动将请求内容转化为浏览器内置的自动化命令来具体对浏览器实现操作。
'''


import datetime
a=datetime.datetime.today()

import os
import logging
logging.basicConfig(level=logging.DEBUG,filename=os.path.join(os.getcwd(),a.strftime('%Y-%m-%d %H:%M:%S')+'.log'))
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_id('kw').send_keys('测试')