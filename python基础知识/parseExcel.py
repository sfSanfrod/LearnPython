#!/usr/bin/python
#encoding=utf-8



__author__ = "小白龙"

from openpyxl import Workbook
from openpyxl import load_workbook
import datetime

def writeExcl():
    wb = Workbook()
    sheet1 = wb.active
    sheet1['A1'] = "书名"
    sheet1.append([1, 2, 4])
    sheet1['B1'] = "时间"
    sheet1.append([datetime.datetime.now()])

    wb.save("写入excel示例.xlsx")

def readExcel(path):
    print("读取Excel：",path)
    wb = load_workbook(path)
    sheets = wb.get_sheet_names()
    print(type(sheets))
    print("工作簿：",sheets)

if __name__ == "__main__":
    writeExcl()
    readExcel("读取Excel示例.xlsx")