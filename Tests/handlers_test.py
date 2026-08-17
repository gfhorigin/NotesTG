import pytest
from unittest.mock import AsyncMock
from app.Handlers.StartHandler import cmd_start
from Tests.conftests import mock_message, mock_bot, mock_db
from app.Keyboards import main_keyboard

@pytest.mark.asyncio
async def test_cmd_start(mock_message,mock_db):
    mock_message.text = "/start"

    await cmd_start(mock_message,mock_db)

    mock_message.answer.assert_awaited_once()
    args, kwargs = mock_message.answer.call_args

    assert args[0] == "Hello! This bot for your cool notes" #TODO: в будущем переделать под локализацию
    assert kwargs.get("reply_markup") == main_keyboard()
