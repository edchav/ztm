import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["From"] = "Edgar R. Chavez"
email["To"] = "ed5chavez5@gmail.com"
email['Subject'] = "You won a billion dollars!!"

email.set_content("You've been scammed")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo() # look up why its ehlo() interesting story, but it's just used to check if the server is awake
    smtp.starttls() # encryption mechanism
    smtp.login("", "") # input your own gmail and password need to use app password did not get it to work

    smtp.send_message(email)
    print('all good boss')