#import stuff

import smtplib
from email.mime.text import MIMEText
import random


#create MIME object

password = 'yjze okyg necd omlx'

sender_email = 'pyautoemail1@gmail.com'
receiver_email = 'pyautoemail1@gmail.com'
subject = 'Daily Dose of Inspiration'

message = MIMEMultipart()

message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject


#import data from text file

with open('Business Cliches.txt') as file:
    cliches = file.readlines()

body = random.choice(cliches)

message.attach(MIMEText(body, 'plain'))

message_string = message.as_string()


#send email with smtplib

with smtplib.SMTP('smtp.gmail.com', 587) as connection:

    connection.starttls()

    connection.login(user=sender_email, password=password)

    connection.sendmail(
        from_addr=sender_email,
        to_addrs=receiver_email,
        msg=message_string
    )




