"""
Module that stores custom filters created
"""
from telebot.custom_filters import AdvancedCustomFilter
from telebot.types import Message


class ContainsWordsFilter(AdvancedCustomFilter):
    key = 'contains_words'

    def check(self, message: Message, word: str) -> bool:
        text = message.text.lower()
        if not text:
            return False
        return word == text