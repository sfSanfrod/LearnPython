#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python练习题100例

#题目1：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
def function_1():
    for a in range(1,5):
        for b in range (1,5):
            for c in range(1,5):
                if (a != b) and (b != c) and (c!=a):
                    print a,b,c

#题目2：计算奖金
def getBonus():
    profit = int(input("请输入利润金额：\n"))
    # 第一种算法，笨方法
    bonus1 = 0
    if (profit<0) :
        print "输入错误，请输入正确的金额！"
    elif profit<100000 :
        bonus1 = profit * 0.1
        print "第1级"
        print bonus1
    elif (profit>100000)&(profit<200000) :
        bonus1 = 100000*0.1 +(profit-100000)*0.075
        print "第2级"
        print bonus1
    elif (profit>200000)&(profit<400000):
        bonus1 = 100000 * 0.1+100000*0.075 +(profit-200000)*0.05
        print "第3级"
        print bonus1
    elif (profit>400000)&(profit<600000):
        bonus1 = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05+(profit - 400000) * 0.03
        print "第4级"
        print bonus1
    elif (profit > 600000 )& (profit < 1000000):
        bonus1 = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03+ (profit - 600000) * 0.015
        print "第5级"
        print bonus1
    elif profit > 1000000:
        bonus1 = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015 + (profit - 1000000) * 0.01
        print "第6级"
        print bonus1
    print "bonus1:" + str(bonus1)
    #第二种算法
    bonus2 = 0
    arr = [1000000,600000,400000,200000,100000,0]
    rat = [0.01,0.015,0.03,0.05,0.075,0.1]
    for index in range(0,6):
        if profit>arr[index]:
            bonus2+=(profit-arr[index])*rat[index]
            print "第"+str(index+1)+"级："+str((profit-arr[index])*rat[index])
            profit = arr[index]
    print "bonus2:"+str(bonus2)

#题目3：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
import math
def getNumber():
    for i in range(10000):
        x = int(math.sqrt(i + 100))
        y = int(math.sqrt(i + 268))
        if (x*x==i+100)and(y*y==i+268):
            print i

#题目4：输入某年某月某日，判断这一天是这一年的第几天？
def indexOfDay():
    year = int(raw_input("请输入年份：\n"))
    month = int(raw_input("请输入月份：\n"))
    while month<1 or month>12:
        month = int(raw_input("月份输入错误，请重新输入月份：\n"))
    day = int(raw_input("请输入日期：\n"))
    while day<1 or day>31:
        day = int(raw_input("日期输入错误，请重新输入日期：\n"))
    arr = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    index = 0
    for i in range(0,month):
        index += arr[i]
        print arr[i],index
    index += day
# 考虑闰年闰月的情况
#闰年：1）可以被4整除又不被100整除的是闰年；2）可以被400整除的是闰年
    leap = 0
    if(year%4==0 and year%100 != 0 ) or (year%400==0):
        leap = 1
    if leap ==1 and month>2:
        index +=1
    print "您输入的日期为" + str(year) + "年第" + str(index) + "天"

#题目5：输入三个整数x,y,z，请把这三个数由大到小输出。
def getSort(x,y,z):
    #使用if比较
    if x>y:
        if y>z:
            print x, y, z
        elif x>z:
            print x, z, y
        else :
            print z,x,y
    elif x>z:
        print y,x,z
    elif y>z:
        print y,z,x
    else :
        print z,y,x
    #使用数组
    arr = []
    arr.append(x)
    arr.append(y)
    arr.append(z)
    arr.sort()
    arr.reverse()
    print arr

#题目6：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
def feibonaqi(n):
    if n<0 :
        print "请输入正确参数！"
        return
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return feibonaqi(n-1)+feibonaqi(n-2)

#题目7：将一个列表的数据复制到另一个列表中。
def copyList():
    arrA = [34,1,56,8,3,10]
    arrB = []
    for i in range(arrA.__len__()):
        arrB.append(arrA[i])
    print arrB
    #方法二
    arrC = arrA[:]
    print arrC

#题目8：输出 9*9 乘法口诀表
def multiplication():
    for i in range(1,10): #迭代1到10之间的数字(即1到9，不包括10)
        line = ""
        for j in range(1,i+1): #range(1,1)不迭代，所以i要加1
            line += "%d*%d=%d " % (i, j, i*j)
        print line+"\n"

#题目9：暂停一秒输出。
import time
def delaySeconds():
    keyValue = {'name':"sunfeng",'age':27,"sex":'man'}
    for key,value in dict.items(keyValue):
        print key,value
        time.sleep(1)

#题目10：暂停一秒输出，并格式化当前时间。
def formatTime():
    for i in range(3):
        t = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        print t
        time.sleep(1)

#题目11：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
#程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
def countRabbit(n):
    #n为月份
    if n<1:
        return "参数错误！"
    if n==1 or n==2:
        return 1
    else :
        return countRabbit(n-1)+countRabbit(n-2)

#题目12：判断101-200之间有多少个素数，并输出所有素数。
#分析：素数是只能被1和它自己整除的数
import math
def primeNumber():
    #质数
    count = 0
    for i in range(101,200):
        flag = 0
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                flag = 1
                break
        if flag==1:
            continue
        count +=1
        print i
    print count

#13、题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身
def  narcissisticNumber():
    #水仙花数
    for i in range(100,1000):
        x = int(i/100)
        y = int(i/10%10)
        z = int(i%10)
        if (x**3+y**3+z**3)==i:
            print i

#题目14：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
def resolvePrimeNumber(n):
    if n<1:
        print "请输入正整数！"

    print '%d=1*'%n,
    while n!=1:
        for i in range(2,n+1):
            if n%i==0:
                j = n/i
                if i==n:
                    print n
                else:
                    print '%d'%j,








print "==============1================="
#function_1()
print "==============2================="
#getBonus()
print "==============3================="
#getNumber()
print "==============4================="
#indexOfDay()
print "==============5================="
#getSort(12,-12,33)
print "==============6================="
#print feibonaqi(10)
print "==============7================="
#copyList()
print "==============8================="
#multiplication()
print "==============9================="
#delaySeconds()
print "==============10================"
#formatTime()
print "==============11================"
#print countRabbit(0)
print "==============12================"
#primeNumber()
print "==============13================"
#narcissisticNumber()
print "==============14================"
resolvePrimeNumber(9)
