from aiogram import  types

from app.config import CB_FULL


def short_inlineNoteKeyboard():
    kb = [
        [types.InlineKeyboardButton(text='...',callback_data=CB_FULL)]
   ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard = kb)
    return keyboard