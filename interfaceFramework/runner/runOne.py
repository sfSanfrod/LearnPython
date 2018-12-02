#!/usr/bin/env python
#coding=utf-8

__author__ = '小白龙'

import os
import unittest
import datetime
from interfaceFramework.public import HTMLTestReportCN,parseConfig
from interfaceFramework.testCase.testCase1 import TestCase1



config = parseConfig.ReadConfig()

class RunOne(unittest.TestCase):
    def __init__(self):

        str = config.read_option('report','reportPath')
        #name = 'report_'+datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d%H%M%S')+'.html'
        self.report = os.path.join(str,'report.html')
        self.suit = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
        #self.suit = unittest.TestSuite(TestCase1('test_Case'))
        self.suit.addTest(TestCase1('test_Case'))
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
    test = RunOne()
    print(test.report)
    test.run()
