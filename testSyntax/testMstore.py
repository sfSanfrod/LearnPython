#!/usr/bin/python
#coding=utf-8

from selenium import webdriver
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = u'https://mstore.ppdai.com'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
mobileEmulation = {'deviceName':'Apple iPhone 6'}
options.add_experimental_option('mobileEmulation',mobileEmulation)
driver = webdriver.Chrome(chrome_options=options)
driver.get(url)
sleep(10)