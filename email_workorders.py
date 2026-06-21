import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from pathlib import Path

def send_email(to_email: str, excel_file_path: str):
    from_email = "EMAIL PLACEHOLDER"
    smtp_server = "SMTP PLACEHOLDER"
    smtp_port = 000

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "SUBJECT PLACEHOLDER"

    body = "BODY PLACEHOLDER"
    msg.attach(MIMEText(body, 'plain'))

    file_path = Path(excel_file_path)
    if not file_path.exists():
        print (f"Error: Attatched file {file_path.name} not found.")
        return
    
    with open(file_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename = {file_path.name}",
    )
    msg.attach(part)
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            # server.login(from_email, "IF AUTHENTICATION REQUIRED, APP PASSWORD PLACEHOLDER")
            server.send_message(msg)
        print(f"Successfully sent email to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {e}")

