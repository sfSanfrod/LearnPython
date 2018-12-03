#!/usr/bin/python
#coding:utf-8

import xlrd,xlwt
import openpyxl
from time import sleep

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def writeExcel(path):
    print(u'开始写入数据：')
    xlpath = path
    #实例化一个excel
    excel = xlwt.Workbook()
    # 新增一个sheet
    sheet = excel.add_sheet(u"工作表1",cell_overwrite_ok=True)
    # 写入数据头
    headlist = [u'序号',u'第一列',u'第二列',u'第三列']
    rowIndex = 0
    column = 0
    for head in headlist:
        sheet.write(rowIndex,column,head)
        column=column+1
    #循环写入数字
    number = 1
    for row in range(1,11):
        print(u'开始写入第%d行数据...'%row)
        #写入序号
        sheet.write(row, 0, row)
        #写入数据
        for col in range(1,4):
            sheet.write(row,col,number)
            number = number+2
        print(u'第%d行数据写入成功：success' % row)
    excel.save(path)




def readExcel(path):
    print(u'开始读取数据：')
    xlpath = path
    excel = xlrd.open_workbook(xlpath)
    # 获取excel工作簿数
    count = len(excel.sheets())
    print(u'工作簿数：%d'%count)
    # 获取 表 数据的行列数
    sheet = excel.sheets()[0]
    nrows = sheet.nrows
    ncols = sheet.ncols
    print(u"表数据行列为(%d, %d)" % (nrows, ncols))
    # 循环读取数据
    for row in range(0,nrows):
        rowvalues = sheet.row_values(row)
        #循环读取每行里的数据
        for data in rowvalues:
            print(data)," ",
        print("")


if __name__ == '__main__':
    path = ur'D:\writeExcel.xls'
    writeExcel(path)
    sleep(2)
    readExcel(path)