import smtplib

gmail_user = ''
gmail_password = ''

#email properties
sent_from = gmail_user
to = ['']
subject = 'Test from Python'
email_text = """
Still just a test. No problems here.
"""

#email send request
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

#TODO

#Understand the try identation and exception capture,
#apply to other projects 

#Further the usage of the script to encompass a particular
#notification use case