from aiogram import  types

def inlineNoteKeyboard():
    kb = [
        [types.InlineKeyboardButton(text='Полностью',callback_data='full')],
        [types.InlineKeyboardButton(text='Удалить', callback_data='delete')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard = kb)
    return keyboard