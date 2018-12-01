#!/usr/bin/env python
#coding=utf-8

__author__ = '小白龙'
from xlrd import open_workbook

class ReadExcel():
    def __init__(self,filepath):
        self.workbook = open_workbook(filepath)
    def read_sheet(self,sheetname):
        self.sheet = self.workbook.sheet_by_name(sheetname)
        return self.sheet
    def get_data(self,filepath,sheetname):
        wb = open_workbook(filepath)
        sheet = wb.sheet_by_name(sheetname)
        nrows = sheet.nrows
        data = []
        for i in range (nrows):
            if sheet.row_values(i)[0] != "姓名" :
                data.append(sheet.row_values(i))
        return data

if __name__ == '__main__':
    wc = ReadExcel(r"D:\GitHub\LearnPython\python基础知识\读取Excel示例.xlsx")
    wc.read_sheet("三年一班")
    wc.get_data()



