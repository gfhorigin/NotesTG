import aiosqlite
import _asyncio
from app.config import DATABASE_NAME


class DataBase:
    async def init_db(self):
        async with aiosqlite.connect(DATABASE_NAME) as db:
            await db.execute("""PRAGMA foreign_keys = ON""")
            await db.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    first_name TEXT,
                    language_code TEXT)
                """)
            await db.execute("""
                CREATE TABLE IF NOT EXISTS notes(
                    user_id INTEGER NOT NULL ,
                    notes_id INTEGER PRIMARY KEY,
                    name TEXT,
                    description TEXT,
                    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE)
                """)
            await db.commit()

    async def new_user(self,
                       user_id: int,
                       username: str,
                       first_name: str,
                       language_code: str):

        async with aiosqlite.connect(DATABASE_NAME) as db:
            await db.execute("""
                INSERT INTO users (user_id, username, first_name, language_code) VALUES (?,?,?,?)
                """, (user_id,username,first_name, language_code))
            await db.commit()

