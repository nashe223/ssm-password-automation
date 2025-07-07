import os
import requests
from dotenv import load_dotenv

load_dotenv()

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_slack_alert(message):
    if not SLACK_WEBHOOK_URL:
        print("Slack webhook not set.")
        return

    payload = {
        "text": f"🔐 SSM Password Rotation Alert:\n{message}"
    }

    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=payload)
        response.raise_for_status()
        print("Slack alert sent.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send Slack alert: {e}")
