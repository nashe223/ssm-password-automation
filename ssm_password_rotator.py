import os
import logging
from dotenv import load_dotenv
from ssm_api.auth import get_access_token
from ssm_api.rotation import rotate_secret
from ssm_api.notifier import send_slack_alert
from ssm_api.gmail_sender import send_email_via_gmail_api


# Load environment variables
load_dotenv()

# Set up logging
LOG_PATH = 'logs/rotation.log'
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)  # Create logs folder if missing

logging.basicConfig(
    filename=LOG_PATH,
    filemode='a',
    format='%(asctime)s %(levelname)s: %(message)s',
    level=logging.INFO
)

# Get config values
SSM_BASE_URL = os.getenv("SSM_BASE_URL")
SECRET_ID = os.getenv("SECRET_ID")

def main():
    try:
        token = get_access_token()
        logging.info("✅ Authenticated with Secret Server.")
        print("Authenticated.")

        success = rotate_secret(SSM_BASE_URL, token, SECRET_ID)
        if success:
            logging.info(f"🔁 Password rotated successfully for Secret ID {SECRET_ID}")
            print("Password rotation successful.")
        else:
            
            error_msg = f"❌ Password rotation failed for Secret ID {SECRET_ID}"
            logging.error(error_msg)
            send_slack_alert(error_msg)
            send_email_via_gmail_api("SSM Rotation Failed", error_msg, os.getenv("EMAIL_TO"))
            print("Password rotation failed.")

    except Exception as e:
        error_msg = f"❌ Error occurred: {e}"
        logging.error(error_msg)
        send_slack_alert(error_msg)
        send_email_via_gmail_api("SSM Rotation Error", str(e), os.getenv("EMAIL_TO"))
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
