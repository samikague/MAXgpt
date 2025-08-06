import os
import dotenv

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart

from bot.handlers.start import start
from bot.database.structure import init_db, close_db

dotenv.load_dotenv()

async def register_handlers(dp: Dispatcher):
    dp.message.register(start, CommandStart())

async def run(): # TODO: Добавить больше отладки, что для бд, что для бота в целом(перенести на loguru)
    await init_db()

    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()

    await register_handlers(dp)
    try:
        await dp.start_polling(bot)
    finally:
        await close_db()
