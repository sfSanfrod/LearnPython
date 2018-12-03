#!/usr/bin/python
#coding:utf-8

import logging
import logging.config

def testLog01():
    print(u'testLog01')
    logging.basicConfig(level=logging.DEBUG,format="%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s",datefmt='%Y-%m-%d %H:%M:%S',filename='testLog01.log',filemode='w')
    ###################################################
    logging.debug(u'这是bug级别的日志记录')
    logging.info(u'这是提示信息级别的日志记录')
    logging.warning(u'这是警告级别的日志记录')

def testLog02():
    print(u'testLog02')
    logging.basicConfig(level=logging.DEBUG,format="%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s",datefmt='%a,%d %b %Y %H:%M:%S',filename='testLog02.log',filemode='w')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-10s:%(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    ###################################################
    logging.debug(u'这是bug级别的日志记录')
    logging.info(u'这是提示信息级别的日志记录')
    logging.warning(u'这是警告级别的日志记录')

def testLogdemo1():
    print(u'testLogdemo1')
    logging.config.fileConfig("logger.conf")
    logger = logging.getLogger("demo01")
    ###################################################
    logging.debug(u'这是bug级别的日志记录')
    logging.info(u'这是提示信息级别的日志记录')
    logging.warning(u'这是警告级别的日志记录')

def testLogdemo2():
    print(u'testLogdemo2')
    logging.config.fileConfig("logger.conf")
    logger = logging.getLogger("demo02")
    ###################################################
    logging.debug(u'这是bug级别的日志记录')
    logging.info(u'这是提示信息级别的日志记录')
    logging.warning(u'这是警告级别的日志记录')


if __name__ == '__main__':
    #testLog01()
    #testLog02()
    #testLogdemo1()
    testLogdemo2()
