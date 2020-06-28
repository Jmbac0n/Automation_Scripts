import smtplib, uuid, datetime

#Switch
switch = True

#Find MAC address of computer
mac = MAC = (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1]))

#Find date and time of alert creation
date_time = datetime.datetime.now()

#Email credentials for sending alerts
gmail_user = ''
gmail_password = ''

#email properties
sent_from = gmail_user
to = ['']
#subject = 'USB Alert'
email_text = ("""\
Subject: USB Alert\n
USB ping!

Date + Time: %s
MAC Address: %s
""" % (str(date_time), (mac)))

#Condition of sending email notification

if switch == True:
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465) #Sets up SMTP server, SSL and port 465
        server.ehlo() #Identifies you to server
        server.login(gmail_user, gmail_password) #Sender's details
        server.sendmail(sent_from, to, email_text) #Send details
        server.close() #Closes server

        print('Email sent')
    except Exception as e:
        print(e)
        print('Something went wrong')
else:
    print("Nope")