#!/usr/bin/python
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

def send_mail(send_from, send_to, subject, text, files=[], server="smtp.gmail.com"):
  assert type(send_to)==list
  assert type(files)==list

  msg = MIMEMultipart()
  msg['From'] = send_from
  msg['To'] = COMMASPACE.join(send_to)
  msg['Date'] = formatdate(localtime=True)
  msg['Subject'] = subject

  msg.attach( MIMEText(text) )

  for f in files:
    part = MIMEBase('application', "octet-stream")
    part.set_payload( open(f,"rb").read() )
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
    msg.attach(part)

  smtp = smtplib.SMTP(server)
  smtp.sendmail(send_from, send_to, msg.as_string())
  smtp.close()

send_mail('lau.joe.a@gmail.com', 'mcfa77y@gmail.com', 'job test', 'thanks to hire me',['attachment.txt'])


https://mail.google.com/mail/?view=cm
&fs=1&to=Herbnj%40gmail.com
&su=Profitable%20e-commerce%20site%20seeks%20Java%20Dev%20-Server%20Side%20Dev%20(SOMA%20%2F%20south%20beach)
&body=%0A%0Ahttp%3A%2F%2Fsfbay.craigslist.org%2Fsfc%2Fsof%2F3889019682.html%0A
&tf=1

https://www.dropbox.com/s/tz1iv5ummf9dkpz/JoeLau-Resume-5-10-2013.doc