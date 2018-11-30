#!/usr/bin/env python
#coding=utf-8

import configparser

class readConfig:
    def __init__(self,filepath):
        self.filepath = filepath
        self.config = configparser.ConfigParser()
        self.config.read(self.filepath)

    def read_option(self,section,name):
        value = self.config.get(section,name)
        return value
    def read_sections(self):
        section_list = self.config.sections()
        return section_list
    def read_items(self,section):
        items_list = self.config.items(section)
        return items_list
    def is_exit(self,section):  #判断section是否存在
        return (section in self.config)

class writeConfig:
    def __init__(self,filepath):
        self.filepath = filepath
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

if __name__ == '__main__':
    rc = readConfig(r"D:\GitHub\config.ini")
    host = rc.read_option('DATABASE', 'host')
    items = rc.config.items('DATABASE')
    print(items)

    wc = writeConfig(r"D:\GitHub\config.ini")
    if ('info' not in wc.config):
        wc.add_section('info')
    wc.add_option('info','name','xiaobialong')
    wc.set_option('info','name','xiaobialong2')
    wc.write()