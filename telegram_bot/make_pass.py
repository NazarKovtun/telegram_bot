"""
Password creation module
"""
import string
import random
from telebot.types import Message

SYMS = string.ascii_letters + string.digits


def make_password(message: Message) -> str:
    try:
        length = int(message.text.strip())
        res: str = ''
        password: str = ''

        for n in range(4):
            rnd_syms = random.choices(SYMS, k=length)
            for i in rnd_syms:
                password += i
            res += password + '\n'
            password = ''
        return res

    except ValueError:
        return f'Неккоректне значення {message.text} Введіть число!'