"""
Optional Email Notification Module
Sends an email with the completed 9-page survey PDF attached
whenever a new response is submitted.
"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_submission_email(submission_data, pdf_path):
    """
    Sends an email with the filled PDF attached.
    Reads config from environment variables (configured in Render or .env):
      - SMTP_HOST (default: smtp.gmail.com)
      - SMTP_PORT (default: 587)
      - SMTP_USER (e.g. your-email@gmail.com)
      - SMTP_PASS (e.g. 16-character Gmail App Password)
      - NOTIFICATION_EMAIL (where forms should be delivered, e.g. dhanukatushar09@gmail.com)
    """
    smtp_user = os.environ.get("SMTP_USER")
    smtp_pass = os.environ.get("SMTP_PASS")
    recipient = os.environ.get("NOTIFICATION_EMAIL", smtp_user)

    # If no email credentials configured, skip silently
    if not smtp_user or not smtp_pass or not recipient:
        return False

    smtp_host = os.environ.get("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.environ.get("SMTP_PORT", 587))

    p_name = submission_data.get("participant_name", "Anonymous")
    sub_id = submission_data.get("submission_id", "")
    sub_date = submission_data.get("submitted_at", "")
    p_contact = submission_data.get("participant_contact", "N/A")

    subject = f"New Survey Submission: {p_name} ({sub_id})"
    
    body = f"""Hello,

A new survey response has been submitted for the AcSIR Societal Program (AcSIR-04-SP):
"Screen Use Behaviour, Digital Habits and Visual Well-being"

Submission Details:
- Submission ID: {sub_id}
- Participant Name: {p_name}
- Contact / Roll No: {p_contact}
- Submitted At: {sub_date}

The completed 9-page filled survey form is attached to this email.

---
AcSIR Research Survey Automated System
"""

    msg = MIMEMultipart()
    msg["From"] = smtp_user
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    if pdf_path and os.path.exists(pdf_path):
        filename = os.path.basename(pdf_path)
        with open(pdf_path, "rb") as f:
            part = MIMEApplication(f.read(), Name=filename)
        part["Content-Disposition"] = f'attachment; filename="{filename}"'
        msg.attach(part)

    try:
        server = smtplib.SMTP(smtp_host, smtp_port, timeout=10)
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)
        server.quit()
        print(f"Email sent successfully for {sub_id} to {recipient}")
        return True
    except Exception as e:
        print(f"Failed to send email notification: {e}")
        return False
