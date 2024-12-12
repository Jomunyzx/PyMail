import smtplib, ssl
from email.message import EmailMessage

# Email credentials and recipient details
email_sender = ''
email_sender_password = '' 
email_reciver = ['']  # Can be multiple recipients

# Email content
subject = ''
body = ''

# Create the email object
em = EmailMessage()
em['From'] = email_sender
em['To'] = ', '.join(email_reciver) 
em['Subject'] = subject
em.set_content(body)

# Establish a secure connection and send the email
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_sender_password)
    smtp.sendmail(email_sender, email_reciver, em.as_string())