import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import sys
# sys.path.append("..")
import time
from const import EMAIL_USER_NAME, EMAIL_PASS_WORD



class EmailSender():
    def __init__(self):
        self.host = "smtp.gmail.com"
        self.port = "587"
        self.username = EMAIL_USER_NAME
        self.passwd = EMAIL_PASS_WORD
        self.from_email = self.username
        
    def send_email(self, to_list, link):
        for user, email_address in to_list:
            msg = MIMEMultipart()
            msg["From"] = Header("MagMatual Assessment")
            msg["To"] = Header(user)
            msg["Subject"] = Header("Magmutal Assessment Survey")
            
            text = "Dear {}, <br><br> You are invited to take Magmutal online assessment survey.<br><br>Please register then take the survey in this link: {}<br><br>Contact us if you have any other concerns! <br><br><br>Thanks,<br><br>Best Regards,<br><br>MagMutal Online Assessment Team".format(user, link)
            text_part = MIMEText(text, "html", "utf-8")
            msg.attach(text_part)
            try:
                email_conn = smtplib.SMTP(self.host, self.port)
                email_conn.ehlo()
                email_conn.starttls()
                email_conn.login(self.username, self.passwd)
                email_conn.sendmail(self.from_email, [email_address], msg.as_string())
                print("Send the email meassage successfully!")
            except smtplib.SMTPException as e:
                print(e)
                print ("Fail to send message")
            email_conn.quit()

