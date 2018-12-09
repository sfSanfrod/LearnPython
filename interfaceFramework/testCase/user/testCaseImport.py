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
test_data = utiles.read_excel(excel, 'caseImport')

@paramunittest.parametrized(*test_data)
class CaseImport(unittest.TestCase):
    """案件导入接口"""
    def setParameters(self,case_name, url, method, assetId, code, message):
        self.host = config.get_option('host', 'edgeUser')
        self.case_name = case_name
        self.url = self.host+url
        self.method = method
        self.assetId = assetId
        self.expect_code = int(code)
        self.expect_msg = message
        self.header = {'Content-Type': "application/x-www-form-urlencoded",'Cache-Control': "no-cache",'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",'appid': "10003", 'token': config.get_option('token', 'token')}

    def test_caseImport(self):
        print("执行测试用例：",self.case_name, self.url, self.method)
        print('请求header：', self.header)
        request.set_url(self.url)

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"file\"; filename=\"D:\\GitHub\\LearnPython\\interfaceFramework\\testData\\caseImport.xlsx\"\r\nContent-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"assetId\"\r\n\r\n2\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        if self.method == 'post_file':
            datas = {"assetId": self.assetId}
            print('请求参数：',datas)
            request.set_data(datas)
            request.set_headers(self.header)
            file_name = r'caseImport.xlsx'
            request.set_file(file_name)
            print('文件路径：', request.file_path)
            response = request.send_post_file(payload)
        else:
            print("method error")

        print('返回code：', response.status_code)
        print('返回body：',response.text)

        self.assertEqual(response.status_code, self.expect_code)
        self.assertIn(self.expect_msg,response.text,'预期信息不在返回值内')


if __name__ == "__main__":
    unittest.main(verbosity=2)