import smtplib, ssl
import os

port = 465 
smtp_server = "smtp.gmail.com"
sender_email = "securepythonrequest@gmail.com"  
receiver_email = "perfecttouchphotoshopping@gmail.com" 

#enviromental variable must be set
password = os.environ.get('dhsemail')

message = "Test secure email"


context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


