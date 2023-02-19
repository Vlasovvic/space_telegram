import os
from dotenv import load_dotenv

import argparse

import download
import fetch_spacex_images
import nasa_apod
import nasa_epic
import telegram_bot


def main():
    # env variables
    load_dotenv()
    nasa_token = os.getenv("NASA_TOKEN")
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    frequency = int(os.getenv("FREQUENCY"))
    
    # init
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--date", help="date in format YYYY-MM-DD")
    parser.add_argument("--spacexid", help="specific spacex launch id")
    parser.add_argument("--frequency", help="set publication frequency")
    args = parser.parse_args()
    folder = "images"

    while True:
        # download
        nasa_images = nasa_apod.fetch_nasa_apod(nasa_token)
        for image_number, image in enumerate(nasa_images):
            file_extension = download.get_file_extension(image)
            download.download_image(f"nasa_{image_number}{file_extension}", image, folder, None)

        epic_images = nasa_epic.fetch_nasa_epic(nasa_token, args.date)
        payload = {'api_key': nasa_token}
        for image_number, image in enumerate(epic_images):
            file_extension = download.get_file_extension(image)
            download.download_image(f"epic_{image_number}{file_extension}", image, folder, payload)

        spacex_images = fetch_spacex_images.fetch_spacex_last_launch(args.spacexid)
        for image_number, image in enumerate(spacex_images):
            file_extension = download.get_file_extension(image)
            download.download_image(f"spacex_{image_number}{file_extension}", image, folder, None)

        images_list = download.get_images_list(folder)

        # publication
        if args.frequency:
            telegram_bot.send_document(telegram_token, chat_id, images_list, args.frequency)
        else:
            telegram_bot.send_document(telegram_token, chat_id, images_list, frequency)

if __name__ == '__main__':
    main()
