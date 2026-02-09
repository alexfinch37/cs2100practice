"""
Fun with APIs
"""

from typing import Optional

from io import BytesIO
from datetime import datetime

from dataclasses import dataclass

import requests

import matplotlib.pyplot as plt
from PIL import Image

##################################################

# Get yours @ https://api.nasa.gov
# In general, do NOT include in repo
API_KEY: str = "DEMO_KEY"

@dataclass(frozen=True)
class NasaPic:
    """Info for a NASA APOD"""

    date: str
    title: str
    explanation: str
    url: str

#####

def is_valid_date(d: str) -> bool:
    """
    Checks if the string matches the YYYY-MM-DD format

    Parameters
    ==========
    d: str
        string to validate

    Returns
    =======
    bool
        True if the date is valid
        YYYY-MM-DD
    """

    try:
        datetime.strptime(d, "%Y-%m-%d")
        return True

    except ValueError:
        return False

def process_nasa_response(hd: bool, response: dict[str, str]) -> NasaPic:
    """
    Converts the NASA json response
    into a corresponding object

    Parameters
    ==========
    hd: bool
        keep the HD url or the regular one

    response: dict[str, str]
        python converson of nasa API JSON

    Returns
    =======
    NasaPic
        extracted API info

    Raises
    ======
    KeyError
        response doesn't have expected
        data ala the API spec; particularly
        the needed keys: (date, title, explanation, hdurl, url)
    """

    needed_keys: set[str] = set(('date', 'title', 'explanation', 'hdurl', 'url'))
    actual_keys: set[str] = set(response.keys())

    if not needed_keys <= actual_keys:
        raise KeyError(f'Missing keys: {needed_keys - actual_keys}')

    return NasaPic(
        response['date'],
        response['title'],
        response['explanation'],
        response['hdurl'] if hd else response['url']
    )

def get_pic_info(hd: bool, date: Optional[str] = None) -> NasaPic:
    """
    Gets NASA's Astronomy-Picture-Of-the-Day (APOD)

    Parameters
    ==========
    hd: bool
        determines if the URL is for
        the HD version of the pic

    date: Optional[str]
        if supplied, 'YYYY-MM-DD'
        format of which day to query

    Returns
    =======
    NasaPic
        info about today's pic!

    Raises
    ======
    requests.RequestException
        an error occurred!!

    ValueError
        date is invalid
    """

    params: dict[str, str] = {
        "api_key": API_KEY
    }

    if date:
        if not is_valid_date(date):
            raise ValueError

        params['date'] = date

    response = requests.get(
        "https://api.nasa.gov/planetary/apod",
        params=params,
        timeout=5.0
    )

    response.raise_for_status()

    return process_nasa_response(hd, response.json())


def display_image_from_url(url: str, title: str, subtitle: str) -> None:
    """
    Displays an image from a URL

    Parameters
    ==========
    url: str
        location of the image

    title: str
        primary title

    subtitle: str
        secondary title

    Raises
    ======
    requests.RequestException
        error fetching the image

    IOError
        error processing the image
    """

    img = Image.open(BytesIO(requests.get(url, timeout=5.0).content))
    plt.imshow(img)
    plt.title(title)
    plt.tick_params(
        left = False,
        bottom = False,
        labelleft = False,
        labelbottom = False
    )
    plt.xlabel(subtitle)
    plt.show()

def main() -> None:
    """Start!"""

    info: NasaPic = get_pic_info(True)
    display_image_from_url(
        info.url,
        info.title,
        info.date
    )

if __name__ == "__main__":
    main()
