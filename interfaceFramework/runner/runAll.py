#!/usr/bin/env python
#coding=utf-8

__author__ = '小白龙'

import os
import unittest
import datetime
from interfaceFramework.public import HTMLTestReportCN,parseConfig
from interfaceFramework.testCase.testCase1 import TestCase1


config = parseConfig.ReadConfig()

class RunAll(unittest.TestCase):
    def __init__(self):
        self.case_path = config.get_option('case', 'path')
        str = config.get_option('report', 'reportPath')
        self.report = os.path.join(str,'report.html')
        self.suit = unittest.defaultTestLoader.discover(self.case_path,pattern='test*.py')
    def setUp(self):
        pass

    def run(self):
        fp = open(self.report,'wb')
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,description="接口测试",tester="小白龙")
        runner.run(self.suit)
        fp.close()

    def tearDown(self):
        pass


if __name__ == '__main__':
    test = RunAll()
    test.run()
