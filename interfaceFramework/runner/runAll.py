#!/usr/bin/env python
#coding=utf-8

__author__ = '小白龙'

import os
import unittest
import datetime
from interfaceFramework.public import parseConfig,sendEmail
from interfaceFramework.lib import HTMLTestReportCN

config = parseConfig.ReadConfig()

class RunAll(unittest.TestCase):
    def __init__(self):
        self.case_path = config.get_option('case', 'path')
        self.report_path = config.get_option('report', 'reportPath')
        self.suit = []

    def set_test_suit(self):
        self.suit = unittest.defaultTestLoader.discover(self.case_path, pattern='test*.py',top_level_dir=None)
        # print(self.case_path)
        # print(self.suit)


    def run(self):
        self.set_test_suit()
        report_name = "Report_%s.html" % datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
        report = os.path.join(self.report_path, report_name)
        fp = open(report,'wb')
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, description="接口测试", tester="小白龙")
        runner.run(self.suit)
        fp.close()
        if config.get_option('email','switch')=='on':
            mail = sendEmail.SendEmail(report)
            mail.send_email()
            print("发送邮件结束")



if __name__ == '__main__':
    runall = RunAll()
    runall.run()
