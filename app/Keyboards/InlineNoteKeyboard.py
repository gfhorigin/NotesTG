from aiogram import  types
from app.Callbacks import CB_FULL_VIEW, CB_DELETE, NoteCallback


def inlineNoteKeyboard():
    kb = [
        [types.InlineKeyboardButton(text='Посмотреть',
                                    callback_data=NoteCallback(action = CB_FULL_VIEW, note_id = '0').pack())],
        [types.InlineKeyboardButton(text='Удалить',
                                    callback_data= NoteCallback(action = CB_DELETE, note_id = '0').pack())]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard = kb)
    return keyboard