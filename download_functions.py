import os
from urllib.parse import urlparse
import requests
from pathlib import Path
from os.path import join, splitext


def get_images_list(folder):
    for dirpath, dirnames, filenames in os.walk(folder):
        images_list = filenames
    return images_list


def download_image(filename, url, save_path, payload):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    Path(save_path).mkdir(parents=True, exist_ok=True)

    with open(join(save_path, filename), 'wb') as file:
        file.write(response.content)


def get_file_extension(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    split_name = splitext(path)
    file_extension = split_name[1]
    return file_extension


def main(file_list):
    for image_number, image in enumerate(file_list):
        file_extension = get_file_extension(image)
        download_image(f"spacex_{image_number}{file_extension}", image, "images", None)


if __name__ == "__main__":
    main([])
