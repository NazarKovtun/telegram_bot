"""
Module for working with CurrencyConverter
"""
from telebot import types

pair: list[str] = ['USD/EUR', 'USD/GBP', 'EUR/USD', 'EUR/GBP', 'GBP/USD', 'GBP/EUR']
currency_lst: list[str] = ['USD', 'JPY', 'GBN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'SEK', 'CHF', 'ISK',
                           'NOK', 'TRY', 'AUD', 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'ILS', 'INR', 'KRW', 'MXN',
                           'MYR', 'NZD', 'PHP', 'SGD', 'THB', 'ZAR']


def get_amount(message: types.Message) -> int | str:
    try:
        amount = int(message.text.strip())
        return amount
    except ValueError:
        return 'Невірний формат\nПовторно введіть суму'


def markup_convert_1() -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='USD/EUR')
    btn2 = types.InlineKeyboardButton('USD/GBP', callback_data='USD/GBP')
    btn3 = types.InlineKeyboardButton('EUR/USD', callback_data='EUR/USD')
    btn4 = types.InlineKeyboardButton('EUR/GBP', callback_data='EUR/GBP')
    btn5 = types.InlineKeyboardButton('GBP/USD', callback_data='GBP/USD')
    btn6 = types.InlineKeyboardButton('GBP/EUR', callback_data='GBP/EUR')
    btn7 = types.InlineKeyboardButton('Інше', callback_data='else')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    return markup


def markup_convert_2() -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup(row_width=3)
    btn1 = types.InlineKeyboardButton('USD', callback_data='USD')
    btn2 = types.InlineKeyboardButton('JPY', callback_data='JPY')
    btn3 = types.InlineKeyboardButton('GBN', callback_data='GBN')
    btn4 = types.InlineKeyboardButton('CZK', callback_data='CZK')
    btn5 = types.InlineKeyboardButton('DKK', callback_data='DKK')
    btn6 = types.InlineKeyboardButton('GBP', callback_data='GBP')
    btn7 = types.InlineKeyboardButton('HUF', callback_data='HUF')
    btn8 = types.InlineKeyboardButton('PLN', callback_data='PLN')
    btn9 = types.InlineKeyboardButton('RON', callback_data='RON')
    btn10 = types.InlineKeyboardButton('SEK', callback_data='SEK')
    btn11 = types.InlineKeyboardButton('CHF', callback_data='CHF')
    btn12 = types.InlineKeyboardButton('ISK', callback_data='ISK')
    btn13 = types.InlineKeyboardButton('NOK', callback_data='NOK')
    btn14 = types.InlineKeyboardButton('TRY', callback_data='TRY')
    btn15 = types.InlineKeyboardButton('AUD', callback_data='AUD')
    btn0 = types.InlineKeyboardButton('>', callback_data='>')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn0)

    return markup


def markup_convert_3() -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup(row_width=3)
    btn1 = types.InlineKeyboardButton('BRL', callback_data='BRL')
    btn2 = types.InlineKeyboardButton('CAD', callback_data='CAD')
    btn3 = types.InlineKeyboardButton('CNY', callback_data='CNY')
    btn4 = types.InlineKeyboardButton('HKD', callback_data='HKD')
    btn5 = types.InlineKeyboardButton('IDR', callback_data='IDR')
    btn6 = types.InlineKeyboardButton('ILS', callback_data='ILS')
    btn7 = types.InlineKeyboardButton('INR', callback_data='INR')
    btn8 = types.InlineKeyboardButton('KRW', callback_data='KRW')
    btn9 = types.InlineKeyboardButton('MXN', callback_data='MXN')
    btn10 = types.InlineKeyboardButton('MYR', callback_data='MYR')
    btn11 = types.InlineKeyboardButton('NZD', callback_data='NZD')
    btn12 = types.InlineKeyboardButton('PHP', callback_data='PHP')
    btn13 = types.InlineKeyboardButton('SGD', callback_data='SGD')
    btn14 = types.InlineKeyboardButton('THB', callback_data='THB')
    btn15 = types.InlineKeyboardButton('ZAR', callback_data='ZAR')
    btn0 = types.InlineKeyboardButton('<', callback_data='<')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn0)
    return markup