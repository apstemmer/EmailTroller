class AddressDetails(object):
    def __init__(self, toaddr, fromaddr, password, smtp, port):
        self.toaddr = toaddr
        self.fromaddr = fromaddr
        self.pw = password
        self.smtp = smtp
        self.port = port


def sendMail(subject, body, addrInfo):

    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText
    
    msg = MIMEMultipart()
    msg['From'] = addrInfo.fromaddr
    msg['To'] = addrInfo.toaddr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP(addrInfo.smtp, addrInfo.port)
    server.starttls() # secure connection
    server.login(addrInfo.fromaddr, addrInfo.pw)
    text = msg.as_string()
    server.sendmail(addrInfo.fromaddr, addrInfo.toaddr, text)
    server.quit()