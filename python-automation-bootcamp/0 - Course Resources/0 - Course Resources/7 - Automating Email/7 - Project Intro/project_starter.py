# TODO 1: Import required modules from datetime, smtplib, and email packages

    # TODO 1a: Import the date class from the datetime module
    # Hint: Use 'from datetime import date'.

    # TODO 1b: Import smtplib for handling the sending of emails
    # Hint: Just use 'import smtplib'.

    # TODO 1c: From the email.mime.multipart module, import MIMEMultipart
    # Hint: Use 'from email.mime.multipart import MIMEMultipart'.

    # TODO 1d: From the email.mime.text module, import MIMEText
    # Hint: Use 'from email.mime.text import MIMEText'.

    # TODO 1e: From the email.mime.base module, import MIMEBase
    # Hint: Use 'from email.mime.base import MIMEBase'.

    # TODO 1f: Import the encoders from the email package
    # Hint: Use 'from email import encoders'.


# TODO 2: Set up email sender credentials

    # TODO 2a: Assign the email address you're sending from to a variable as a string

    # TODO 2b: Assign your app password to a variable as a string


# TODO 3: Read the list of recipient emails from a text file and process it

    # TODO 3a: Open the file 'project_emails.txt' in read mode
    # Hint: Use a 'with' statement to open the file.

    # TODO 3b: Read the email addresses into a list
    # Hint: Use the 'readlines' method to get each line of the file as a list element.

    # TODO 3c: Process the list of emails using a list comprehension, and assign the result to a variable
    # Hint: Use a list comprehension to strip whitespace and newline characters from each email.
    # Example: [email.strip() for email in email_list]

    # TODO 3d: Join the processed emails into a single string separated by commas, and assign the result to another variable
    # Hint: Use the 'join' method with ', ' as the separator on the processed list of emails.
    # Example: ', '.join(processed_emails)


# TODO 4: Prepare the email

    # TODO 4a: Create a subject line for the email that includes today's date, and assign the result to a variable
    # Hint: Use 'date.today()' to insert today's date into an "f string".

    # TODO 4b: Initialize a MIMEMultipart object for the email message, and assign the result to a variable

    # TODO 4c: Set the 'From', 'To', and 'Subject' fields of the email
    # Hint: The 'To' field should be that string of email addresses separated by commas.


# TODO 5: Attach a file to the email

    # TODO 5a: Open the 'customer_complaints.txt' file in binary read mode
    # Hint: Use a 'with' statement and open the file with 'rb' mode.

    # TODO 5b: Create a MIMEBase object for the attachment, and assign the result to a variable
    # Hint: Use MIMEBase with "application" and "octet-stream" as parameters.

    # TODO 5c: Set the payload of the MIMEBase object with the content of the file by reading the file content
    # Hint: Use the 'read' method on the file object to get its content, then pass this content to the 'set_payload' method of the MIMEBase object.

    # TODO 5d: Encode the attachment in base64
    # Hint: Pass the MIMEBase object to the 'encoders.encode_base64' function.

    # TODO 5e: Add a header to the MIMEBase object for the email attachment
    # Hint: Use the 'add_header' method of the MIMEBase object, with 'Content-Disposition' and 'attachment; filename= customer_complaints.txt' as parameters.

    # TODO 5f: Attach the MIMEBase object to the email message
    # Hint: Use the 'attach' method of the MIMEMultipart object with the MIMEBase object as a parameter.


# TODO 6: Attach a plain text body to the email

    # TODO 6a: Determine the number of complaints in the 'customer_complaints.txt' file
    # Hint: You can count the number of complaints directly within the context manager used for attaching the file.
    #       You can use the readlines() method inside the context manager to get a list of lines.
    #       Count the number of lines using 'len()' and subtract 1 for the header.

    # TODO 6b: Create the email body with the count of complaints
    # Hint: Format a string that includes the number of complaints, e.g., "There are X complaints in today's file."

    # TODO 6c: Attach the email body to the message as plain text
    # Hint: Use MIMEText with the body string (produced in the previous step) and the word "plain" as parameters, then attach it using the 'attach' method of the MIMEMultipart object.


# TODO 7: Convert the email message to a string
# Hint: Use the 'as_string' method of the email message object.


# TODO 8: Send the email

    # TODO 8a: Connect to the Gmail SMTP server using smtplib
    # Hint: Use smtplib.SMTP with the 'smtp.gmail.com' server and port 587.

    # TODO 8b: Start TLS for email security
    # Hint: Use the 'starttls' method of the SMTP connection object.
    #       This step is crucial for encrypting your email to ensure secure transmission over the Internet.

    # TODO 8c: Log in to the email server using the sender's credentials
    # Hint: Use the 'login' method of the SMTP connection object.
    #       Pass your sender email and app password as arguments to authenticate.

    # TODO 8d: Send the email using the 'sendmail' method
    # Hint: Use the 'sendmail' method of the SMTP connection object to send the email.
    #       The 'from_addr' parameter should be the sender's email address.
    #       The 'to_addrs' parameter should be the list of recipient emails.
    #       The 'msg' parameter should be the email message string you created earlier.
    #       Example: connection.sendmail(from_addr=sender_email, to_addrs=emails, msg=message_string)
