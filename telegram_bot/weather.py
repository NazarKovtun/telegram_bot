import json
import requests
from telebot import types
from config import WEATHER_API, OPEWEATHER_URL
from messages import weather_message


def get_weather_message(message: types.Message) -> str:
    city: str = message.text.strip().lower()
    res: requests.Response = requests.get(OPEWEATHER_URL.format(city=city, api=WEATHER_API))
    data: dict = json.loads(res.text)
    new_message: str = weather_message.format(
        name=data['name'],
        weather_desc=data['weather'][0]['description'],
        main_temp=data['main']['temp'],
        wind_speed=data['wind']['speed'])
    return new_message