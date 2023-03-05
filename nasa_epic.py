import requests
from datetime import datetime
import argparse
from dotenv import load_dotenv
from os import environ

import download_functions


def fetch_nasa_epic(nasa_token, date):
    nasa_images = []
    payload = {"api_key": nasa_token}
    url = f"https://api.nasa.gov/EPIC/api/natural/date/{date}"
    response = requests.get(url, params=payload)
    response.raise_for_status()
    nasa_content = response.json()
    for content in nasa_content:
        try:
            image_time, image_name = content['date'], content['image']
            a_date_time = datetime.fromisoformat(image_time)
            a_date_time = a_date_time.strftime("%Y/%m/%d")
            image_url = f"https://api.nasa.gov/EPIC/archive/natural/{a_date_time}/png/{image_name}.png"
            nasa_images.append(image_url)
        except BaseException as e:
            print(f"error:{e}, content = {content}")
    return nasa_images


def main():
    load_dotenv()
    nasa_token = environ["NASA_TOKEN"]
    parser = argparse.ArgumentParser(description="")
    format_today = datetime.today().strftime("%Y-%m-%d")
    parser.add_argument("--date", help="date in format YYYY-MM-DD", type=str, default=format_today)
    args = parser.parse_args()
    epic_images = fetch_nasa_epic(nasa_token, args.date)
    payload = {'api_key': nasa_token}
    for image_number, image in enumerate(epic_images):
        file_extension = download_functions.get_file_extension(image)
        download_functions.download_image(f"epic_{image_number}{file_extension}", image, "images", payload)


if __name__ == "__main__":
    main()
