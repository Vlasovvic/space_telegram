import requests
from dotenv import load_dotenv
from os import environ
import argparse

import download_functions


def fetch_nasa_apod(nasa_token, count):
    nasa_images = []
    payload = {"api_key": nasa_token, "count": count}
    response = requests.get("https://api.nasa.gov/planetary/apod", params=payload)
    response.raise_for_status()
    nasa_content = response.json()
    for content in nasa_content:
        if content['media_type'] == 'image':
            image_url = content['hdurl']
            nasa_images.append(image_url)
    return nasa_images


def main():
    load_dotenv()
    nasa_token = environ["NASA_TOKEN"]
    
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--count", help="set APOD photos count", default=30)
    args = parser.parse_args()

    nasa_images = fetch_nasa_apod(nasa_token, args.count)
    for image_number, image in enumerate(nasa_images):
        file_extension = download_functions.get_file_extension(image)
        download_functions.download_image(f"nasa_{image_number}{file_extension}", image, "images", None)


if __name__ == "__main__":
    main()
