from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

async def get_start_keyboard():
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(text="👤 Профиль", callback_data="profile"))
    keyboard.add(InlineKeyboardButton(text="🤖 Сменить модель", callback_data="change_model"))
    keyboard.add(InlineKeyboardButton(text="📝 Пользовательское соглашение", url="https://legal.max.ru/ps"))
    keyboard.add(InlineKeyboardButton(text="🌐 Смена языка", callback_data="change_language")) # Заготовка под последущую мультиязычность

    return keyboard.adjust(2).as_markup()