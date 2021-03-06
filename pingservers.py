# This tool ping servers and send mail to notify down servers
# Reference: http://stackoverflow.com/questions/64505/sending-mail-from-python-using-smtp

import os
import sys
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

if len(sys.argv) == 1:
    sys.exit("Ex: python pingservers.py 192.168.0.116,192.168.0.150,192.168.0.151,192.168.0.153,192.168.0.216,192.168.0.89,192.168.0.85")
    
servers = list(str(sys.argv[1]).split(','))
upservers = []
downservers = []

for server in servers:
    response = os.system("ping " + server)
    if response == 0:
        upservers.append(server);
    else:
        downservers.append(server);


if len(downservers) > 0:
    msg = MIMEMultipart()
    msg['From'] = 'FROM@gmail.com'
    msg['To'] = 'TO@gmail.com'
    msg['Subject'] = 'Server down'
    message = 'Down servers:' + str(downservers)
    msg.attach(MIMEText(message))

    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login('FROM@gmail.com', 'FROM_PASSWORD')

    mailserver.sendmail('FROM@gmail.com','TO@gmail.com',msg.as_string())

    mailserver.quit()