import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Dict, List
from CONFIG import *

def notify_by_email(matching_appointments: List[Dict]):
    
    server = smtplib.SMTP(email_smtp_server,email_smtp_port)
    server.starttls()
    server.login(email_sender_username, email_sender_password)
    
    #For loop, sending emails to all email recipients
    for recipient in email_recepients:
        message = MIMEMultipart('alternative')
        message['From'] = email_sender_account
        message['To'] = recipient
        message['Subject'] = email_subject
        message.attach(MIMEText(create_email_body(matching_appointments), 'html'))
        text = message.as_string()
        server.sendmail(email_sender_account,recipient,text)

    #All emails sent, log out.
    server.quit()
        
def create_email_body(matching_appointments: List[Dict]) -> str:
    body = "<h1>Available appointments</h1>"
    for index, appointment in enumerate(matching_appointments):
        body += f"<h3>Appointment #:{index}</h3>"
        body += f"<strong> Date: </strong> {appointment['appointmentDt']['date']} <br>"
        body += f"<strong>Day of week: </strong> {appointment['appointmentDt']['dayOfWeek']} <br>"
        body += f"<strong>Start time: </strong> {appointment['startTm']} <br>"
        body += f"<strong>End time: </strong> {appointment['endTm']} <br>"
        body += f"-------------------------------------------------------- <br>"
    return body
