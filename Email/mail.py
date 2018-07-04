import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#input your email id and your password.
email=input("input your Email id : ")
password=input("Enter your password : ")

#call the server
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.connect("smtp.gmail.com", 465)
server.login(email, password)

fromaddr = email
#input target email id, subject.
toaddr = str(input("Enter the target Email address : "))
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = str(input("Subject : "))
#input body.
body = str(input("Input the message : "))
msg.attach(MIMEText(body, 'plain'))

#input the file you want to attach and send.
filename = "name of the attachment.txt"
attachment = open("file.txt", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)

text=msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

