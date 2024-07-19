
#Sending a simple email using python
#smptlib-->Simple mail transfer protocol
#Email OTP Aythentication

import random #(To generate numbers randomly)
import math      #(To calculate)
import smtplib  #(To tranfer the mail)


#we will generate a 6 digit otp by taking base digits

digits="0123456789"
OTP="" #empty string


#Now we will use math module along with module to generate a customized 6 digit otp
#floor means base value

for i in range(6):
    OTP+=digits[math.floor(random.random()*10)] #(Assignment operator ocnsider updated value)
    #print(OTP)
otp=OTP+"is your OTP"
msg=otp


#include our email automation

s=smtplib.SMTP("smtp.gmail.com",587) #source mail
s.starttls()
s.login("purna32surekha@gmail.com","ietg nctx dldr exti")
user="purna32surekha@gmail.com"
emailid=input("Enter the mail which you to send the opt:")
s.sendmail(user,emailid,msg)
while True:
    a=input("Enter your otp: ")
    if a==OTP:
        print("OTP Crrct")
    else:
        print("Invalid OTP")
