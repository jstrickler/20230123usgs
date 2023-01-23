import smtplib
from datetime import datetime
from imghdr import what  # module to determine image type
from email.message import EmailMessage # module for creating email message
from getpass import getpass # module for reading password privately


SMTP_SERVER = "smtp2go.com"  # global variables for external information (IRL should be from environment -- command line, config file, etc.)
SMTP_PORT = 2525

SMTP_USER = 'pythonclass'

SENDER = 'jstrick@mindspring.com'
RECIPIENTS = ['jstrickler@gmail.com']


def main():
    smtp_server = create_smtp_server()
    now = datetime.now()
    msg = create_message(
        SENDER,
        RECIPIENTS,
        'Here is your attachment',
        'Testing email attachments from python class at {}\n\n'.format(now),
    )
    add_text_attachment('../DATA/parrot.txt', msg)
    add_image_attachment('../DATA/felix_auto.jpeg', msg)
    send_message(smtp_server, msg)


def create_message(sender, recipients, subject, body):
    msg = EmailMessage()  # create instance of EmailMessage to hold message
    msg.set_content(body)  # set content (message text) and various headers
    msg['From'] = sender
    msg['To'] = recipients
    msg['Subject'] = subject
    return msg


def add_text_attachment(file_name, message):
    with open(file_name) as file_in:  # read data for text attachment
        attachment_data = file_in.read()
    message.add_attachment(attachment_data)  # add text attachment to message


def add_image_attachment(file_name, message):
    with open(file_name, 'rb') as file_in:  # read data for binary attachment
        attachment_data = file_in.read()
    image_type = what(None, h=attachment_data)  # get type of binary data
    message.add_attachment(attachment_data, maintype='image', subtype=image_type)  # add binary attachment to message, including type and subtype (e.g., "image/jpg)"


def create_smtp_server():
    password = getpass("Enter SMTP server password:")  # get password from user (don't hardcode sensitive data in script)
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)  # create SMTP server connection
    smtpserver.login(SMTP_USER, password)  # log into SMTP connection

    return smtpserver


def send_message(server, message):
    try:
        server.send_message(message)  # send message
    finally:
        server.quit()


if __name__ == '__main__':
    main()
