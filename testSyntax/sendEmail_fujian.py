#!/usr/bin/python
#coding=utf-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

if __name__=='__main__':
    """测试发送带附件的邮件"""
    # 准备数据
    sender = u'sunfeng163666@163.com'
    reciver = u'sunfeng163666@163.com'
    subject = u'会议很好邮件8'
    smtpserver = u'smtp.163.com'
    username = u'sunfeng163666@163.com'
    password = u'ssf5762172'
    #构造附件
    msg = MIMEMultipart('附件')
    msg['Subject']=Header(subject,'utf-8')
    attachment = MIMEText(open(r'D:\testReport.html').read(),'base64',encoding='utf-8') # 读取附件
    attachment['Content-Type']='application/octet-stream'
    attachment['Content-Disposition']='attachment;filename="tianqi.html"'
    msg.attach(attachment)   #关联附件
    #添加正文
    text = MIMEText(u'今天的会议非常成功，明天一起出去玩吧', 'plain', 'utf-8')
    msg.attach(text)

    msg['From']=sender
    msg['To']=reciver
    #开始发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username,password)
    smtp.sendmail(sender,reciver,msg.as_string())
    smtp.quit()