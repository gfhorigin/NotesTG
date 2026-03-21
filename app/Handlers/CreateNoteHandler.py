from aiogram import Router, types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from app.Keyboards import main_keyboard
from app.States.NoteStates import CreateNote
import app.DataBase as db

router = Router()

@router.message(StateFilter(None), F.text == 'Создать заметку')
async def cmd_create_note(message: types.Message, state: FSMContext):

    await  message.answer('Введите название заметки')
    await state.set_state(CreateNote.create_note_name)

@router.message(CreateNote.create_note_name, F.text)
async def create_note_name(message: types.Message, state: FSMContext):
    #TODO: проверка содержания названия
    await state.update_data(create_note_name = message.text)
    await  state.set_state(CreateNote.create_note_desc)
    await message.answer("Введите содержание заметки")

@router.message(CreateNote.create_note_desc, F.text)
async def create_note_text_desc(message: types.Message, state: FSMContext):
    note_data = await state.get_data()
    db.notes[note_data['create_note_name']] = message.text
    await message.answer('Заметка успешно создана!', reply_markup=main_keyboard())
    await state.clear()

