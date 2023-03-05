import os
import random

from dotenv import load_dotenv

import argparse

import telegram_bot
import download_functions
import telegram


def main():
    load_dotenv()
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    frequency = int(os.getenv("FREQUENCY"))

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--frequency", help="set publication frequency", default=14400)
    args = parser.parse_args()
    folder = "images"
    images_list = download_functions.get_images_list(folder)

    while True:
        try:
            if args.frequency:
                telegram_bot.send_document(telegram_token, chat_id, images_list, args.frequency)
            else:
                telegram_bot.send_document(telegram_token, chat_id, images_list, frequency)
            random.shuffle(images_list)
        except telegram.error.NetworkError as e:
            for attempt in range(2):
                if telegram.Bot.answerCallbackQuery:
                    break
                else:
                    print(f"error: {e}, reconnect attempt={attempt}")
        print("out of attempts, exit")
        exit()


if __name__ == "__main__":
    main()
