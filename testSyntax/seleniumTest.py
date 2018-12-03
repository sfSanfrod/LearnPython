#!/usr/bin/python
#coding=utf-8

from selenium import webdriver
from time import sleep

import sys
reload(sys)
sys.setdefaultencoding(u'utf-8')


def testQQEmail(url):

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(chrome_options=options)

    driver.get(url)
    print(u'已打开浏览器')
    #输入用户名密码
    driver.find_element_by_id('inputuin').clear()
    driver.find_element_by_id('inputuin').send_keys(u'sunfeng@qbao.com')
    driver.find_element_by_id('pp').clear()
    driver.find_element_by_id('pp').send_keys(u'Sunfeng123')
    sleep(1)
    #5天内自动登录
    driver.find_element_by_xpath(u'//input[@id="ss" and @type="checkbox"]').click()
    sleep(1)
    driver.find_element_by_xpath(u'//input[@id="ss" and @type="checkbox"]').click()
    sleep(1)
    #提交登录
    driver.find_element_by_name(u'btlogin').submit()
    print(u'登录中。。。')
    sleep(10)
    #验证登录
    usernameEle = driver.find_element_by_xpath(u'//div[@class="td_new_user_info"]//a[@class="nt_nickname"]')
    username = usernameEle.get_attribute("text")
    print(username.isDisplayed())
    print(username)
    print(u'登录成功')

    sleep(30)

if __name__=='__main__':
    url = u'https://exmail.qq.com/cgi-bin/loginpage?t=dm_loginpage&dmtype=bizmail'
    testQQEmail(url)