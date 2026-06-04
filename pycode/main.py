import smtplib
from email.message import EmailMessage

# Create the email
msg = EmailMessage()
msg["Subject"] = "Test Email"
msg["From"] = "cteshops@outlook.com"
msg["To"] = "cteshops@gmail.com"
msg.set_content("Hello from Python!")

# Outlook SMTP settings
SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587

USERNAME = "cteshops@outlook.com"
PASSWORD = "Cso#20266202"

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()  # Encrypt connection
    server.login(USERNAME, PASSWORD)
    server.send_message(msg)

print("Email sent successfully!")