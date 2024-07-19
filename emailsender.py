import smtplib, ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr, parseaddr, formatdate
from email.header import Header
import time


#A working product would generate a differnt ID for each client
messageid = '172136491989.19236.1554871168693874964@Jacobys-X13.lan'

port = 465 
smtp_server = "smtp.gmail.com"
sender_email = "securepythonrequest@gmail.com"  

#enviromental variable must be set
password = os.environ.get('secureemail')

#Working product would get the customers email from companies connection on dhsserver.py
receiver_email = "perfecttouchphotoshopping@gmail.com" 

#Send firstime email
def sendmail(content):
    

    msg = MIMEMultipart()
    msg['From'] = formataddr(('Secure', sender_email))
    msg['To'] = receiver_email
    msg['Subject'] = 'Secure Data Hiding Software'
    msg['Date'] = time.strftime("%a, %d %b %Y %H:%M:%S %z")


    msg['Message-ID'] = messageid
    
    

    

    body = f'DO NOT CLICK ON THIS LINK UNTIL INSTRUCTED TO DO SO \n {content}'
    msg.attach(MIMEText(body, 'plain'))
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            
            server.sendmail(sender_email, [receiver_email], msg.as_string())
    except Exception as e:
        print(f"Error: {e}")

    

# reply to the email instructing click on link
def replymail():
    
    #This is an example, wokring product would recieve company information from connection ID on dhsserver.py
    company = 'dell'
    requestedinfo = 'Credit car information'
    reason = 'To pay for monthly subscription'

    # Reply content
    reply_subject = "Request for you information"
    reply_body = f"Click on the link above if you consent to {company} acsessing your {requestedinfo} {reason}"

    # Compose the reply email
    msg = MIMEMultipart()
    msg['From'] = formataddr(('Secure', sender_email))
    msg['To'] = receiver_email
    msg['Subject'] = Header(reply_subject, 'utf-8')
    msg['Date'] = formatdate(localtime=True)

    # References and In-Reply-To headers
    # Typically, these would be extracted from the original email
    msg['In-Reply-To'] = messageid
    msg['References'] = messageid

  
    # Combine reply and original content
    msg.attach(MIMEText(reply_body, 'plain', 'utf-8'))

    # Send the email
    try:
        server = smtplib.SMTP(smtp_server, port)
       
        server.login(sender_email, password)
        server.sendmail(sender_email, [receiver_email], msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")