from aiogram.types import CallbackQuery

from bot.database.requests import get_user

async def profile_handler(callback: CallbackQuery):
    user = await get_user(callback.from_user.id)

    if not user:
        await callback.answer("Вы не найдены в БД. Отпишите @aboba_keeper") # User-debug метод.(ток что выдумал) В последствии будет удален
        return
    
    await callback.message.edit_caption(
        caption=f"<b>👤 Профиль @{callback.from_user.username}:</b>\n\n"
        f"<b>💬 Ежедневное кол-во запросов:</b> {user.requests}\n"
        f"<b>🕛 Осталось запросов:</b> {user.remaining_requests}\n"
        f"<b>🗃️ Всего запросов:</b> {user.total_requests}\n\n"
        f"<b>🔮 Текущая модель:</b> {user.current_model}\n\n",

        reply_markup=None,

        parse_mode="HTML"
    )



