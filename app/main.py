import asyncio

from aiogram import Dispatcher, Bot

from app.config import API_TOKEN
from Handlers import routers

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
dp.include_routers(*routers)

async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())