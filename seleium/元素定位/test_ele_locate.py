#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test_ele_locate.py 
@time: 2021/03/19 
"""

from time import sleep
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
使用find_element()的好处是方法名不会写死，定位方式可以通过参数传递，在一些框架中使用时会更加灵活一些
通过 find_elements() 或者find_elements_by_id() （注意都多了个 s），将以列表的形式返回所有符合条件的元素。

jquery语法：
$('这里是css selector语法')，如：$("#kw")
发送文本：.val()
点击：.click()
'''

class TestLocate:
    def setup(self):
        self.driver=webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        patch = os.path.dirname(os.path.abspath(__file__))
        file_patch = 'file:///' + patch + '/ele_locate.html'
        print(file_patch)
        self.driver.get(file_patch)
        self.driver.implicitly_wait(3)


    def teardown(self):
        self.driver.quit()

    def test_by_css(self):
        #css 选择器语法：https://www.runoob.com/cssref/css-selectors.html
        # 测试css的语法是：$$("") ，括号中的内容为css的定位语法,css_selector:不能用于appium，应用里面嵌套的网页可以，比xpath快
        pass

    def test_by_xpath(self):
        '''
            xpath:xml path language(速度慢，从头到尾遍历，可用于appium，seleium)
            / 代表子元素  //代表所有子孙元素  . 选取当前节点  .. 选取当前节点的父节点 @ 选取属性
            表达式  结果
            /books/book[1] 选取books子元素的第一个book元素
            /books/book[last()] 选取books子元素的最后一个book元素
            /books/book[last()-1]  选取books子元素的倒数第二个book元素
            /books/book[position()<3] 选取最前面的两个属于books元素的子元素的book属性
            //title[@lang='eng]  选取所有title冤死，切这些元素拥有职位eng的lang属性
            /books/book[price>35]  选取books所有books元素，且其中的price必须大于35
            /books/book[price>35]/title  选取books元素在book元素的所有title，且book的price必须大于35

            在console中用 $x('//*[@id="s_tab"]//a[0]')
            '''
        # https://blog.csdn.net/minzhung/article/details/102641230
        #验证xpath语法是$x(“your_xpath_selector”)，如：$x('//*[@id="kw"]')
        pass


    def test_by_id(self):
        # id是全局唯一的
        # console验证：document.getElementById("alert")
        self.driver.find_element_by_id("alert").click()
        sleep(3)

    def test_by_name(self):
        # 同一表单中name不相同，同一页面name可能相同，name和id可以共存
        # console验证：document.getElementsByName("user")
        self.driver.find_element(By.NAME,"user").click()
        sleep(3)

    def test_by_tag_name(self):
        # 标签，在某些特殊情况下定位body，html，head，或者批量处理某些标签
        # console验证：document.getElementsByTagName("button")
        btn=self.driver.find_element(By.TAG_NAME,"button")
        print(btn.text)

    def test_by_link_text(self):
        # 专门用来定位文本链接也就是<a> 标签。
        # console验证：$x('//a[string()="Alert-id"]')
        txt=self.driver.find_element(By.LINK_TEXT,"Alert-id")
        print(txt.text)

        # 模糊匹配的定位
        # console验证：$x('//a[contains(string(), "Alert")]')
        txt2 = self.driver.find_element_by_partial_link_text("Alert")
        print(txt2.text)

    def test_by_class_name(self):
        # class="bg foot" ,空格在这里的作用是分割多个类名的。这个 class 属性有1个空格，那么的代表这个 class 属性中包含了2个类名。
        #document.getElementsByClassName("bg")
        re = self.driver.find_elements(By.CLASS_NAME,"bg")
        for e in re:
            print(e.tag_name,e.text)

        h_re= self.driver.find_element(By.CLASS_NAME,"head")
        print("h_re:",h_re.text)

        f_re = self.driver.find_element(By.CLASS_NAME, "foot")
        print("f_re:", f_re.text)







