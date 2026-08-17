import aiosqlite
import _asyncio
from app.config import DATABASE_NAME, USERS_TABLE, NOTES_TABLE


class DataBase:
    def __init__(self, db_path: str = DATABASE_NAME):
        self.db_path = db_path
    async def init_db(self):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""PRAGMA foreign_keys = ON""")
            await db.execute(f"""
                CREATE TABLE IF NOT EXISTS {USERS_TABLE}(
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    first_name TEXT,
                    language_code TEXT)
                """)
            await db.execute(f"""
                CREATE TABLE IF NOT EXISTS {NOTES_TABLE}(
                    user_id INTEGER NOT NULL ,
                    notes_id INTEGER PRIMARY KEY,
                    name TEXT,
                    description TEXT,
                    FOREIGN KEY (user_id) REFERENCES {USERS_TABLE}(user_id) ON DELETE CASCADE)
                """)
            await db.commit()

    async def new_user(self,
                       user_id: int,
                       username: str,
                       first_name: str,
                       language_code: str):
        #TODO: проверка пользователя на уникальность
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                INSERT INTO users (user_id, username, first_name, language_code) VALUES (?,?,?,?)
                """, (user_id,username,first_name, language_code))
            await db.commit()

