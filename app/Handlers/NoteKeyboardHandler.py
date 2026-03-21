from aiogram import Router, types, F
import app.DataBase as db
from app.Keyboards import inlineNoteKeyboard, short_inlineNoteKeyboard
from app.config import CB_FULL, CB_DELETE, CB_FULL_VIEW

router = Router()

@router.callback_query(F.data == CB_FULL)
async def full_keyboard_note(callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=inlineNoteKeyboard())

@router.callback_query(F.data == CB_DELETE)
async def delete_note(callback: types.CallbackQuery):
    await callback.answer("Заметка удалена", show_alert=True)
    #TODO: удаление заметки из бд

@router.callback_query(F.data == CB_FULL_VIEW)
async def full_view_note(callback: types.CallbackQuery):
    await callback.answer('Тут ваша полная заметка',show_alert=True)
