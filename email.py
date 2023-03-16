from email.message import EmailMessage
# from app1 import password
import ssl
import smtplib

email_sender = 'billleynyuy@gmail.com'
email_password = 'bill2002' 
email_receiver='billthegreatempire@gmail.com'

subject = "we are making a deal with you"
body=""".ENGE2101_CA_PROJECT_GROUP_18-1[1].docx"""


em=EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()


with smtplib.SMTP_SSL('smtp.gmail.com',456,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver, em.as_string())
 