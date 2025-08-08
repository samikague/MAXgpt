from bot.utils.keyboards import get_start_keyboard
from bot.config import Images

from aiogram.types import Message


async def start(message: Message):
    await message.answer_photo(
        photo=Images.start_image,
        caption=f'<b>Привет, {message.from_user.first_name}!</b>\n\n<i>Я - MAX AI, твой персональный ассистент в мире нейросетей.</i>\n\n'
        f'<b>В моем каталоге есть множество AI-помощников для самых разных задач - от решения домашнего задания, до написания кода.</b>\n\n'
        f'Ниже представлен интерфейс, с помощью которого ты можешь пользоваться мной. Давай же начнем погружение вместе!',
        reply_markup=await get_start_keyboard(),
        parse_mode="HTML",
    )