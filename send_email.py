import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "david.e.gress@gmail.com"
    password = os.getenv("PASSWORD") # osgsdxzjueuajbsb"
    receiver = "david.e.gress@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


#send_email()
