#!/usr/bin/env python3

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

filename = "Ally10pm.html"

def send_email_via_smtp(recipient,cc, subject, body):
    try:
        message = MIMEMultipart('alternative')
        message['From'] = 'Tidal-NoReply@apexclearing.com'
        message['To'] = recipient
        message['CC'] = cc
        message['Subject'] = subject
        msg = open(filename,"r")
        #print(msg.read())
        message.attach(MIMEText(msg.read(), 'html'))
        print(message.as_string())
    
        # SMTP session
        session =    smtplib.SMTP('nonauthrelay.apexclearing.local',25)#smtplib.SMTP('smtp.office365.com', 587)  # use outlook's smtp server and port ## Updated to internal relay server
        #session.starttls()  # enable security
        #session.login(sender_address, sender_pass)  # login with mail_id and password
        text = message.as_string()
        session.sendmail('Tidal-NoReply@apexclearing.com', recipient.split(","), text)
        session.quit()
    
    except Exception as e:
        print("Error", e)

email_Subject = 'Ally Critical Data Feeds - Batch Update for 10:00pm CT'
#send_email_via_smtp('TKBatch@invest.ally.com','rmcilveen@apexfintechsolutions.com,arossi@apexfintechsolutions.com, acorales@apexfintechsolutions.com, croaquin@apexfintechsolutions.com, mkulkarni@apexfintechsolutions.com', email_Subject, "") 
send_email_via_smtp('test@example.com','rmcilveen@apexfintechsolutions.com,arossi@apexfintechsolutions.com, acorales@apexfintechsolutions.com, croaquin@apexfintechsolutions.com, mkulkarni@apexfintechsolutions.com', email_Subject, "") 