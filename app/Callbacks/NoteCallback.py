from aiogram.filters.callback_data import CallbackData

from app.config import NOTE_PREFIX


class NoteCallback(CallbackData, prefix=NOTE_PREFIX):
    action: str
    note_id: str
