#!/usr/bin/env python
#coding=utf-8

import os
import xlrd

def read_excel(file,sheet):
    data = []
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheet_by_name(sheet)
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0]!="用例名字":
            data.append(sheet.row_values(i))
    return data
