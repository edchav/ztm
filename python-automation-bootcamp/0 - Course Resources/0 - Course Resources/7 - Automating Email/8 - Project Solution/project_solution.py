from datetime import date

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

sender_email = 'your email here'
password = 'your app password here'

with open('project_emails.txt', 'r') as emails_file:
    emails = [email.strip() for email in emails_file.readlines()]

emails_string = ', '.join(emails)

subject = f"Status Report for {date.today()}"

message = MIMEMultipart()

message['From'] = sender_email
message['To'] = emails_string
message['Subject'] = subject

with open('customer_complaints.txt', 'rb') as attachment:
    data = attachment.readlines()
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= customer_complaints.txt')

body = f"There are {len(data) - 1} complaints in today's file."

message.attach(MIMEText(body, "plain"))

message.attach(part)

message_string = message.as_string()

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=sender_email, password=password)
    connection.sendmail(from_addr=sender_email, to_addrs=emails, msg=message_string)