from aiogram import Router, types
from aiogram.filters import Command
from app.Keyboards import main_keyboard

router = Router()
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello! This bot for your cool notes", reply_markup=main_keyboard())

