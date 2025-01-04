import requests
from config.settings import TELEGRAM_URL, BOT_TOKEN


def send_telegram_message(chat_id, message):
    params = {
        "text": message,
        "chat_id": chat_id,
    }
    response = requests.get(f"{TELEGRAM_URL}{BOT_TOKEN}/send_message", params=params)
    if response.status_code != 200:
        send_telegram_message(chat_id, message)
