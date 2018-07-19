#!/usr/bin/python
#encoding=utf-8

__author__ = "小白龙"

import urllib.request


if __name__ == "__main__":
    url = "https://book.douban.com/j/subject_suggest?q=python"
    response = urllib.request.urlopen(url)
    print(response)
    print("返回状态码：", response.status)
    print("返回状态码对应的文字：",response.reason)
    print("返回的header：",response.headers)
    # 将bytes数据流解码成string
    response_str = response.read().decode()
    print(response_str)
    # 将string转换成dict
    response_dict = eval(response_str)
    print(response_dict)
    print("共有%d本推荐书籍"%len(response_dict))
    n = len(response_dict)
    for book in response_dict:
        print(book["title"],"作者：",book["author_name"])

