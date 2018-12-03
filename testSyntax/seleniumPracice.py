#!/usr/bin/python
#coding=utf-8

from selenium import webdriver
from time import sleep

import sys
reload(sys)
sys.setdefaultencoding(u'utf-8')

if __name__=='__main__':
    url = u'https://exmail.qq.com/cgi-bin/loginpage?t=dm_loginpage&dmtype=bizmail'
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(chrome_options=options)
    print(u'已打开浏览器')
    driver.get(url)
    print(u'已打开网页')
    # 输入用户名密码
    name = driver.find_element_by_id('inputuin')
    passwd = driver.find_element_by_id('inputuin')
    print(name.get_property('location'))