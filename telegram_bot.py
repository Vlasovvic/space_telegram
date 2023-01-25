import os
from dotenv import load_dotenv

import telegram

def main():
    load_dotenv()
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    bot = telegram.Bot(token=telegram_token)
    bot.send_message(chat_id=chat_id, text="sample_text")

if __name__ == "__main__":
    main()