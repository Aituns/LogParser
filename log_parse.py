from email.mime import text
import smtplib, ssl
from email.mime.text import MIMEText

def sendEmail(text, countInfected):
    smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
    smtp_ssl_port = 465
    username = ''
    password = '' 
    sender = '@gmail.com'
    targets = ['@gmail.com']

    msg = MIMEText("Virus Locations \n" + text)
    msg['Subject'] = 'Found ' + str(countInfected) + ' infected file(s)'
    msg['From'] = sender
    msg['To'] = ', '.join(targets)

    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(sender, targets, msg.as_string())
    server.quit()               

def logParse():
    num_lines = sum(1 for line in open('clamav.log')) - 1
    f = open("clamav.log", 'r')
    contents = f.readlines()
    x = contents[num_lines - 6].split(': ')
    totalInfectedFiles = int(x[1])
    
    if (totalInfectedFiles > 0):
        text = ""
        for i in range(totalInfectedFiles):
            text += contents[num_lines - 13 - i]
        sendEmail(text, totalInfectedFiles)