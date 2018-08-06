#!/usr/bin/python
#encoding=utf-8

__author__ = "小白龙"

from urllib import request , response, parse
# import urllib
import re



#未登录时刷新

def login(username,password):
    req = request.Request(url_login)
    req.add_header('Origin','http://')
    # req.add_header('Cookie','mywork.tab.tasks=false; JSESSIONID=7902501B4D6424D692891F597EE872ED')
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')
    req.add_header('Content-Type','application/x-www-form-urlencoded')
    req.add_header('Connection','keep-alive')
    req.add_header('Referer','http://')

    values = {"os_username":username,"os_password":password,"login":"登陆","os_destination":""}
    data = parse.urlencode(values).encode('utf-8')

    with request.urlopen(req, data) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))

def count(url):
    # respone = request.urlopen(url)
    req = request.Request(url)
    req.add_header('Cookie', 'mywork.tab.tasks=false; JSESSIONID=AB9820356EBDBFFA9DD8E0FE494CF26C')
    response = request.urlopen(req)
    page = response.read().decode()
    print(page)
    pattern = r'代码分享\（\d{4}-\d{1,2}-\d{1,2}\）'
    # p = re.compile(pattern)
    result = re.findall(pattern,page)
    print(result)
    print(len(result))
    url_pattern = r'/pages/viewpage.action\?pageId=\d{7,10}">代码分享\（'
    url_result = re.findall(url_pattern,page)
    print(url_result)
    print(len(url_result))

def parseComent(url):
    pass


if __name__ == "__main__":
    # login('sunfeng','123456')
    count(url1)

    # 代码分享2018 - 1 - 17）