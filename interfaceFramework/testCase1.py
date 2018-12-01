#!/usr/bin/env python
#coding=utf-8

import unittest
import paramunittest
from interfaceFramework import parseExcel,sendRequest

excel = parseExcel.ReadExcel(r"D:\GitHub\LearnPython\python基础知识\读取Excel示例.xlsx")
test_data = excel.get_data(r"D:\GitHub\LearnPython\python基础知识\读取Excel示例.xlsx","三年一班")
request = sendRequest.SendRequest()

@paramunittest.parametrized(*test_data)
class TestCase1(unittest.TestCase):

    def setParameters(self,name,kemu,fenshu,state):
        self.name = name
        self.kemu = kemu
        self.fenshu = fenshu
        self.state = state
        para = []
    def test_Case(self):
        print(self.name,self.kemu,self.fenshu,self.state)
        params = {"name":self.name,"kemu":self.kemu,"fenshu":self.fenshu,"state":self.state}
        request.set_url(r"https://www.baidu.com/home/msg/data/personalcontent")
        request.set_params(params)
        response = request.send_get()
        print(response.url)

if __name__ == "__main__":
    unittest.main()

