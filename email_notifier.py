"""
Email Notification Module
Sends an email with the completed 9-page survey PDF attached
whenever a new response is submitted.
"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

DEFAULT_RECIPIENT = "dhanukatushar9@gmail.com"

def send_submission_email(submission_data, pdf_path):
    """
    Sends an email with the filled PDF attached to dhanukatushar9@gmail.com.
    """
    smtp_user = os.environ.get("SMTP_USER", DEFAULT_RECIPIENT).strip()
    smtp_pass = os.environ.get("SMTP_PASS", "").strip()
    recipient = os.environ.get("NOTIFICATION_EMAIL", DEFAULT_RECIPIENT).strip()

    # If no app password configured, skip
    if not smtp_pass:
        print("Email notification skipped: SMTP_PASS (Gmail App Password) not set in Environment.")
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
-------------------
• Submission ID: {sub_id}
• Participant Name: {p_name}
• Contact / Roll No: {p_contact}
• Submitted At: {sub_date}

The completed 9-page survey form with all checked boxes is attached to this email.

---
AcSIR Research Survey Automated System
"""

    msg = MIMEMultipart()
    msg["From"] = smtp_user
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain", "utf-8"))

    if pdf_path and os.path.exists(pdf_path):
        filename = os.path.basename(pdf_path)
        with open(pdf_path, "rb") as f:
            part = MIMEApplication(f.read(), Name=filename)
        part["Content-Disposition"] = f'attachment; filename="{filename}"'
        msg.attach(part)

    try:
        server = smtplib.SMTP(smtp_host, smtp_port, timeout=15)
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)
        server.quit()
        print(f"SUCCESS: Email sent for {sub_id} to {recipient}")
        return True
    except Exception as e:
        print(f"ERROR: Failed to send email notification: {e}")
        return False
