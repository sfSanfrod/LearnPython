#!/usr/bin/python
#encoding=utf-8



__author__ = "小白龙"

from openpyxl import Workbook

if __name__ == "__main__":
    wb = Workbook()
    sheet = wb.active
    sheet['A1'] = "书名"

    wb.save("简单excel写示例.xlsx")