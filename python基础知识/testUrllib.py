#!/usr/bin/python
#encoding=utf-8

__author__ = "小白龙"

import urllib.request

if __name__ == "__main__":
    url = "https://book.douban.com/j/subject_suggest?q=python"
    response = urllib.request.urlopen(url)
    print(response)
    # 将bytes数据流解码成string
    response_str = response.read().decode()
    print(response_str)
    # 将string转换成dict
    response_dict = eval(response_str)
    print(response_dict)
    print(len(response_dict))
    for ( i=0;i< len(response_dict);i++ ):
        pass

