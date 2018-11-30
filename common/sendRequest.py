#!/usr/bin/env python
#coding=utf-8

import requests

class SendRequest():
    def __init__(self):
        self.headers = {}
        self.host = None
        self.url = None
        self.params = {}
        self.data = {}
    def set_url(self,url):
        self.url = url
        return self.url
    def set_headers(self,header):
        self.headers = header
    def set_params(self,params):
        self.params = params
    def set_data(self,data):
        self.data = data

    def send_get(self):
        response = requests.get(url=self.url,headers=self.headers,params=self.params)
        return response

    def send_post(self):
        response = requests.post(url=self.url,headers=self.headers,data=self.data)
        return response

if __name__ == '__main__':
    sentReq = SendRequest()
    urlStr = r'https://www.baidu.com/home/msg/data/personalcontent?callback=jQuery110209756313901626137_1543412774419&num=8&_req_seqid=&sid=&_=1543412774420'
    sentReq.set_url(urlStr)
    response = sentReq.send_get()
    print(response.headers)
    print(response.cookies)
    print(response.text)

    print("=========================")
    url2 = r'http://i.baidu.com/msg/message/get/'
    data = {'srcid':1,
            'status':0,
            'appid':0,
            'intPage':0,
            'cuttitle':30}
    sentReq.set_url(url2)
    sentReq.set_data(data)
    response2 = sentReq.send_post()
    print(response2.text)