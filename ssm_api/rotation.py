import requests

def rotate_secret(ssm_base_url, token, secret_id):
    rotate_url = f"{ssm_base_url}/api/v1/secrets/{secret_id}/change-password"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.post(rotate_url, headers=headers)

    if response.status_code == 204:
        return True
    else:
        print(f"❌ Rotation failed: {response.status_code} - {response.text}")
        return False
