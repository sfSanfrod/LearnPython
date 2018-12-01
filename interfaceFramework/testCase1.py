#!/usr/bin/env python
#coding=utf-8

import unittest
import paramunittest
from interfaceFramework import parseExcel,sendRequest,utiles,parseConfig

request = sendRequest.SendRequest()
config = parseConfig.ReadConfig(r"D:\GitHub\LearnPython\interfaceFramework\config.ini")
excel = config.read_option('file','address')
print(excel)
test_data = utiles.read_excel(excel,'三年一班')

@paramunittest.parametrized(*test_data)
class TestCase1(unittest.TestCase):

    def setParameters(self, case_name, url, method, param1,param2):
        self.case_name = case_name
        self.url = url
        self.method = method
        self.param1 = param1
        self.param2 = param2

    def test_Case(self):
        print("执行测试用例：",self.case_name)
        print(self.case_name, self.url, self.method)
        urlstr = r"https://www.baidu.com/home/msg/data/personalcontent"
        request.set_url(self.url)

        if self.method == 'get':
            params = {"param1": self.param1, "param2": self.param2}
            request.set_params(params)
            response = request.send_get()
        elif self.method == 'post':
            datas = {"param1": self.param1, "param2": self.param2}
            request.set_data(datas)
            response = request.send_post()
        else:
            print("method error")

        print(response.url)
        print(response.text)

if __name__ == "__main__":
    unittest.main()

