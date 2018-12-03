#!/usr/bin/python
#coding=utf-8

__author__ = u'浪里小白龙'

from time import sleep
from selenium import webdriver
import unittest
from threading import Thread

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def test_baidu_search(browser,url):
        driver = None
        if browser=='ie':
            driver = webdriver.Ie()
        elif browser == 'firefox':
            driver = webdriver.Firefox()
        elif browser == 'chrome':
            driver = webdriver.Chrome()
        else:
            driver = None
            exit()

        print(u'开始['+browser+'_001]百度搜索')
        driver.get(url)
        # 清理搜索输入框中的数据
        driver.find_element_by_id('kw').clear()
        # 在搜索输入框中输入浪里小白龙
        driver.find_element_by_id('kw').send_keys(u'浪里小白龙')
        # 单击 百度一下 按钮
        driver.find_element_by_id('su').click()
        sleep(5)
        driver.quit()


if __name__ == '__main__':
    # 浏览器和首页url
    url = u'http://www.baidu.com'
    data={"ie":url,"firefox":url,"chrome":url}

    # 构建线程
    threads=[]
    for browser,url in data.items():
        t = Thread(target=test_baidu_search,args=(browser,url))
        threads.append(t)
    # 启动所有线程
    for t in threads:
        t.start()



