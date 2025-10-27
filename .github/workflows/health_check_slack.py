import requests
import sys
import os
import time

API_URL = os.getenv("API_URL", "http://localhost:3000/usuarios")
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

def send_slack_alert(message, emoji="⚠️"):
    if not SLACK_WEBHOOK:
        print("⚠️ Nenhum webhook configurado. Ignorando alerta.")
        return
    payload = {"text": f"{emoji} {message}"}
    requests.post(SLACK_WEBHOOK, json=payload)

def check_api(url):
    try:
        r = requests.get(url, timeout=3)
        if r.status_code == 200:
            print("✅ API está online!")
            return True
        else:
            print(f"⚠️ Status {r.status_code}")
            return False
    except requests.exceptions.RequestException:
        print("❌ API fora do ar!")
        return False

for attempt in range(1, 4):
    if check_api(API_URL):
        sys.exit(0)
    else:
        time.sleep(2)

send_slack_alert(f"A API {API_URL} está fora do ar! ❌")
sys.exit(1)
