from aiogram.fsm.state import StatesGroup, State

class CreateNote(StatesGroup):
    create_note_name = State()
    create_note_desc = State()