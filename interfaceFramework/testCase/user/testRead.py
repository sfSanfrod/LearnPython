#!/usr/bin/env python
#coding=utf-8

__author__ = '小白龙'

import unittest
from interfaceFramework.lib import paramunittest
from interfaceFramework.public import sendRequest, parseConfig, utiles

request = sendRequest.SendRequest()
config = parseConfig.ReadConfig()
excel = config.get_option('file', 'user_address')
test_data = utiles.read_excel(excel, 'read')

@paramunittest.parametrized(*test_data)
class Read(unittest.TestCase):
    """阅读消息接口"""
    def setParameters(self, case_name, url, method, msg_id, code, message):
        self.host = config.get_option('host', 'edgeUser')
        self.case_name = case_name
        self.url = self.host + url
        self.method = method
        self.msg_id = msg_id
        self.expect_code = int(code)
        self.expect_msg = message
        self.header = {'Content-Type': "application/json", 'token': config.get_option('token', 'token')}

    def test_query(self):
        print("执行测试用例：", self.case_name, self.url, self.method)
        print('请求header：', self.header)
        request.set_url(self.url)

        if self.method == 'get':
            params = {"id": self.msg_id}
            request.set_params(params)
            request.set_headers(self.header)
            response = request.send_get()
        elif self.method == 'post_json':
            datas = {"id": self.msg_id}
            request.set_data(datas)
            request.set_headers(self.header)
            response = request.send_post_json()
        else:
            print("method error")

        print('返回code：', response.status_code)
        print('返回body：', response.text)
        self.assertEqual(response.status_code, self.expect_code)
        self.assertIn(self.expect_msg, response.text, '预期信息不在返回值内')


if __name__ == "__main__":
    unittest.main(verbosity=2)
