import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from typing import Tuple
import os

user = os.getenv('EMAIL_USER')
password = os.getenv('EMAIL_PASSWORD')
name = os.getenv('EMAIL_NAME')
address = os.getenv('EMAIL_FROM')
smtp_address = os.getenv('SMTP_ADDRESS')
port = os.getenv('SMTP_PORT', 587)

to = os.getenv('EMAIL_TO')
cc = os.getenv('EMAIL_CC', '')
cco = os.getenv('EMAIL_CCO', '')

assert any([to, cc, cco])

all_recipients = []
all_recipients.extend(to.split(','))
all_recipients.extend(cc.split(','))
all_recipients.extend(cco.split(','))

def send(content, subject="", files: list[Tuple]=[]):
    with smtplib.SMTP(smtp_address, port) as server:
        server.starttls()
        server.login(user, password)
        
        msg = create_message(content, subject, files)
        server.send_message(msg, from_addr=address, to_addrs=all_recipients)

def create_message(content='', subject='', files: list[Tuple]=[]):
    msg = MIMEMultipart()
    msg['From'] = f'{name} <{address}>'
    msg['Subject'] = subject
    msg['To'] = to
    msg['Cc'] = cc

    msg.attach(MIMEText(content, 'html', 'utf-8'))
    attach_files(msg, files)
    
    return msg

def attach_files(msg: MIMEMultipart, files: list[Tuple]=[]):
    for name, content in files:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(content)
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename="{name}"')
        msg.attach(part)