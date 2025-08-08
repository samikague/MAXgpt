import os
import dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart

from bot.handlers.start import start
from bot.handlers.profile import profile_handler
from bot.database.structure import init_db, close_db
from bot.utils.middlewares import RegistrationMiddleware

dotenv.load_dotenv()

async def register_handlers(dp: Dispatcher):
    dp.message.register(start, CommandStart())
    dp.callback_query.register(profile_handler, F.data == "profile")

async def run(): # TODO: Добавить больше отладки, что для бд, что для бота в целом(перенести на loguru)
    try:
        await init_db()
    except Exception as e:
        print(f"Ошибка инициализации базы данных: {e}")
        return

    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()

    dp.message.middleware(RegistrationMiddleware())

    await register_handlers(dp)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await close_db()
