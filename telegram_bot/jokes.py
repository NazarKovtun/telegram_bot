"""
Module for working with JokeAPI
"""
import requests
from telebot import formatting

JOKES_API_BASE_URL = 'https://v2.jokeapi.dev/joke/Programming,Pun'


def get_joke(joke_type: str | None) -> dict | None:
    url = JOKES_API_BASE_URL
    params = {
        'lang': 'en',
        'blacklistFlags': 'nsfw,religious,political,racist,sexist,explicit',
        'type': 'single'
    }
    if joke_type:
        params['type'] = joke_type
    response = requests.get(url, params=params)

    if response.status_code != 200:
        return

    json_data: dict = response.json()

    if json_data.get('error'):
        return

    return json_data


def get_random_single_joke():
    json_data = get_joke('single')

    if not json_data:
        return 'Error'

    return json_data['joke']


def get_random_twopart_joke() -> str:
    json_data = get_joke('twopart')

    if not json_data:
        return 'Error'

    text = formatting.format_text(
        formatting.escape_html(json_data['setup']),
        formatting.hspoiler(json_data['delivery'])
    )

    return text