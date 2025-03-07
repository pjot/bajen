import requests
import config
from pydantic import BaseModel

URL = "https://api.pushover.net/1/messages.json"


class Message(BaseModel):
    title: str
    message: str


def send(message: Message):
    body = {
        "token": config.push_token(),
        "user": config.push_user_key(),
        "title": message.title,
        "message": message.message,
    }
    requests.post(URL, json=body)
