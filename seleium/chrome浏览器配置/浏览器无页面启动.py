#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 浏览器无页面启动.py 
@time: 2021/02/19 
"""

'''
所谓的无页面启动就是不会启动浏览器，全部都是看不到的，只是在后台进行了运行。
环境配置
1. 需要将chrome的驱动放入到环境变量中。
2. 需要用到webdriver中的ChromeOptions()方法。
3. 将方法中的headless 参数配置为True。
'''


#无页面启动进入百度
from selenium import webdriver
# 导入chromeOptions方法
opt = webdriver.ChromeOptions()
# 将headless设置为True，此方法表示将chrome设置为无页面启动
opt.headless = True
# 将设置好的参数添加到chrome浏览器中进行启动
driver = webdriver.Chrome(options=opt)
driver.get('https://www.baidu.com')
print(driver.title)