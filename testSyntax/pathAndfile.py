#!/usr/bin/python
#coding=utf-8

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#打印当前路径
curpath = os.getcwd()
print(curpath)
#遍历目录下的文件并打印绝对路径，方法一：
def print_path_one(path):
    if not os.path.isdir(path):
        print(u'路径错误')
        return False
    for file in os.listdir(path):
        fullpath = os.path.join(path,file)
        print(fullpath)
        if os.path.isdir(fullpath):
            print_path_one(fullpath)

def print_path_two(path):
    """使用os.walk()方法"""
    if not os.path.isdir(path):
        print(u'路径错误')
        return False
    #root 根目录
    #dirs 根目录下的子目录
    #files 根目录下的文件
    walk_result = os.walk(path)
    print(walk_result)
    for root,dirs,files in walk_result:
        #打印跟目录
        print(root)
        #遍历子目录
        for name in dirs:
            print(name)
        #遍历子文件
        for name in files:
            print(name)

if __name__=='__main__':
    path=r'D:\A'
    print_path_one(path)
    print(u'===============')
    print_path_two(path)
