from aiogram import Router, types, F
import app.DataBase as db
from app.Keyboards import short_inlineNoteKeyboard

router = Router()

@router.message(F.text == 'Просмотреть существующие заметки')
async def cmd_view_note(message: types.Message):

    await  message.answer('Ваши заметки:' ,  parse_mode="MarkdownV2")

    for key in  db.notes.keys():
        text = f' *{str(key)}*: {str(db.notes[key])}\n'
        await message.answer(text, parse_mode="MarkdownV2",reply_markup=short_inlineNoteKeyboard())


