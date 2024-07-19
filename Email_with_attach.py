import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text  import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os #Enter your gmail app passcode

to="js.saroja21@gmail.com"
From="purna32surekha@gmail.com"

#Enter to whom you want to send

subject="Offer Letter"
text="Congratulations you are selected for the respective post"

#body of mail

attach="Email.py" #give your attachment name
msg=MIMEMultipart()
msg["From"]=From
msg["To"]=to
msg["Subject"]=subject
msg.attach(MIMEText(text))

#To load and encode the attachment

part=MIMEBase("application", "octet-stream")
part.set_payload(open(attach,"rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="%s"'%os.path.basename(attach))
msg.attach(part)

#Server Connection Starts...

mailserver=smtplib.SMTP("smtp.gmail.com",587)
mailserver.starttls()
mailserver.login(From,"ietg nctx dldr exti")
mailserver.sendmail(From, to, msg.as_string())
print("Done")
#close the connection
