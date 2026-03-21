from aiogram import Router, types, F
import app.DataBase as db
from app.Keyboards import inlineNoteKeyboard

router = Router()

@router.message(F.text == 'Просмотреть существующие заметки')
async def cmd_view_note(message: types.Message):

    await  message.answer('Ваши заметки:' ,  parse_mode="MarkdownV2")

    for key in  db.notes.keys():
        text = f' *{str(key)}*: {str(db.notes[key])}\n'
        await message.answer(text, parse_mode="MarkdownV2",reply_markup=inlineNoteKeyboard())


# @router.callback_query(F.data == 'full')
# async def full_note(callback: types.CallbackQuery):
#     await callback.answer("Показываю полную заметку...")
#     # Ваша логика
#
# @router.callback_query(F.data == 'delete')
# async def delete_note(callback: types.CallbackQuery):
#     await callback.answer("Заметка удалена", show_alert=True)
#     # Ваша логика