#!/usr/bin/env python
#coding=utf-8

__author__ = '小白龙'

import os
import unittest
import datetime
from interfaceFramework.public import HTMLTestReportCN,parseConfig
from interfaceFramework.testCase.testCase1 import TestCase1


config = parseConfig.ReadConfig()
case_path = config.get_option('case', 'path')
report_path = config.get_option('report', 'reportPath')

class RunOne(unittest.TestCase):
    def __init__(self):

        #name = 'report_'+datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d%H%M%S')+'.html'
        self.report = os.path.join(report_path,'report.html')
        self.case_list = []

    def setUp(self):
        pass
    def read_case_list(self):
        file = open('./testCaseList.txt')
        for value in file.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.case_list.append(data.replace("\n", ""))
        file.close()
        print("需要执行的测试用例集合："+str(self.case_list))
    def set_case_suite(self):
        self.suit = []

    def run(self):
        fp = open(self.report,'wb')
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,description="接口测试",tester="小白龙")
        runner.run(self.suit)
        fp.close()

    def tearDown(self):
        pass


if __name__ == '__main__':
    test = RunOne()
    # print(test.report)
    test.read_case_list()

