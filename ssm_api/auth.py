import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Load Secret Server credentials from .env
SSM_BASE_URL = os.getenv("SSM_BASE_URL")
SSM_USERNAME = os.getenv("SSM_USERNAME")
SSM_PASSWORD = os.getenv("SSM_PASSWORD")

def get_access_token():
    auth_url = f"{SSM_BASE_URL}/oauth2/token"
    payload = {
        "username": SSM_USERNAME,
        "password": SSM_PASSWORD,
        "grant_type": "password"
    }

    try:
        response = requests.post(auth_url, data=payload)
        response.raise_for_status()
        return response.json()["access_token"]
    except requests.exceptions.RequestException as e:
        raise Exception(f"Auth failed: {e}")

