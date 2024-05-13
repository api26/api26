# ！ /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2024/4/27 0027 8:49
# Author    : yang
# @File     : send_email_base.py
# @Software : PyCharm

import smtplib
#邮件需要专门的MIME格式
from email.mime.text import MIMEText
#plain指普通文件格式邮件内容
msg = MIMEText("今天天气真好！","plain","utf-8")
#发件人
msg["From"] = "2761978436@qq.com"
#收件人
msg["To"] = "2761978436@qq.com"
#邮件的标题
msg["Subject"] = "邮件标题-美好的一天"

smtp = smtplib.SMTP_SSL("smtp.qq.com")
smtp.login("2761978436@qq.com","jbivqrlddibtdcgh")
smtp.sendmail("2761978436@qq.com","2761978436@qq.com", msg.as_string())
smtp.quit()