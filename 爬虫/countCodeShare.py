#!/usr/bin/python
#encoding=utf-8

__author__ = "小白龙"

from urllib import request , response, parse
# import urllib
import re



url1 = "http://confluence.ppdai.com/plugins/pagetree/naturalchildren.action?decorator=none&excerpt=false&sort=position&reverse=false&disableLinks=false&expandCurrent=false&hasRoot=true&pageId=10066797&treeId=0&startDepth=0&mobile=false&treePageId=2917743"
url2 = "http://confluence.ppdai.com/plugins/pagetree/naturalchildren.action?decorator=none&excerpt=false&sort=position&reverse=false&disableLinks=false&expandCurrent=false&hasRoot=true&pageId=19729728&treeId=0&startDepth=0&mobile=false&treePageId=2917743"
url_index = "http://confluence.ppdai.com/"
url_login = "http://confluence.ppdai.com/dologin.action"
"""os_username=sunfeng&os_password=123456&login=%E7%99%BB%E5%BD%95&os_destination="""
#未登录时刷新
"""http://confluence.ppdai.com/login.action;jsessionid=4A2D225E921FE0E28AB44F430E8DC345?os_destination=%2Fpages%2Fviewpage.action%3FpageId%3D10066799"""

def login(username,password):
    req = request.Request(url_login)
    req.add_header('Origin','http://confluence.ppdai.com')
    # req.add_header('Cookie','mywork.tab.tasks=false; JSESSIONID=7902501B4D6424D692891F597EE872ED')
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')
    req.add_header('Content-Type','application/x-www-form-urlencoded')
    req.add_header('Connection','keep-alive')
    req.add_header('Referer','http://confluence.ppdai.com/login.action?logout=true')

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
    req.add_header('Cookie', 'mywork.tab.tasks=false; JSESSIONID=5EF3D96C7C8F6FFA3E0E726CF4906C6E')
    response = request.urlopen(req)
    page = response.read().decode()
    print(page)
    pattern = r'代码分享\（\d{4}-\d{1,2}-\d{1,2}\）'
    # p = re.compile(pattern)
    result = re.findall(pattern,page)
    print(result)
    print(len(result))

if __name__ == "__main__":
    # login('sunfeng','123456')
    count(url1)

    # 代码分享2018 - 1 - 17）