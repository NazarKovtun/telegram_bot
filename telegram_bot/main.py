"""
This is a test telegram bot.
For start run this file.
Name Bot in Telegram:
@I_canHelpBot
"""
import telebot
from currency_converter import CurrencyConverter
from telebot import types, formatting

import config
import converter
import jokes
import make_pass
import messages
import my_filters
import notes_db
import weather

bot: telebot.TeleBot = telebot.TeleBot(config.BOT_TOKEN)
bot.add_custom_filter(my_filters.ContainsWordsFilter())

amount: int = 0
currency: CurrencyConverter = CurrencyConverter()
currencies_name: list[str] = []


# region start and help

@bot.message_handler(commands=['start'])
def start(message: types.Message) -> None:
    bot.send_message(
        message.chat.id,
        'Привіт, натисни команду /help, щоб дізнатися,що я вмію',
        reply_markup=messages.markup_start())


@bot.message_handler(commands=['help'])
def info(message: types.Message) -> None:
    bot.send_message(message.chat.id, messages.help_message, parse_mode='html')


# endregion

# region convert

@bot.message_handler(commands=['convert'])
def convert(message: types.Message) -> None:
    bot.send_message(message.chat.id, 'Введіть суму')
    bot.register_next_step_handler(message, summa)


def summa(message: types.Message) -> None:
    global amount
    amount = converter.get_amount(message)

    if amount is str:
        bot.reply_to(message, 'Невірний формат\nПовторно введіть суму')
        bot.register_next_step_handler(message, convert)
        return

    if amount > 0:
        bot.send_message(
            message.chat.id,
            'Оберіть пару валют',
            reply_markup=converter.markup_convert_1())

    else:
        bot.reply_to(message, 'Сума має бути бульше нуля')
        bot.register_next_step_handler(message, summa)


@bot.callback_query_handler(func=lambda callback: True)
def callback_convert(callback: types.CallbackQuery) -> None:
    global currencies_name, amount

    back: bool = False
    if callback.data == '<':
        back = True
    if callback.data in converter.pair:
        currencies_name.clear()
        currencies_name = callback.data.split('/')
        res = currency.convert(amount, currencies_name[0], currencies_name[1])
        bot.send_message(
            callback.message.chat.id,
            f'{amount} {currencies_name[0]} = {round(res, 2)} {currencies_name[1]}')

    elif callback.data == 'else' or (back and not currencies_name):
        bot.send_message(
            callback.message.chat.id,
            'Оберіть валюту з якої\nтреба конвертувати',
            reply_markup=converter.markup_convert_2())

    elif callback.data in converter.currency_lst and not currencies_name:
        currencies_name.append(callback.data)
        bot.send_message(
            callback.message.chat.id,
            'Оберіть валюту в яку\nтреба конвертувати',
            reply_markup=converter.markup_convert_2())

    elif back and currencies_name:
        bot.send_message(
            callback.message.chat.id,
            'Оберіть валюту в яку\nтреба конвертувати',
            reply_markup=converter.markup_convert_2())

    elif callback.data == '>':
        bot.send_message(
            callback.message.chat.id,
            'Оберіть валюту для\nконвертування',
            reply_markup=converter.markup_convert_3())

    elif callback.data in converter.currency_lst and currencies_name:
        currencies_name.append(callback.data)
        res = currency.convert(amount, currencies_name[0], currencies_name[1])
        bot.send_message(
            callback.message.chat.id,
            f'{amount} {currencies_name[0]} = {round(res, 2)} {currencies_name[1]}')
        currencies_name.clear()


# endregion

# region weather

@bot.message_handler(commands=['weather'])
def weather(message: types.Message) -> None:
    bot.send_message(message.chat.id, 'Впишіть назву населеного пункту)')
    bot.register_next_step_handler(message, get_weather)


def get_weather(message: types.Message) -> None:
    try:
        bot.reply_to(
            message,
            weather.get_weather_message(message))
    except KeyError:
        bot.reply_to(message, 'Невірна назва населеного пункту\nВпишіть назву корректно')
        bot.register_next_step_handler(message, get_weather)


# endregion

# region make_pass

@bot.message_handler(commands=['make_pass'])
def get_syms(message: types.Message) -> None:
    bot.send_message(message.chat.id, 'Введіть довжину паролю')
    bot.register_next_step_handler(message, get_length)


def get_length(message: types.Message) -> None:
    bot.send_message(
        message.chat.id,
        make_pass.make_password(message))


# endregion

# region calculate

@bot.message_handler(commands=['calculate'])
def start_calculate(message: types.Message) -> None:
    bot.send_message(message.chat.id, 'Введіть вираз, синтаксично вірно та без "="')
    bot.register_next_step_handler(message, calculate)


def calculate(message: types.Message) -> None:
    try:
        res: int | float = eval(message.text.strip())
        bot.send_message(message.chat.id, f'{res}')

    except (SyntaxError, NameError):
        bot.send_message(message.chat.id, 'Вираз введено не вірно, будь ласка,\nвведіть вираз ще раз')
        bot.register_next_step_handler(message, calculate)


# endregion

# region joke

@bot.message_handler(commands=['joke'])
def send_random_joke(message: types.Message):
    bot.send_message(
        message.chat.id,
        jokes.get_random_single_joke(),
        parse_mode='html')


@bot.message_handler(commands=['joke_twopart'])
def send_random_two_part_joke(message: types.Message):
    bot.send_message(
        message.chat.id,
        jokes.get_random_twopart_joke(),
        parse_mode='html')


# endregion

# region notes

@bot.message_handler(commands=['notes'])
def notes_handle(message: types.Message):
    notes_db.make_db()
    bot.send_message(
        message.chat.id,
        'Нотатки\nОберіть дію в меню',
        reply_markup=notes_db.markup_db())


@bot.message_handler(contains_words='створити нотатку')
def make_note_handle(message: types.Message):
    bot.send_message(message.chat.id, 'Введіть назву нотатки')
    bot.register_next_step_handler(message, make_note)


def make_note(message: types.Message):
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введіть текст нотатки')
    bot.register_next_step_handler(message, note, name)


def note(message, name):
    notes_db.make_note(message, name)
    bot.send_message(message.chat.id, 'Нотатку створено')


@bot.message_handler(contains_words='переглянути нотатки')
def show_note_handle(message: types.Message):
    bot.send_message(message.chat.id, 'Всі нотатки:')
    bot.register_next_step_handler(message, show_notes)


def show_notes(message: types.Message):
    text = notes_db.show_notes()
    if not text:
        text = 'Нотаток не має'
    bot.send_message(message.chat.id, text)


@bot.message_handler(contains_words='видалити нотатку')
def delete_note_handle(message: types.Message):
    bot.send_message(message.chat.id, 'Введіть назву нотатки')
    bot.register_next_step_handler(message, delete_note)


def delete_note(message: types.Message):
    text = notes_db.delete_note(message)
    if not text:
        bot.send_message(message.chat.id, 'Нотатку видалено')
    else:
        bot.send_message(message.chat.id, text)


# endregion


if __name__ == '__main__':
    bot.infinity_polling()
