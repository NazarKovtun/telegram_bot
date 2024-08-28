"""
Message storage module
"""
from telebot import types


help_message = ('/weather - <b>Дізнатися погоду в місті</b>\nВсе, що вам треба зробити це вписату назву населенного '
                'пункту\n/make_pass - <b>Генератор паролів</b>\nВам потрібно ввести довжину паролю і ви отримаєте 4 '
                'згенерованих паролі на вибір\n/convert - <b>Конвертер валют</b>\nВводите суму та обираєте потрібну '
                'валюту зі списку. Все!\n/calculate - <b>Калькулятор</b>\nВводите вираз та бот все підрахує. '
                'Впевніться, що вираз не має помилок. Бот підтримує математичні операціі Python, такі як + - / * // %\n'
                '/joke - <b>Випадковий жарт</b>\nБот надсилає випадковий короткий жарт\n/joke_twopart - <b>Випадковий '
                'жарт, що складається з двох частин</b>\nБот надсилає двохрядковий жарт (основна частина та кінець, що '
                'захований в спойлер)')

weather_message = ('Погода в {name} - {weather_desc}\n'
                   'Температура - {main_temp}℃\n'
                   'Вітер - {wind_speed}м/с')


def markup_start() -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('/weather')
    btn2 = types.KeyboardButton('/make_pass')
    btn3 = types.KeyboardButton('/convert')
    btn4 = types.KeyboardButton('/calculate')
    btn5 = types.KeyboardButton('/help')
    btn6 = types.KeyboardButton('/joke')
    btn7 = types.KeyboardButton('/joke_twopart')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    return markup
