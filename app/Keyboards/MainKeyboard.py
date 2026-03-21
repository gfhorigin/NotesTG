from aiogram import  types

def main_keyboard():
    kb = [
            [types.KeyboardButton(text="Создать заметку")],
            [types.KeyboardButton(text="Просмотреть существующие заметки")]
        ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard