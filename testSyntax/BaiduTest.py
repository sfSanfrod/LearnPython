#!/usr/bin/python
#coding=utf-8

__author__ = u'浪里小白龙'

from time import sleep

from selenium import webdriver
import HTMLTestRunner
import unittest

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class BaiduTest(unittest.TestCase):
    #"百度首页搜索测试"
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.baidu.com"

    def test_baidu_search(self):
        driver = self.driver
        print(u'开始[case_001]百度搜索')
        driver.get(self.base_url)
        #验证标题
        self.assertEqual(driver.title,u'百度一下，你就知道')
        # 清理搜索输入框中的数据
        driver.find_element_by_id('kw').clear()
        # 在搜索输入框中输入浪里小白龙
        driver.find_element_by_id('kw').send_keys(u'浪里小白龙')
        # 单击 百度一下 按钮
        driver.find_element_by_id('su').click()
        sleep(3)
        # 验证搜索结果标题
        self.assertEqual(driver.title,u'浪里小白龙_百度搜索')
        sleep(10)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(BaiduTest('test_baidu_search'))
    # 定义报告输出路径
    htmlPath = ur'D:\testReport.html'
    fp = file(htmlPath,'wb')  #wb,如果该文件已存在则覆盖，不存在则新建文件
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'百度测试',description=u'测试用例结果')
    runner.run(testunit)
    fp.close()
