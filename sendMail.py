import time, threading
import smtplib
from smtplib import SMTPAuthenticationError
  
def create_thread(user, pwd, recipient, subject, body, wait):
    threadObj = threading.Thread(target=send_email, args=[user, pwd, recipient, subject, body, wait])
    threadObj.start()
    

def send_email(user, pwd, recipient, subject, body, wait):
    delayTime = time.time() + wait 
    while delayTime > time.time():
        print int(delayTime - time.time())
        time.sleep(0.1)
                
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body
    
    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    #connect to the host(Google)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
    except smtplib.socket.gaierror:
        print "couldn't connect to server"
    
    server.ehlo()
    server.starttls()
    
    #Login with email and pw
    try:
        server.login(gmail_user, gmail_pwd)
    except SMTPAuthenticationError:
        print "authentication error"
    
    server.sendmail(FROM, TO, message)
    server.close()
    print 'successfully sent the mail'
