import os
from dotenv import load_dotenv
from datetime import datetime
import argparse

import download_functions
import fetch_spacex_images
import nasa_apod
import nasa_epic


def main():
    # env variables
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]

    # init
    format_today = datetime.today().strftime("%Y-%m-%d")
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--date", help="date in format YYYY-MM-DD", default=format_today)
    parser.add_argument("--spacexid", help="specific spacex launch id", default="latest")
    parser.add_argument("--count", help="set APOD photos count", default=30)
    args = parser.parse_args()
    folder = "images"

    # download
    nasa_images = nasa_apod.fetch_nasa_apod(nasa_token, args.count)
    for image_number, image in enumerate(nasa_images):
        file_extension = download_functions.get_file_extension(image)
        download_functions.download_image(f"nasa_{image_number}{file_extension}", image, folder, None)

    epic_images = nasa_epic.fetch_nasa_epic(nasa_token, args.date)
    payload = {'api_key': nasa_token}
    for image_number, image in enumerate(epic_images):
        file_extension = download_functions.get_file_extension(image)
        download_functions.download_image(f"epic_{image_number}{file_extension}", image, folder, payload)

    spacex_images = fetch_spacex_images.fetch_spacex_last_launch(args.spacexid)
    for image_number, image in enumerate(spacex_images):
        file_extension = download_functions.get_file_extension(image)
        download_functions.download_image(f"spacex_{image_number}{file_extension}", image, folder, None)


if __name__ == '__main__':
    main()
