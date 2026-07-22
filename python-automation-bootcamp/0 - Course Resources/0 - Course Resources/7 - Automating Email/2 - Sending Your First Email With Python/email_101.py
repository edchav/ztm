import smtplib

sender_email = 'pyautoemail1@gmail.com'
password = 'yjze okyg necd omlx'

with smtplib.SMTP('smtp.gmail.com', 587) as connection:

    connection.starttls()

    connection.login(user=sender_email, password=password)

    connection.sendmail(
        from_addr=sender_email,
        to_addrs=sender_email,
        msg='Subject:Hello...\n\n...World!'
    )