from urllib.parse import urlparse
import requests
from pathlib import Path
from os.path import join, splitext


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
