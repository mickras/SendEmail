import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SendEmail:
    def __init__(self):
        self.smtp_server = "mysmtpserver.local"
        self.smtp_port = 25
        self.smtp_username = ""
        self.smtp_password = ""
        self.sender_name = ""
        self.receiver_name = ""

    def SendEmail(self, from_email, to_email, subject, body_text):
        msg = MIMEMultipart()
        msg['From'] = self.sender_name + "<" + from_email + ">"
        msg['To'] = self.receiver_name + "<" + to_email + ">"
        msg['Subject'] = subject
        msg.attach(MIMEText(body_text, 'plain'))

        server = smtplib.SMTP(self.smtp_server, self.smtp_port)

        if len(self.smtp_username) > 0:
            server.login(self.smtp_username, self.smtp_password)

        server.ehlo()
        server.starttls()
        server.ehlo()
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
