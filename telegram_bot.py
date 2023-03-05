import os
import random

from dotenv import load_dotenv
import time
from pathlib import Path

import argparse
import telegram

import download_functions


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
    frequency = int(os.getenv("FREQUENCY"))

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--frequency", help="set publication frequency", default=14400)
    args = parser.parse_args()

    bot = telegram.Bot(token=telegram_token)
    while True:
        images_list = download_functions.get_images_list("images")
        message = send_document(telegram_token, chat_id, images_list, args.frequncy)
        random.shuffle(images_list)


if __name__ == "__main__":
    main()
