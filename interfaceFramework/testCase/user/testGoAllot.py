#!/usr/bin/env python
#coding=utf-8

__author__ = '小白龙'

import unittest
from interfaceFramework.lib import paramunittest
from interfaceFramework.public import sendRequest, parseConfig, utiles
import os

request = sendRequest.SendRequest()
config = parseConfig.ReadConfig()
excel = config.get_option('file', 'user_address')
test_data = utiles.read_excel(excel, 'goAllot')

@paramunittest.parametrized(*test_data)
class GoAllot(unittest.TestCase):
    """修改经办为分案状态"""
    def setParameters(self,case_name, url, method, userIdList, code, message):
        self.host = config.get_option('host', 'edgeUser')
        self.case_name = case_name
        self.url = self.host+url
        self.method = method
        self.userIdList = userIdList
        self.expect_code = int(code)
        self.expect_msg = message
        self.header = {'Content-Type': "application/json", 'token': config.get_option('token', 'token')}

    def test_goAllot(self):
        print("执行测试用例：",self.case_name, self.url, self.method)
        print('请求header：', self.header)
        request.set_url(self.url)

        if self.method == 'post_json':
            datas = {"userIdList": eval(self.userIdList)}
            print('请求参数：',datas)
            request.set_data(datas)
            request.set_headers(self.header)
            response = request.send_post_json()
        else:
            print("method error")

        print('返回code：', response.status_code)
        print('返回body：',response.text)

        self.assertEqual(response.status_code, self.expect_code)
        self.assertIn(self.expect_msg,response.text,'预期信息不在返回值内')


if __name__ == "__main__":
    unittest.main(verbosity=2)