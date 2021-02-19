#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 屏蔽浏览器检测框.py 
@time: 2021/02/19 
"""


'''
其他配置
https://sites.google.com/a/chromium.org/chromedriver/capabilities
浏览器检测框，就是我们在启动selenium的时候，看到一条地址栏下面存在一个弹框：Chrome正在受到自动测试软件的控制。
将"excludeSwitches", ['enable-automation'] 配置到浏览器中。
'''

from selenium import webdriver
options = webdriver.ChromeOptions()
# 添加参数进行去除浏览器检测框
options.add_experimental_option("excludeSwitches", ['enable-automation'])
# 将参数添加到浏览器中
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.baidu.com/')