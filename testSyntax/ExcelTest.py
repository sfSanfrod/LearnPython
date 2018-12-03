#!/usr/bin/python
#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
import xlrd
from time import sleep
import unittest
import HTMLTestRunner

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class LoadTestData:
    def __init__(self,path):
        self.path = path

    def load_data(self):
        #打开Excel文件
        excel = xlrd.open_workbook(self.path)
        # 获取第一个工作表
        table = excel.sheets()[0]
        # 获取行数
        nrows = table.nrows
        # 从第二行开始遍历数据,存入一个list中
        test_data = []
        for i in range(1,nrows):
            test_data.append(table.row_values(i))
        # 返回读取的数据列表
        return test_data


class ExcelTest(unittest.TestCase):
    """百度首页搜索测试用例"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = u'http://www.baidu.com'
        self.path = ur'D:\seleniumExcelTest.xlsx'

    def test_baidu_search(self):
        driver = self.driver
        print(u"开始[case_0001]百度搜索")
        # 加载测试数据
        test_excel = LoadTestData(self.path)
        data = test_excel.load_data()
        print("测试数据:")
        print(data)
        #循环参数化
        for d in data:
            driver.get(self.base_url)
            # 验证标题
            self.assertEqual(driver.title, u'百度一下，你就知道')
            # 清理搜索输入框中的数据
            driver.find_element_by_id('kw').clear()
            # 参数化 搜索词
            driver.find_element_by_id('kw').send_keys(d[0])
            # 单击 百度一下 按钮
            driver.find_element_by_id('su').click()
            sleep(3)
            # 验证搜索结果标题
            self.assertEqual(driver.title, d[1])
            sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(ExcelTest("test_baidu_search"))
    # 定义报告输出路径"
    htmlPath = ur"D:\testExcelReport.html"
    fp = file(htmlPath,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"参数化百度搜索关键词测试",description=u"测试结果")
    runner.run(testunit)
    fp.close()