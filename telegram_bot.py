import os
from dotenv import load_dotenv
import time
from pathlib import Path

import telegram


def send_document(token, chat_id, images, sleep):
    bot = telegram.Bot(token=token)
    for image in images:
        image_path = Path("images", image)
        with open(image_path, 'rb') as document:
            bot.send_document(chat_id=chat_id, document=document)
            time.sleep(sleep)


def main():
    load_dotenv()
    telegram_token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    bot = telegram.Bot(token=telegram_token)
    while True:
        message = bot.send_photo(chat_id=chat_id, photo=open("images/epic_0.png", 'rb'))


if __name__ == "__main__":
    main()
