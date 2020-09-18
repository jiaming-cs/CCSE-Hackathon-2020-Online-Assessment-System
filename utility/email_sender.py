import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import sys
# sys.path.append("..")
import time
from const import EMAIL_USER_NAME, EMAIL_PASS_WORD, SCORE_NOTIFICATION_EMAIL_TEMPLATE, INVITATION_EMAIL_TEMPLATE
from utility.pie_chart import make_pie_chart



class EmailSender():
    def __init__(self):
        self.host = "smtp.gmail.com"
        self.port = "587"
        self.username = EMAIL_USER_NAME
        self.passwd = EMAIL_PASS_WORD
        self.from_email = self.username
        
    def send_invitation(self, to_list, link):
        for user, email_address, password in to_list:
            msg = MIMEMultipart()
            msg["From"] = Header("MagMatual Assessment")
            msg["To"] = Header(user)
            msg["Subject"] = Header("Magmutal Assessment Survey")
            
            text = INVITATION_EMAIL_TEMPLATE.format(name = user, email = email_address, password = password, link = link)
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
    
    def send_score(self, user, email_address, score, suggesions_dict):
        msg = MIMEMultipart()
        msg["From"] = Header("MagMatual Assessment")
        msg["To"] = Header(user)
        msg["Subject"] = Header("Magmutal Assessment Survey Score")
        
        text = SCORE_NOTIFICATION_EMAIL_TEMPLATE.format(name = user, score = score, suggestions = "<br><br>".join(list(suggesions_dict.keys())))
        text_part = MIMEText(text, "html", "utf-8")
        msg.attach(text_part)

        make_pie_chart(suggesions_dict)
        with open("./graphs/pie_chart.png", "rb") as f:
            msg_image = MIMEImage(f.read())
        msg_image.add_header('Content-ID', '<chart>')
        msg.attach(msg_image)
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

