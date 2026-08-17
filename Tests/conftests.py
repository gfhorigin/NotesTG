import pytest
from unittest.mock import AsyncMock, MagicMock
from app.Handlers import start_router
from aiogram import Bot, Dispatcher
from aiogram.types import User, Message, Chat
from aiogram.methods import SendMessage
from app.DataBase import _DataBase

@pytest.fixture()
def mock_bot():
    bot = AsyncMock(spec = Bot)
    bot.send_message = AsyncMock()
    return bot

@pytest.fixture
def mock_message(mock_bot):
    user = User(id=123, is_bot=False,first_name='Test')
    chat = Chat(id=456, type='private')

    msg = AsyncMock(spec= Message)
    msg.from_user = user
    msg.chat = chat
    msg.text= ""

    msg.answer = AsyncMock()
    msg.bot = mock_bot
    return msg

@pytest.fixture
def mock_db():
    return AsyncMock(spec=_DataBase)
