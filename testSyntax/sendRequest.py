#!/usr/bin/python
#coding=utf-8

import urllib2
import openpyxl

if __name__=='__main__':
    url = u"https://api.douban.com/v2/book/search?q=python"
    response = urllib2.urlopen(url)


    response_str = response.read()
    # 将string转换成dict
    response_dic = eval(response_str)
    count = response_dic['count']
    total = response_dic['total']
    print(count)
    print(total)