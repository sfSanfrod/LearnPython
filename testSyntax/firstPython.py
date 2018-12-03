#!/usr/bin/python
#coding=utf-8

import time

str = "Hello World!"
str2 = "我是孙峰！"
print str +"\n"+ str2
print "字符串str2的长度为：",len(str2)

flag = False
name = "Tom"
if name == "SunFeng":
    flag = True
    print "Welcome Boss!"
else:
    print "Your name is "+name

list1 = ['physics', 'chemistry', 1997, 2000]
print list1[1:2]
print list1[0:-2]

#时间&日期
nowtime = time.time()
print "当前时间戳：",nowtime
localtime = time.localtime(time.time())
print "当地时间：",localtime

#函数
def printMsg(string):
    print "My name is "+ string
    print "What's your name ?"
    return "Messages were printed."

print printMsg("Sanford")

#文件IO
#两种读取标准输入的函数raw_input、input
def whatsUname():
    strA = raw_input("Hi beautiful girl ,whats u name?")
    print "Nice to meet u " + strA
    strB = input("please input a number!")
    print strB



whatsUname()



