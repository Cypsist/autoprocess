# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 10:45:06 2023

@author: Reaper
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

# 创建一个 Chrome 浏览器实例
browser = webdriver.Chrome()

# 打开一个搜索引擎的网站
browser.get("https://www.baidu.com/")

# 找到搜索框并输入关键字
search_box = browser.find_element(By.NAME,'wd')
search_box.send_keys("Python")
search_box.send_keys(Keys.RETURN)

# 等待搜索结果加载完成
sleep(5)

# 找到搜索结果的第一条，并点击打开
first_result = browser.find_element(By.CSS_SELECTOR,"#content_left div.result h3.t a")
first_result.click()
input()
# 关闭浏览器
browser.quit()
