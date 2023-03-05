import requests
import argparse

import download


def fetch_spacex_last_launch(spacexid):
    url = f"https://api.spacexdata.com/v5/launches/{spacexid}"
    response = requests.get(url)
    response.raise_for_status()
    spacex_content = response.json()
    spacex_images = spacex_content['links']['flickr']['original']
    return spacex_images


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--spacexid", help="launch spacex id", default="latest")
    args = parser.parse_args()
    spacex_images = fetch_spacex_last_launch(args.spacexid)
    if spacex_images:
        for image_number, image in enumerate(spacex_images):
            file_extension = download.get_file_extension(image)
            download.download_image(f"spacex_{image_number}{file_extension}", image, "images", None)
    else:
        print("current launch haven't photos")


if __name__ == "__main__":
    main()
