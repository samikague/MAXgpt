import os
import dotenv

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart

from bot.handlers.start import start

dotenv.load_dotenv()

async def register_handlers(dp: Dispatcher):
    dp.message.register(start, CommandStart())

async def run():
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()

    await register_handlers(dp)
    await dp.start_polling(bot)
