from aiogram import Router, types
from aiogram.filters import Command
from app.Keyboards import main_keyboard
from app.DataBase import _DataBase

router = Router()
@router.message(Command("start"))
async def cmd_start(message: types.Message, db: _DataBase):
    await message.answer("Hello! This bot for your cool notes", reply_markup=main_keyboard())
    user = message.from_user

    user_id = user.id
    username = user.username
    first_name = user.first_name
    language_code = user.language_code
    #TODO: обрабоотка языка
    await db.new_user(user_id, username, first_name, language_code)





