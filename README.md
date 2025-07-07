# 🔐 SSM Password Automation

A secure, alert-enabled script for rotating secrets via the Delinea (Secret Server) API — with Slack and Gmail API notifications on failure.

---

## 🚀 Features

- Authenticates with Delinea Secret Server (SSM)
- Rotates a target secret's password
- Logs actions to `rotation.log`
- Sends Slack alerts on failure
- Sends secure email alerts using Gmail API
- Configurable via `.env` (no secrets in code)

---

## 🧰 Tech Stack

- Python 3.10+
- `requests`, `python-dotenv`, `Flask` (mock server)
- Gmail API (`google-auth`, `google-api-python-client`)
- Slack Webhook integration

---

## ⚙️ Setup Instructions

### 1. Clone the repo and install dependencies

```bash
git clone https://github.com/yourusername/ssm-password-automation.git
cd ssm-password-automation
python -m venv venv
source venv/Scripts/activate  # or venv/bin/activate on macOS/Linux
pip install -r requirements.txt
