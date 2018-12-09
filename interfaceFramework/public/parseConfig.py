#!/usr/bin/env python
#coding=utf-8

__author__ = '小白龙'

import configparser
import os

#因为config.ini文件与当前python文件在同一目录下，
# 所以直接根据当前文件所在目录拼接config文件的路径
# path = os.path.dirname(os.getcwd()) #获取当前文件所在目录的父目录
# configPath = os.path.join(path, "public\config.ini")     #拼接config文件路径
configPath = r'D:\GitHub\LearnPython\interfaceFramework\public\config.ini'

class ReadConfig:
    def __init__(self):
        self.filepath = configPath
        self.config = configparser.ConfigParser()
        self.config.read(self.filepath,encoding='utf-8')

    def get_option(self, section, name):
        value = self.config.get(section,name)
        return value
    def get_sections(self):
        section_list = self.config.sections()
        return section_list
    def get_items(self, section):
        items_list = self.config.items(section)
        return items_list
    def is_exit(self,section):  #判断section是否存在
        return (section in self.config)

class WriteConfig:
    def __init__(self):
        self.filepath = configPath
        self.config = configparser.ConfigParser()
        self.config.read(self.filepath)
        self.fp = open(self.filepath,'w')

    def set_option(self,section,name,value):
        self.config.set(section,name,value)


    def add_section(self,section):
        self.config.add_section(section)


    def add_option(self,section,option,value):
        self.config.set(section,option,value)

    def write(self):  #修改配置文件结束后都需要调用改方法写入到配置文件
        self.config.write(self.fp)

def test_read():
    rc = ReadConfig()
    host = rc.get_option('file', 'platform_address')
    items = rc.config.items('file')
    print(items)
def test_write():
    wc = WriteConfig()
    if ('addsection' not in wc.config):
        wc.add_section('addsection')
        wc.add_option('addsection', 'name', 'xiaobialong')
        wc.set_option('addsection', 'name', 'xiaobialong2')
    wc.write()

if __name__ == '__main__':
    #test_read()
    #test_write()
    from interfaceFramework.public import sendRequest, parseConfig, utiles
    config = parseConfig.ReadConfig()
    excel = config.get_option('file', 'platform_address')
    test_data = utiles.read_excel(excel, '三年一班')
    print(test_data)




