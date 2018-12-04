#!/usr/bin/env python
#coding=utf-8

__author__ = '小白龙'

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

class SendEmail():
    def __init__(self):
        self.msg = None
        self.smtserver = r'smtp.163.com'

        revivers = ['985758828@qq.com','sunfeng163666@163.com']
        self.reciver = ";".join(revivers)
        self.sender = 'sunfeng163666@163.com'
        self.username = r'sunfeng163666@163.com'
        self.passwd = r'XXXXXX'

    def set_email(self):

        subject = r'InterfaceTestReport发送邮件（正常）'

        #构造附件
        msg = MIMEMultipart('mixed')
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = self.reciver
        #构造文本
        text = r'Hi all，' \
               r'这里是神州项目二期接口测试报告，报告地址：http://www.baidu.com' \
               r'详情请见附件，谢谢！'
        text_plain = MIMEText(text,'plain', 'utf-8')
        msg.attach(text_plain)
        #构造html
        html = """
                <html>  
                <head></head>  
                    <body>  
                        <p>Hi!<br>  
                        How are you?<br>  
                        Here is the <a href="http://www.baidu.com">link</a> you wanted.<br> 
                        </p> 
                    </body>  
                </html>  
                """
        text_html = MIMEText(html,'html','utf-8')
        text_html["Content-Disposition"] = 'attachment; filename="texthtml.html"'
        msg.attach(text_html)
        #添加文件
        file = open(r'D:\testReport.html','rb').read()
        text_file = MIMEText(file,'base64', 'utf-8')
        text_file['Content-Type'] = 'application/octet-stream'
        text_file["Content-Disposition"] = 'attachment; filename="report.html"'
        msg.attach(text_file)
        self.msg = msg

    def send_email(self):
        smtp = smtplib.SMTP()
        smtp.connect(self.smtserver)
        smtp.login(self.username,self.passwd)
        smtp.sendmail(self.sender,self.reciver,self.msg.as_string())

if __name__ == '__main__':
    mail = SendEmail()
    mail.set_email()
    mail.send_email()