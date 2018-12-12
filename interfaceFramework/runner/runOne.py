#!/usr/bin/env python
#coding=utf-8

__author__ = '小白龙'

import os
import unittest
import datetime
from interfaceFramework.public import parseConfig,sendEmail
from interfaceFramework.lib import HTMLTestReportCN

config = parseConfig.ReadConfig()
# case_path = config.get_option('case', 'path')
case_path = r'D:\GitHub\LearnPython\interfaceFramework\testCase'
report_path = config.get_option('report', 'reportPath')

class RunOne(unittest.TestCase):
    def __init__(self):
        self.report_path = config.get_option('report', 'reportPath')
        self.case_list = []

    def setUp(self):
        pass
    #读取testCaseList.txt文件里的测试用例类
    def read_case_list(self):
        file = open('./testCaseList.txt')
        for value in file.readlines():
            case_name = str(value)
            if case_name != '' and not case_name.startswith("#"):
                self.case_list.append(case_name.replace("\n", ""))
        file.close()
        print("需要执行的测试用例集合："+str(self.case_list))
    #将read_case_list()方法读取的测试用例类放到测试集合里
    def set_case_suite(self):
        self.read_case_list()
        test_suit = unittest.TestSuite()
        suit_module = []
        for case in self.case_list:
            casename = case.split('/')[-1]
            path = case_path+'\\'+str(case.split('/')[0])
            print(casename)
            print(path)
            discover = unittest.defaultTestLoader.discover(path,pattern=casename,top_level_dir=None)
            suit_module.append(discover)
        if len(suit_module)>0:
            for suit in suit_module:
                for case in suit:
                    test_suit.addTest(case)

        else :
            return None
        return test_suit

    def run(self):
        suit = self.set_case_suite()
        report_name = "Report_%s.html" % datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
        report = os.path.join(self.report_path, report_name)
        fp = open(report,'wb')
        if suit is not None:
            runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, description="接口测试", tester="小白龙")
            runner.run(suit)
        fp.close()
        if config.get_option('email','switch')=='on':
            mail = sendEmail.SendEmail(report)
            mail.send_email()
            print("发送邮件结束")

    def tearDown(self):
        pass


if __name__ == '__main__':
    test = RunOne()
    test.run()

