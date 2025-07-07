from ssm_api.gmail_sender import send_email_via_gmail_api
import os
from dotenv import load_dotenv

load_dotenv()

# Test send
send_email_via_gmail_api(
    subject="Test Email from SSM Script",
    body="This is a test alert from your Python script using Gmail API.",
    to_email=os.getenv("EMAIL_TO")
)
