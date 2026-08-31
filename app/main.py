import asyncio

from aiogram import Dispatcher, Bot

from app.config import API_TOKEN
from .Handlers import routers
from .DataBase import _DataBase

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
db = _DataBase()
dp.include_routers(*routers)
dp.workflow_data["db"]= db
async def main():
    await db.init_db()
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())