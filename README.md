# Simple Python Class for sending emails
This is a simple Python Class that uses the smtplib and email packages to send email. Currently the class can only send plain email messages.

Example usage:
```
import SendEmail

# Create an Email object
email_obj = SendEmail.SendEmail()

# Set server address and port. You can also add default values for these in
# the SendEmail class (line 7 and 8), to avoid having to define them every time.
email_obj.smtp_server = "scansmtp.gbs.adm.local"
email_obj.smtp_port = 25

# If your server requires authentication, otherwise this can be omitted:
email_obj.smtp_username = "MySMTPUserName"
email_obj.smtp_password = "MySecretSMTPPassword"

# It isn't mandatory to specify Name on sender and receiver, but we can do it if we want:
email_obj.sender_name = "From Name"
email_obj.receiver_name = "To Name"

# Define subject and body text:
subject = "Test email subject"
message = "Hi,\n\nThis is the email body\n\nRegards,\nPython"

# Sender and receiver:
sender_email = "from@email.com"
receiver_email = "to@email.com"

# Send the email
email_obj.SendEmail(sender_email, receiver_email, subject, message)

```
