'''
Send an email testing
'''

import smtplib
from urllib.request import urlopen
import datetime as dt
import time

'''
---mail of the receiver
---mail of the sender
---password mail of the sender
'''

RECEIVER = ""
MAIL = ""
PWD =  ""

# run with pythonw
# Send an email at a fixed hour of the day running as a background task

while True:
    if dt.datetime.today().hour == 21:
        ip = urlopen("https://ip.42.pl/raw").read()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(MAIL, PWD)

        msg = f"l'indirizzo ip e' {ip.decode('utf-8')}"
        # from mail - to mail - msg
        server.sendmail(MAIL , RECEIVER, msg)

        server.quit()

        # 1 msg every then it sleeps 1 hour
        time.sleep(60*60)
