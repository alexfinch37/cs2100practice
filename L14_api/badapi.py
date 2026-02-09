"""
Mutation practice
"""

import re

from nasaapi import NasaPic

##################################################

def is_valid_date1(_: str) -> bool:
    """Always False"""
    return False

def is_valid_date2(d: str) -> bool:
    """Only if today"""
    return d == '2026-02-09'

def is_valid_date3(d: str) -> bool:
    """Proper pattern, but not checking real dates"""
    return bool(re.match(
        re.compile(r"^\d{4}-\d{2}-\d{2}$"),
        d
    ))

#####

def process_nasa_response1(hd: bool, response: dict[str, str]) -> NasaPic:
    """No validation"""

    return NasaPic(
        response['date'],
        response['title'],
        response['explanation'],
        response['hdurl'] if hd else response['url']
    )

def process_nasa_response2(_: bool, response: dict[str, str]) -> NasaPic:
    """Always use regular hd"""

    return NasaPic(
        response['date'],
        response['title'],
        response['explanation'],
        response['url']
    )

def process_nasa_response3(hd: bool, response: dict[str, str]) -> NasaPic:
    """Only validate needed url"""

    needed_keys: set[str] = set(('date', 'title', 'explanation'))
    if hd:
        needed_keys.add('hdurl')
    else:
        needed_keys.add('url')

    actual_keys: set[str] = set(response.keys())

    if not needed_keys <= actual_keys:
        raise KeyError(f'Missing keys: {needed_keys - actual_keys}')

    return NasaPic(
        response['date'],
        response['title'],
        response['explanation'],
        response['hdurl'] if hd else response['url']
    )

def process_nasa_response4(hd: bool, response: dict[str, str]) -> NasaPic:
    """Always same date"""

    needed_keys: set[str] = set(('date', 'title', 'explanation', 'hdurl', 'url'))
    actual_keys: set[str] = set(response.keys())

    if not needed_keys <= actual_keys:
        raise KeyError(f'Missing keys: {needed_keys - actual_keys}')

    return NasaPic(
        '2026-02-06',
        response['title'],
        response['explanation'],
        response['hdurl'] if hd else response['url']
    )

def process_nasa_response5(hd: bool, response: dict[str, str]) -> NasaPic:
    """Swap title/explanation"""

    needed_keys: set[str] = set(('date', 'title', 'explanation', 'hdurl', 'url'))
    actual_keys: set[str] = set(response.keys())

    if not needed_keys <= actual_keys:
        raise KeyError(f'Missing keys: {needed_keys - actual_keys}')

    return NasaPic(
        response['date'],
        response['explanation'],
        response['title'],
        response['hdurl'] if hd else response['url']
    )

def process_nasa_response6(hd: bool, response: dict[str, str]) -> NasaPic:
    """Swap urls"""

    needed_keys: set[str] = set(('date', 'title', 'explanation', 'hdurl', 'url'))
    actual_keys: set[str] = set(response.keys())

    if not needed_keys <= actual_keys:
        raise KeyError(f'Missing keys: {needed_keys - actual_keys}')

    return NasaPic(
        response['date'],
        response['title'],
        response['explanation'],
        response['url'] if hd else response['hdurl']
    )

##################################################

def main() -> None:
    """Start!"""

if __name__ == "__main__":
    main()
