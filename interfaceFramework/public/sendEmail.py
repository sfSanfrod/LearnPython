#!/usr/bin/env python
#coding=utf-8

__author__ = '小白龙'

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from interfaceFramework.public import parseConfig

config = parseConfig.ReadConfig()

class SendEmail():
    def __init__(self,report_path):
        self.report_path = report_path
        # if str(config.get_option('email','sender')).__contains__('163.com'):
        #     self.smtserver = r'smtp.163.com'
        self.smtserver = r'smtp.163.com'
        recivers = []
        for reciver in str(config.get_option('email','recivers')).split(','):
            recivers.append(reciver)
        self.reciver = ";".join(recivers)
        self.sender = config.get_option('email','sender')
        self.username = config.get_option('email','username')
        self.passwd = config.get_option('email','passwd')
        self.msg = None

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
        file = open(self.report_path,'rb').read()
        text_file = MIMEText(file,'base64', 'utf-8')
        text_file['Content-Type'] = 'application/octet-stream'
        text_file["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        msg.attach(text_file)
        self.msg = msg

    def send_email(self):
        self.set_email()
        smtp = smtplib.SMTP()
        smtp.connect(self.smtserver)
        smtp.login(self.username,self.passwd)
        smtp.sendmail(self.sender,self.reciver,self.msg.as_string())

if __name__ == '__main__':
    mail = SendEmail(r'D:\testReport.html')
    mail.send_email()
    print(mail.reciver)
