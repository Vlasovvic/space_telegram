import os
from dotenv import load_dotenv

import argparse

import common_use_functions
import fetch_spacex_images
import nasa_apod
import nasa_epic


def main():
    load_dotenv()
    nasa_token = os.getenv("NASA_TOKEN")
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--date", help="date in format YYYY-MM-DD")
    parser.add_argument("--spacexid", help="")
    args = parser.parse_args()

    nasa_images = nasa_apod.fetch_nasa_apod(nasa_token)
    for image_number, image in enumerate(nasa_images):
        file_extension = common_use_functions.get_file_extension(image)
        common_use_functions.download_image(f"nasa_{image_number}{file_extension}", image, "images", None)

    epic_images = nasa_epic.fetch_nasa_epic(nasa_token, args.date)
    payload = {'api_key': nasa_token}
    for image_number, image in enumerate(epic_images):
        file_extension = common_use_functions.get_file_extension(image)
        common_use_functions.download_image(f"epic_{image_number}{file_extension}", image, "images", payload)

    spacex_images = fetch_spacex_images.fetch_spacex_last_launch(args.spacexid)
    for image_number, image in enumerate(spacex_images):
        file_extension = common_use_functions.get_file_extension(image)
        common_use_functions.download_image(f"spacex_{image_number}{file_extension}", image, "images", None)


if __name__ == '__main__':
    main()
