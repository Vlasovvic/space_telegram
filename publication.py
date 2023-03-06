import os
import random
import time

from dotenv import load_dotenv

import argparse

import telegram_bot
import download_functions
import telegram


def main():
    load_dotenv()
    telegram_token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--frequency", help="set publication frequency", default=14400)
    args = parser.parse_args()
    folder = "images"
    images_list = download_functions.get_images_list(folder)

    while True:
        try:
            telegram_bot.send_document(telegram_token, chat_id, images_list, args.frequency)
            random.shuffle(images_list)
        except telegram.error.NetworkError as e:
            attempt = 0
            if telegram.Bot.answerCallbackQuery:
                break
            else:
                print(f"error: {e}, reconnect attempt={attempt}")
                time.sleep(15)


if __name__ == "__main__":
    main()
