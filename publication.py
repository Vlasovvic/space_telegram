import os
import random

from dotenv import load_dotenv

import argparse

import telegram_bot
import download


def main():
    load_dotenv()
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    frequency = int(os.getenv("FREQUENCY"))

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--frequency", help="set publication frequency")
    args = parser.parse_args()
    folder = "images"
    images_list = download.get_images_list(folder)

    while True:

        if args.frequency:
            telegram_bot.send_document(telegram_token, chat_id, images_list, args.frequency)
        else:
            telegram_bot.send_document(telegram_token, chat_id, images_list, frequency)
        random.shuffle(images_list)


if __name__ == "__main__":
    main()
