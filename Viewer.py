from dotenv import load_dotenv
import os

import asyncio
from aiogram import Bot, Dispatcher, types, F

from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from States import CreateNote

####
notes = {'test': 'my note'}
####
load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Создать заметку")],
        [types.KeyboardButton(text="Просмотреть существующие заметки")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,resize_keyboard=True)
    await message.answer("Hello! This bot for your cool notes", reply_markup=keyboard)



@dp.message(StateFilter(None), F.text == 'Создать заметку')
async def cmd_create_note(message: types.Message, state: FSMContext):

    await  message.answer('Введите название заметки')
    await state.set_state(CreateNote.create_note_name)

@dp.message(CreateNote.create_note_name, F.text)
async def create_note_name(message: types.Message, state: FSMContext):
    #TODO: проверка содержания названия
    await state.update_data(create_note_name = message.text)
    await  state.set_state(CreateNote.create_note_desc)
    await message.answer("Введите содержание заметки")

@dp.message(CreateNote.create_note_desc, F.text)
async def create_note_text_desc(message: types.Message, state: FSMContext):
    note_data = await state.get_data()
    notes[note_data['create_note_name']] = message.text
    await message.answer('Заметка успешно создана!')
    await state.clear()

@dp.message(F.text == 'Просмотреть существующие заметки')
async def cmd_create_note(message: types.Message):

    await  message.answer('Ваши заметки:' ,  parse_mode="MarkdownV2")

    for key in  notes.keys():
        text = f' *{str(key)}*: {str(notes[key])}\n'
        await message.answer(text, parse_mode="MarkdownV2")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
