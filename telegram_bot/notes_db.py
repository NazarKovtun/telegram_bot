"""
Module for working with database
on the road command /notes
"""
import datetime
import sqlite3
from telebot import types


def markup_db() -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Створити нотатку')
    btn2 = types.KeyboardButton('Переглянути нотатки')
    btn3 = types.KeyboardButton('Видалити нотатку')
    markup.row(btn1)
    markup.row(btn2, btn3)
    return markup


def make_db() -> None:
    conn = sqlite3.connect('notes.sql')
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS notes (
    id int auto_increment primary key,
    date varchar(10),
    name TEXT NOT NULL,
    text TEXT)''')
    conn.commit()
    cur.close()
    conn.close()


def make_note(message: types.Message, name: str) -> None:
    conn = sqlite3.connect('notes.sql')
    cur = conn.cursor()

    today = datetime.date.today()
    text = message.text.strip()

    cur.execute('''
    INSERT INTO notes (date, name, text)
    VALUES (?, ?, ?)''', (today, name, text))
    conn.commit()
    cur.close()
    conn.close()


def show_notes() -> str:
    conn = sqlite3.connect('notes.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM notes')
    notes = cur.fetchall()

    text = ''
    for note in notes:
        text += f'Дата: {note[1]}\nНазва: {note[2]}\n\n{note[3]}\n\n'

    cur.close()
    conn.close()
    return text


def delete_note(message: types.Message) -> None | str:
    conn = sqlite3.connect('notes.sql')
    cur = conn.cursor()

    name = message.text.strip()

    cur.execute('SELECT name FROM notes')
    names = cur.fetchall()

    if name in names:
        cur.execute('''
        DELETE FROM notes
        WHERE name = ?''', (name,))
        conn.commit()
        cur.close()
        conn.close()
        return
    else:
        return 'Нотатку не знайдено'