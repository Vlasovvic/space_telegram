import requests
from dotenv import load_dotenv
from os import environ

import download_functions


def fetch_nasa_apod(nasa_token):
    nasa_images = []
    payload = {"api_key": nasa_token, "count": 30}
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
    nasa_images = fetch_nasa_apod(nasa_token)
    for image_number, image in enumerate(nasa_images):
        file_extension = download_functions.get_file_extension(image)
        download_functions.download_image(f"nasa_{image_number}{file_extension}", image, "images", None)


if __name__ == "__main__":
    main()
