import requests
import config

URL = "https://api.pushover.net/1/messages.json"


def send(title: str, message: str):
    body = {
        "token": config.push_token(),
        "user": config.push_user_key(),
        "title": title,
        "message": message,
    }
    requests.post(URL, json=body)
