#!/usr/bin/env python
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

SMTP_SERVER = "smtpcorp.com"
SMTP_PORT = 2525
SMTP_USER = 'jstrickpython'
SMTP_PWD = 'python(monty)'

SENDER = 'jstrick@mindspring.com'
RECIPIENTS = ['jstrickler@gmail.com']

msg = MIMEMultipart("Please enjoy this picture of a chimp")
msg['Subject'] = "A chimp for you"

file_name = '../DATA/chimp.bmp'
with open(file_name, 'rb') as file_in:
    attachment_data = file_in.read()

    short_name = os.path.basename(file_name)
    attachment = MIMEImage(attachment_data)
    attachment.add_header(
        'Content-Disposition', 'attachment', filename=short_name
    )

    msg.attach(attachment)

smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
smtp.login(SMTP_USER, SMTP_PWD)

smtp.sendmail(
    SENDER,
    RECIPIENTS,
    msg.as_string()
)
