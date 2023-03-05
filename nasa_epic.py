import requests
from datetime import datetime
import argparse
from dotenv import load_dotenv
from os import environ

import download


def fetch_nasa_epic(nasa_token, date):
    nasa_images = []
    payload = {"api_key": nasa_token}
    if date:
        url = f"https://api.nasa.gov/EPIC/api/natural/date/{date}"
    else:
        url = "https://api.nasa.gov/EPIC/api/natural"
    response = requests.get(f"{url}", params=payload)
    response.raise_for_status()
    nasa_content = response.json()
    for content in nasa_content:
        try:
            image_time, image_name = content['date'], content['image']
            a_date_time = datetime.fromisoformat(image_time)
            a_date_time = a_date_time.strftime("%Y-%m-%d")
            a_date_time = a_date_time.split("-")
            request_year, request_month, request_day = a_date_time[0], a_date_time[1], a_date_time[2]
            image_url = f"https://api.nasa.gov/EPIC/archive/natural/{request_year}/{request_month}/{request_day}/png/{image_name}.png"
            nasa_images.append(image_url)
        except BaseException as e:
            print(f"error:{e}, content = {content}")
    return nasa_images


def main():
    load_dotenv()
    nasa_token = environ["NASA_TOKEN"]
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--date", help="date in format YYYY-MM-DD", type=str)
    args = parser.parse_args()
    epic_images = fetch_nasa_epic(nasa_token, args.date)
    payload = {'api_key': nasa_token}
    for image_number, image in enumerate(epic_images):
        file_extension = download.get_file_extension(image)
        download.download_image(f"epic_{image_number}{file_extension}", image, "images", payload)


if __name__ == "__main__":
    main()
