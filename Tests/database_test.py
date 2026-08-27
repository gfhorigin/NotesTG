import pytest
from unittest.mock import AsyncMock
from app.Handlers.StartHandler import cmd_start
from app.DataBase import _DataBase
import aiosqlite

from app.config import NOTES_TABLE, USERS_TABLE


@pytest.mark.asyncio
async def test_init_db():
    TEMP_NAME = "temp.db"
    db = _DataBase(TEMP_NAME)
    await db.init_db()

    async with aiosqlite.connect(TEMP_NAME) as con:
        cur = await con.execute("""SELECT name FROM sqlite_master WHERE type = 'table'""")
        tables = await cur.fetchall()
        table_names = [row[0] for row in tables]

        assert USERS_TABLE in table_names
        assert NOTES_TABLE in table_names