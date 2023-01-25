import os
from dotenv import load_dotenv

import telegram

def main():
    load_dotenv()
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    bot = telegram.Bot(token=telegram_token)
    message = bot.send_photo(chat_id=chat_id, photo=open("images/epic_0.png", 'rb'))


if __name__ == "__main__":
    main()