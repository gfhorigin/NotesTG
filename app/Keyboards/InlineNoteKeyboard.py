from aiogram import  types

from app.config import CB_FULL_VIEW, CB_DELETE


def inlineNoteKeyboard():
    kb = [
        [types.InlineKeyboardButton(text='Посмотреть',callback_data=CB_FULL_VIEW)],
        [types.InlineKeyboardButton(text='Удалить', callback_data=CB_DELETE)]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard = kb)
    return keyboard