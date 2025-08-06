from bot.database.structure import User

async def register_user(telegram_id: int): # Надо проверить данную функцию, из-за того, что пока что ей нет применений в коде, написать под конец тесты
    user = await User.filter(User.telegram_id == telegram_id)
    if not user:
        user = User(telegram_id=telegram_id)
        try:
            await User.save(user)
        except Exception as e:
            raise e