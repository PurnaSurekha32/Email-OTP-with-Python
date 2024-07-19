
#Now we will add subject and make sure to address is visible along with body of email using email package

import smtplib  #simple mail transfer protocol
#mime---->Multi purpose Internet Mail Extension
#Protocol----->Any format(PPt,Doc,Png,Files...etc)

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText # All the mail's are in text format

#defining data
From="purna32surekha@gmail.com"  #Give your email Id
to="js.saroja21@gmail.com" # Give receiver gmail Id
subject="Pandi OTP" #Give your own subject
msg=MIMEMultipart()
msg["From"]=From
msg["To"]=to
msg["Subject"]=subject
body="Hello! first mail using python script"
msg.attach(MIMEText(body,"plain"))
text=msg.as_string()

#same usage of smtplib to start the process #Common step for email

server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

#Next, log in to the server

server.login(From, "ietg nctx dldr exti")

#Give your app passcode here , Send Email

server.sendmail(From,to,text)
print("Mail Sent")
server.quit()
