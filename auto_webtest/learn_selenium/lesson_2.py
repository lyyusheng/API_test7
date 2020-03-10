# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"E:\python37\Lib\site-packages\selenium\webdriver\chrome\chrome\chromedriver.exe")
driver.get('http://www.baidu.com')
