import requests
import argparse

import common_use_functions


def fetch_spacex_last_launch(id):
    if id:
        url = f"https://api.spacexdata.com/v5/launches/{id}"
    else:
        url = "https://api.spacexdata.com/v5/launches/latest"
    response = requests.get(f"{url}")
    response.raise_for_status()
    spacex_content = response.json()
    spacex_images = spacex_content['links']['flickr']['original']
    return spacex_images


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", help="launch id")
    args = parser.parse_args()
    spacex_images = fetch_spacex_last_launch(args.id)
    if spacex_images:
        for image_number, image in enumerate(spacex_images):
            file_extension = common_use_functions.get_file_extension(image)
            common_use_functions.download_image(f"spacex_{image_number}{file_extension}", image, "images", None)
    else:
        print("current launch haven't photos")

if __name__ == "__main__":
    main()
