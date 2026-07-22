#import stuff

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import random


#create MIME object

password = 'yjze okyg necd omlx'

sender_email = 'pyautoemail1@gmail.com'
#receiver_email = 'pyautoemail1@gmail.com'
subject = 'Daily Dose of Inspiration'

#import emails

with open('Emails.txt') as file:
    emails = [email.strip() for email in file.readlines()]

emails_string = ', '.join(emails)

message = MIMEMultipart()

message['From'] = sender_email
message['To'] = emails_string
message['Subject'] = subject


#import data from text file

with open('Business Cliches.txt') as file:
    cliches = file.readlines()

body = random.choice(cliches)

message.attach(MIMEText(body, 'plain'))


#attach airhorn mp3 file

with open('airhorn.mp3', 'rb') as attachment:
    part = MIMEBase('application','octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename=airhorn.mp3')

message.attach(part)

message_string = message.as_string()


#send email with smtplib

with smtplib.SMTP('smtp.gmail.com', 587) as connection:

    connection.starttls()

    connection.login(user=sender_email, password=password)

    connection.sendmail(
        from_addr=sender_email,
        to_addrs=emails,
        msg=message_string
    )




