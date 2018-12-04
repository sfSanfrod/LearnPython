#!/usr/bin/python
#coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header

if __name__=='__main__':
    """发送html形式的邮件"""
    #准备数据
    sender = u'sunfeng163666@163.com'
    reciver = u'985758828@qq.com'
    subject = u'python send text mail测试'
    smtpserver = u'smtp.163.com'
    username = u'sunfeng163666@163.com'
    password = u'XXXXX'
    msg=MIMEText(u'<html><h1>你好，这是html格式的邮件，哇咔咔</h1></html>','html','utf-8')
    msg['Subject']=Header(subject,'utf-8')
    msg['From']=sender
    msg['To']=reciver
    msg.attach()
    #开始发送
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username,password)
    smtp.sendmail(sender,reciver,msg.as_string())
    smtp.quit()