#!/usr/bin/env python
#encoding=utf-8

__author__ = "小白龙"

import pymysql
from interfaceFramework.public import  parseConfig

config = parseConfig.ReadConfig()

class testDB():
    def __init__(self):
        self.host =config.get_option('database','host')
        self.port = int(config.get_option('database','port'))
        self.user = config.get_option('database','user')
        self.passwd = config.get_option('database','passwd')
        self.db = config.get_option('database','db')

    def creat_connect(self):
        self.connect = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.db)
        return self.connect
    def creat_cursor(self):
        self.cursor = self.connect.cursor()
        return self.cursor

    def close(self):
        self.cursor.close()
        self.connect.close()

if __name__ == '__main__':
    db = testDB()
    db.creat_connect()
    cursor = db.creat_cursor()
    sql = 'select * from tb_assets limit 10'
    cursor.execute(sql)
    row = cursor.fetchall()
    for i in row:
        print(i)
