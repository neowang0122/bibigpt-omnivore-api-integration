import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class email_sending:
    def send_email(this, sender_password, recipient_email, subject, content):
        # Create a multipart message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject

        # Add the content to the email body
        message.attach(MIMEText(content, "plain"))

        # Connect to the SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)

    # Example usage
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"
    recipient_email = "recipient_email@example.com"
    subject = "Hello"
    content = "This is the email content."

    send_email(sender_email, sender_password, recipient_email, subject, content)